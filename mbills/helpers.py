import warnings

from decimal import Decimal

from django.conf import settings

from python_mbills.api import MBillsAPI
from python_mbills.exceptions import SignatureValidationException

from mbills.models import MBillsTransaction


MBILLS_RSA_PUBLIC_KEY = getattr(settings, 'MBILLS_RSA_PUBLIC_KEY', None)
MBILLS_API_KEY = getattr(settings, 'MBILLS_API_KEY', None)
MBILLS_SECRET_KEY = getattr(settings, 'MBILSS_SECRET_KEY', None)

MBILLS_API_ENDPOINT = getattr(settings, 'MBILSS_API_ENDPOINT', 'https://demo3.halcom.com/MBillsWS')

if MBILLS_API_KEY is None or MBILLS_SECRET_KEY is None:
    warnings.warn("Missing MBILLS_API_KEY and/or MBILLS_SECRET_KEY from settings. API calls will fail!")

if MBILLS_RSA_PUBLIC_KEY is None:
    warnings.warn("Failed to load MBILLS_RSA_PUBLIC_KEY from settings. None of the API calls will be verified!")


# Configure the class only once...better than loading everytime a request is made...
mbills_api = MBillsAPI(api_key=MBILLS_API_KEY, shared_secret=MBILLS_SECRET_KEY, mbills_rsa_pub_key=MBILLS_RSA_PUBLIC_KEY,
                       nonce_length=10, api_endpoint=MBILLS_API_ENDPOINT)


def generate_new_transaction(amount, purpose, payment_reference=None, order_id=None, channel_id=None, capture=True):
    """
    Create a new transaction object. 
    
    :param amount: 
    :param purpose: 
    :param payment_reference: 
    :param order_id: 
    :param channel_id: 
    :param capture: 
    :return: 
    """
    tx_id, token_number, status = mbills_api.create_new_sale(amount, purpose, payment_reference, order_id, channel_id, capture)

    mbills_transaction = MBillsTransaction(transaction_id=tx_id,
                                           currency=mbills_api.currency,
                                           purpose=purpose,
                                           payment_reference=payment_reference,
                                           capture=capture,
                                           order_id=order_id,
                                           channel_id=channel_id,
                                           payment_token_number=token_number,
                                           status=status,
                                           ).save()

    return mbills_transaction


def update_transaction_status(transaction):
    """
    Update the transaction status and return the refreshed transcation object
    :param transaction: 
    :return: 
    """
    tx_json = mbills_api.fetch_transaction_status(transaction_id=transaction.transaction_id)

    return _update_transaction_from_data(transaction, tx_json)


def handle_webhook(json_data):
    """
    Fetch the transaction from the database and update it's status.
    
    If the transaction does not exist in the database this function will 
    raise a DoesNotExist exception on the MBillsTransaction object.
    
    If the received webhook data server signature is not valid it will raise SignatureValidationException exception.
    
    :param json_data: data received from the webhook
    :return: 
    """
    if not mbills_api.base.verify_response(json_data):
        raise SignatureValidationException('Server signature verification has failed')

    transaction = MBillsTransaction.objects.get(transaction_id=json_data.get('transactionid'))

    return _update_transaction_from_data(transaction, json_data)


def _update_transaction_from_data(transaction, json_data):
    # Update the fields...
    transaction.status = json_data.get('status', transaction.status)
    transaction.settled_amount = Decimal(json_data.get('settledamount', 0) / 100.0)
    transaction.fees = Decimal(json_data.get('fees', 0) / 100.0)
    transaction.transaction_type = json_data.get('transactiontype', transaction.transaction_type)

    transaction.save()

    return transaction

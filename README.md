# Django MBills

Django MBills library wraps around [*python-mbills*](https://github.com/boris-savic/python-mbills) in order to provide Django functionality. 

The library is pretty lightweight only containing one model and a few helper functions. APIs should be implemented by the main app as most of you use different frameworks and workflows.

## Installation

    $ pip install django-mbills

## Quick Start

1. Add *mbills* to installed apps:

     
    INSTALLED_APPS = [
        ...
        
        'mbills',
        
        ...
    ]


2. Run migrations
     
     
    $ python manage.py migrate


3. Configure settings

There are 4 settings you have to configure before you can use the app.

In your `settings.py` set the following variables:

- **MBILLS_RSA_PUBLIC_KEY** - public RSA key of the MBills API. 
- **MBILLS_API_KEY** - your API key
- **MBILLS_SECRET_KEY** - your secret key
- **MBILLS_API_ENDPOINT** - MBills server endpoint. Defaults to their test server demo3.halcome.com/MBillsWS


3. Implement your API

In your API calls or Views you can issue calls to:

1. Generate a new transaction

```python
tx = generate_new_transaction(amount, purpose, payment_reference=None, order_id=None, channel_id=None, capture=True)
```

2. Update transaction status
```python
tx = update_transaction_status(tx)
```

3. Handle webhook received data (might raise SignatureValidationException and DoesNotExist)

```python
tx = handle_webhook(json_data)
```

For more detailed documentation check the project source.

## Contact

**Boris Savic**

 * Twitter: [@zitko](https://twitter.com/zitko)
 * Email: boris70@gmail.com

# Django MBills

Django MBills library wraps around *python-mbills* in order to provide Django functionality. 

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



3. Implement your API

In your API calls or Views you can issue calls to:

    - generate_new_transaction
    - update_transaction_status
    - handle_webhook
    


For more detailed documentation check the project source.


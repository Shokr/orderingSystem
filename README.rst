Order System
===============

Muhammed Shokr | Back End Engineer – Interview Task Solution
mohammedshokr2014@gmail.com

Run project
---------------

::


  $ virtualenv -p python3 venv
  $ source venv/bin/activate
  $ pip install -r requirements.txt
  $ python manage.py migrate
  $ python manage.py collectstatic
  $ python manage.py runserver # Or gunicorn config.wsgi:application --log-file -



Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

* To generate reset user table and create 3 User, use this command::

    $ python manage.py reset_users


Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Fixer API
^^^^^^^^^^^^^^^^^^^^^

* updated rates from fixer.io, use this command::

    $ python manage.py update_rates

* Successfully cleared rates for fixer.io, use this command::

    $ python manage.py clear_rates


Testing Accounts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Admin
    - Username: muhammed, Password: 123456789
* Normal User
    - Username: nader, Password: 123456789


API ENDPOINTS
---------------
* API swagger-ui :- http://127.0.0.1:8000/swagger/

API DOCS
-------------
* API ReDoc :- http://127.0.0.1:8000/redoc/


URLS List
----------------
* Admin Protal :- http://127.0.0.1:8000/admin/
* API :- http://127.0.0.1:8000/api/
* API swagger-ui :- http://127.0.0.1:8000/swagger/
* API ReDoc :- http://127.0.0.1:8000/redoc/
* JSON view of API specification :- http://127.0.0.1:8000/swagger.json
* YAML view of your API specification :- http://127.0.0.1:8000/swagger.yaml

Flask-PyFCM
===============================
[![Build Status](https://travis-ci.org/rstit/flask-pyfcm.svg?branch=master)](https://travis-ci.org/rstit/flask-pyfcm)

version number: 0.0.1

contributor: Piotr Poteralski

Overview
--------

Flask extension for PyFCM - Python client for FCM

Installation
--------------------

To install use pip:
```bash
$ pip install Flask-PyFCM
```

Or clone the repo:
```bash
$ git clone https://github.com/rstit/flask-airbrake.git
$ python setup.py install
```
Usage
-----
You’ll need to do, is setup config:
```python
# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging
FCM_API_KEY = os_env.get('FCM_API_KEY')
# Not required proxy dict
FCM_PROXY_DICT = {
    "http"  : "http://127.0.0.1",
    "https" : "http://127.0.0.1",
}
```

Then initialize PyFCM under your application:
```python
from flask_pyfcm import FCM
fcm = FCM()

def create_app():
    app = Flask(__name__)
    fcm.init_app(app)
    return app
```

You can implement handler for getting bad ids to your devices implementation:
For example: SQLAlchemy:
```python
@fcm.failure_handler
def handle_bad_ids(ids, *args):
    for device in Device.query.filter(Device.id.in_(ids)):
        device.mark_as_inactive()
```
Contributing
------------

TBD

TODO
------------
* Coverage
* Docs
from unittest import TestCase

from flask import Flask
from flask import _app_ctx_stack as stack
from flask_pyfcm import FCM
from pyfcm import FCMNotification

class FCMExtensionTest(TestCase):

    def setUp(self):
        self.app = Flask('unit_tests')


        self.fcm = FCM()

        def create_app():
            app = Flask(__name__)
            app.config['FCM_API_KEY'] = 'test-key'
            app.config['FCM_PROXY_DICT'] = {}
            self.fcm.init_app(app)
            return app

        self.app = create_app()

    def test_001_application_context(self):
        with self.app.app_context():
            self.fcm.push_service
            self.assertIsInstance(stack.top.fcm_service, FCMNotification)

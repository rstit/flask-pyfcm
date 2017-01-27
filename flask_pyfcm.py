from flask import current_app
from pyfcm import FCMNotification

# Find the stack on which we want to store PyFCM client.
# Starting with Flask 0.9, the _app_ctx_stack is the correct one,
# before that we need to use the _request_ctx_stack.
try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack


class FCM(object):
    FCM_INVALID_ID_ERRORS = [
        'InvalidRegistration',
        'NotRegistered',
        'MismatchSenderId'
    ]

    def __init__(self, app=None):
        self.app = app
        self._failure_handler = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault("FCM_API_KEY", "")
        app.config.setdefault("FCM_PROXY_DICT", None)

    @property
    def push_service(self):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'fcm_service'):
                ctx.fcm_service = FCMNotification(
                    api_key=current_app.config['FCM_API_KEY'],
                    proxy_dict=current_app.config['FCM_PROXY_DICT']
                )
            return ctx.fcm_service

    def notify_single_device(self, registration_id, *args, **kwargs):
        self.notify_multiple_devices([registration_id], **kwargs)

    def notify_multiple_devices(self, registration_ids, **kwargs):
        response = self.push_service.notify_multiple_devices(registration_ids,
                                                             **kwargs)
        if response.get('failure'):
            id_and_responses = zip(registration_ids, response.get('results'))
            filtered = filter(
                lambda x: x[1].get('error') in self.FCM_INVALID_ID_ERRORS,
                id_and_responses
            )
            invalid_messages = dict(filtered)
            invalid_ids = list(invalid_messages.keys())
            if self._failure_handler:
                self._failure_handler(invalid_ids, invalid_messages)
            return False
        return True

    def failure_handler(self, f):
        """Register a handler for getting bad ids.
        fcm = FcM()
        fcm.push_service.
        This decorator is not required::
            @fcm.failure_handler
            def handle_bad_ids(ids, *args):
                for device in Device.query.filter(id.in(ids)):
                    device.mark_as_inactive()
        """
        self._failure_handler = f
        return f

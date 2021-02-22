class AppError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.status_code = status_code
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        if payload:
            self.payload = payload

    def message(self):
        return self.message

    def code(self):
        return self.code

    def messages(self):
        return self.messages

    def format(self):
        obj = {'code': self.status_code or 500, 'message': self.message}
        if self.payload is not None:
            obj['messages'] = self.payload

        return obj

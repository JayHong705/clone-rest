from rest_framework.exceptions import APIException


class WootCustomError(Exception):
    """
    Woot Custom 에러 메세지
        - status_code:
        - message:
        - type:
        - field:
    """
    def __init__(self, status, message, type):
        self.status = status
        self.message = message
        self.type = type


class WootException(APIException):
    @staticmethod
    def bad_request(message="", code=None):
        raise WootCustomError(400, message, code)

    @staticmethod
    def unauthorized(message="", code=None):
        raise WootCustomError(401, message, code)

    @staticmethod
    def forbidden(message="", code=None):
        if not message:
            message = "접근 권한이 없습니다."
        raise WootCustomError(403, message, code)

    @staticmethod
    def not_found(message="", code=None):
        raise WootCustomError(404, message, code)
from rest_framework.response import Response


class CustomResponseMixin(object):
    """
    custom response 형식
        - status_code: 200 ~ 500 사이의 상태 코드
        - data: 모든 데이터를 담고 있는 object
    """
    def response(self, status_code, data=None):
        response_data = {
            data: {} if data is None else data
        }

        return Response(status=status_code, data=response_data)
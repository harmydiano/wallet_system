from ...utils.constants import OK


class AppResponse:
    @staticmethod
    def get_success_meta():
        return {'status_code': OK, 'success': True}

    @staticmethod
    def format(meta, data=None):
        response = dict()
        response['meta'] = meta
        if 'code' in meta:
            meta['status_code'] = meta['code']
            del meta['code']

        if data is not None:
            response['data'] = data
        return response


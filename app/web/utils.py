from typing import Any, Optional
from aiohttp.web_response import Response, json_response as aiohttp_json_response


def json_response(data: Any=None, status: str='ok') -> Response:
    if data is None:
        data = {}
    return aiohttp_json_response(data={
        'status': status, 'data': data
        })


def error_json_response(http_status: int, status: str='error', message: Optional[str]=None, 
                        data: Optional[dict]=None):
    if data is None:
        data = {}
    return aiohttp_json_response(status=http_status, data={
        'status': status, 'data': data, 'message': str(message)
        })

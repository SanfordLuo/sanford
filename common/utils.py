import time
import json
from django.http import JsonResponse


def get_current_timestamp():
    return int(time.time() * 1000)


def json_response(is_succ=False, data=None, total=None, message=None):
    """
    格式化输出
    :param is_succ:
    :param data:
    :param total:
    :param message:
    :return:
    """
    ret_dict = {
        'is_succ': is_succ
    }
    if data:
        ret_dict['data'] = data
    if total:
        ret_dict['total'] = total
    if message:
        ret_dict['message'] = message
    return JsonResponse(ret_dict)

from flask import Blueprint, request, jsonify
import log
import reprocess.discovery
mapping = Blueprint('discovery', __name__)

def error(exception, code=400):
    log.critical(str(exception))
    resp = {
        "message": str(exception),
        "code": code,
    }
    return jsonify(resp), code


def http_handler(func):
    def _handler(*args, **kwargs):
        try:
            ret = func(*args, **kwargs)
            return jsonify(ret)
        except Exception as ex:
            return error(ex)
    return _handler


@mapping.route("/discovery/<entity_id>", methods=['GET'])
@http_handler
def execute_reprocess_if_necessary(entity_id):
    # reference_date = request.headers.get('Reference-Date')
    # version = request.headers.get('Version')
    # branch = request.headers.get('Branch', 'master')


    return check()
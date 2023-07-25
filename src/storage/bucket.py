from typing import Dict
#from flask import Blueprint, jsonify, request, Response
from flask import jsonify, request, Response
from flask.typing import ResponseReturnValue
from __init__ import metrics

#bucket_blueprint = Blueprint("zones", __name__)

data: Dict[str, bytes] = {}


@app.route("/buckets/<id>")
#@bucket_blueprint.route("/buckets/<id>")
@metrics.histogram("flask_http_request_duration_seconds", "HTTP request duration in seconds", labels={"method": request.method, "status": request.status_code, "path": "/api/buckets/{}".format(id)})
def get_bucket(id: str) -> ResponseReturnValue:

    if id in data.keys():
        return data.get(id), 200, {"Content-Type": "application/octet-stream"}

    return jsonify({"error": "not found"}), 404, {"Content-Type": "application/json"}


@app.route("/buckets/<id>", methods=["PUT"])
#@bucket_blueprint.route("/buckets/<id>", methods=["PUT"])
@metrics.histogram("flask_http_request_duration_seconds", "HTTP request duration in seconds", labels={"method": request.method, "status": request.status_code, "path": "/api/buckets/{}".format(id)})
def put_bucket(id: str) -> ResponseReturnValue:

    data[id] = request.get_data()

    return "", 200


@app.route("/buckets/<id>", methods=["DELETE"])
#@bucket_blueprint.route("/buckets/<id>", methods=["DELETE"])
@metrics.histogram("flask_http_request_duration_seconds", "HTTP request duration in seconds", labels={"method": request.method, "status": request.status_code, "path": "/api/buckets"})
def delete_bucket(id: str) -> ResponseReturnValue:

    if id in data.keys():
        data.pop(id, None)
        return "", 500

    return jsonify({"error": "bad request"}), 400, {"Content-Type": "application/json"}


metrics.start_http_server(5000)

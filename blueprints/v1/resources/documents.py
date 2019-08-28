from flask import request, jsonify, make_response
from flask_restful import Resource
from ..modules.connection import RedisClient
from ..modules.verify import verifySignedData, verifySignedHeader
from hashlib import sha256

client = RedisClient().conn
    
class Documents(Resource):
    def get(self, pk, key):
        try:
            # check request
            if not client:
                raise BadRequest('Server unavailable', 404)

            # get data
            docKey = sha256((pk + key).encode('utf-8')).hexdigest()
            if not client.exists(docKey):
                raise BadRequest('Not found', 404)
            res = client.get(docKey)

            # response
            return make_response(jsonify(res.decode("utf-8")), 200)

        except BadRequest as e:
            return make_response(jsonify(message=e.message), e.status)
    
    def put(self, pk, key):
        try:
            # check request
            if not client:
                raise BadRequest('Server unavailable', 404)
            if not request.data:
                raise BadRequest('No body', 400)
            if not request.headers.get('Authorization'):
                raise BadRequest('No Authorization header', 400)

            # verify data
            data = verifySignedData(pk, request.json)
            authHeader = verifySignedHeader(pk, request.headers.get('Authorization'))
            if not data:
                raise BadRequest('Invalid data', 400)
            if not authHeader:
                raise BadRequest('Invalid Authorization header', 400)

            # set data
            docKey = sha256((pk + key).encode('utf-8')).hexdigest()
            res = client.set(docKey, request.json)

            # response
            return make_response(jsonify(message="succes"), 200)

        except BadRequest as e:
            return make_response(jsonify(message=e.message), e.status)
        except:
            return make_response(jsonify(message="Internal server error"), 500)

class BadRequest(Exception):
    """Custom exception class to be thrown when local error occurs."""
    def __init__(self, message, status=400, payload=None):
        self.message = message
        self.status = status
        self.payload = payload
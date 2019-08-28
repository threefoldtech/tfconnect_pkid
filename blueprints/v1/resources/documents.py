from flask import request, jsonify, make_response
from flask_restful import Resource
from ..modules.connection import RedisClient
from ..modules.verify import verifySignedData
from hashlib import sha256

client = RedisClient().conn

class Documents(Resource):
    def get(self, pk, key):
        try:
            docKey = sha256((pk + key).encode('utf-8')).hexdigest()
            if (client.exists(docKey)):
                res = client.get(docKey)
                return make_response(jsonify(res.decode("utf-8")), 200)
            else:
                return make_response(jsonify(message="Not found"), 404)
        except TypeError:
            return make_response(jsonify(message="Invalid json input"), 500)
        except:
            return make_response(jsonify(message="Internal server error"), 500)
    
    def put(self, pk, key):
        try:
            data = verifySignedData(pk, request.json)
            if data is not None:
                docKey = sha256((pk + key).encode('utf-8')).hexdigest()
                res = client.set(docKey, data)
                return make_response(jsonify(message="succes"), 200)
            else:
                raise ValueError
        except TypeError:
            return make_response(jsonify(message="Invalid input"), 400)
        except ValueError:
            return make_response(jsonify(message="Invalid"), 400)
        except:
            return make_response(jsonify(message="Internal server error"), 500)

import os
from flask import Flask

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    
    from blueprints.v1.api import api_bp as v1
    app.register_blueprint(v1, url_prefix='/v1')

    # from api.v2.api import api_bp as v2
    # app.register_blueprint(v2_, url_prefix='/v2')

    return app

if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
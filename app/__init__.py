from flask import Flask

def create_app(config_filename='../instance/config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)
    
    from .routes import main
    app.register_blueprint(main)
    
    return app

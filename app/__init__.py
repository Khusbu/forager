from flask import Flask
from flask_bootstrap import Bootstrap
from app import initializer


def create_app():
    app = Flask(__name__)

    def run_on_start():
        initializer.setup_data('data/finefoods.txt')
    run_on_start()
    return app


app = create_app()
bootstrap = Bootstrap(app)

from app import routes

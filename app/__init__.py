from flask import Flask
from flask_bootstrap import Bootstrap
from app import indexer


def create_app():
    app = Flask(__name__)

    def run_on_start():
        indexer.create_indexes_from_dataset('data/finefoods.txt')
    run_on_start()
    return app


app = create_app()
bootstrap = Bootstrap(app)

from app import routes

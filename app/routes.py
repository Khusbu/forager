from app import app
from store import cache


@app.route('/')
@app.route('/index')
def index():
    return str(len(cache.get('documents')))
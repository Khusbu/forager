from app import app
from flask import request

from app.parser import parse
from .retriever import retrieve_top_k_reviews
from flask import render_template


@app.route('/search')
def search():
    query_terms = parse(request.args.get('search'))
    top_k_reviews = retrieve_top_k_reviews(query_terms)
    return render_template('results.html', reviews=top_k_reviews, query_terms=query_terms)


@app.route('/')
def index():
    return render_template('input.html')

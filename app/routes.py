from app import app
from flask import request
from .retriever import retrieve_top_k_reviews
from flask import render_template


@app.route('/search')
def search():
    query_terms = request.args.get('search').split()
    top_k_reviews = retrieve_top_k_reviews(query_terms)
    return render_template('results.html', reviews=top_k_reviews, query_terms=query_terms)


@app.route('/')
def index():
    return render_template('input.html')

from app import app
from flask import request
from document_retriever import retrieve_documents
from scorer import get_top_k_documents


@app.route('/search')
def search():
    query_terms = request.args.get('search').split()
    documents = retrieve_documents(query_terms)
    top_k_documents = get_top_k_documents(query_terms, documents)
    return '\n\n'.join(top_k_documents)

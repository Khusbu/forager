from app import app
from flask import request
from document_retriever import retrieve_documents


@app.route('/search')
def search():
    return retrieve_documents(request.args.get('search'))
from store import cache


def retrieve_documents(query_term):
    document_indexes = cache.get('inverted_index').get(query_term)
    text = ''
    if document_indexes:
        for document_index in document_indexes:
            text += cache.get('documents').get(document_index)
            text += '\n\n'
    return text
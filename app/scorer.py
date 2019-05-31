import operator
from store import cache

K = 20


def score_documents(query_terms, documents):
    '''
    :param query_terms: list of query terms
    :param documents:
    :return: map of document to score
    '''
    return {document: score_document(query_terms, document) for document in documents}


def calculate_score(freq, total_query_terms):
    return float(freq)/total_query_terms


def score_document(query_terms, document):
    freq = 0
    document_indexes = cache.get('documents')
    for query_term in query_terms:
        if query_term in document_indexes.get(document):
            freq += 1
    return calculate_score(freq, len(query_terms))


def get_top_k_documents(query_terms, documents):
    document_to_score = score_documents(query_terms, documents)
    print('Document to score', document_to_score)
    sorted_document_to_score = sorted(document_to_score.items(), key=operator.itemgetter(1))[:K]
    return [cache.get('documents').get(document) for document, _ in sorted_document_to_score]




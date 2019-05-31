from store import cache


def retrieve_documents(query_terms):
    document_set = set()
    for query_term in query_terms:
        document_indexes = cache.get('inverted_index').get(query_term)
        if document_indexes:
            document_set = document_set.union(set(document_indexes))
    return list(document_set)


from .store import store


def retrieve_documents(query_terms):
    document_set = set()
    for query_term in query_terms:
        document_indexes = store.get_document_ids_by_word(query_term)
        if document_indexes:
            document_set = document_set.union(set(document_indexes))
    return list(document_set)


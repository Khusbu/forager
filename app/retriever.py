from app import scorer
from .store import store


def retrieve_reviews(query_terms):
    review_ids_set = set()
    for query_term in query_terms:
        review_ids_by_word = store.get_review_ids_by_word(query_term)
        if review_ids_by_word:
            review_ids_set = review_ids_set.union(set(review_ids_by_word))
    return [store.get_review_by_id(id) for id in list(review_ids_set)]


def retrieve_top_k_reviews(query_terms):
    reviews = retrieve_reviews(query_terms)
    return scorer.get_top_k_reviews(query_terms, reviews)

from .store import store


def create_inverted_index_for_reviews(review_indexes):
    '''
    :param review_indexes: dict of id_to_review
    :return: {
        <word>: <list_of_review_ids>,
        ...
    }
    '''
    review_inverted_indexes = {}
    for index, review in review_indexes.items():
        words = list(set(review.text.split()))
        for word in words:
            review_inverted_indexes[word] = review_inverted_indexes.get(word, [])
            review_inverted_indexes[word].append(index)
    return review_inverted_indexes


def create_index_for_reviews(reviews):
    '''
    :param reviews: Review objects
    :return: {
        <id>: <review_dict>,
        ...
    }
    '''
    review_indexes = {}
    for index, review in enumerate(reviews):
        if reviews:
            review_indexes.update({index+1: review})
    return review_indexes


def create_indexes(reviews):
    '''
    :param reviews: list of Review objects
    :return: None

    Create index and inverted index for reviews and store it in cache.
    '''
    review_indexes = create_index_for_reviews(reviews)
    store.add_reviews(review_indexes)
    review_inverted_indexes = create_inverted_index_for_reviews(review_indexes)
    store.add_word_to_review_ids(review_inverted_indexes)


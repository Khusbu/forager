K = 20


def score_reviews(query_terms, reviews):
    '''
    :param query_terms: list of query terms
    :param reviews:
    :return: map of review to score
    '''
    return {review: score_review(query_terms, review) for review in reviews}


def calculate_score(freq, total_query_terms):
    return float(freq)/total_query_terms


def score_review(query_terms, review):
    freq = 0
    for query_term in query_terms:
        if query_term in review.text:
            freq += 1
    return calculate_score(freq, len(query_terms))


def get_top_k_reviews(query_terms, reviews):
    review_to_score = score_reviews(query_terms, reviews)
    # sort by document score and then by review/score
    sorted_review_to_score = sorted(review_to_score.items(), key=lambda x: (-x[1], -float(x[0].score)))[:K]
    return [review for review, _ in sorted_review_to_score]




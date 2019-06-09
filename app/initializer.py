from app import indexer
from app.review import Review

TEXT_PRODUCT_ID = 'product/productId: '
TEXT_USER_ID = 'review/userId: '
TEXT_PROFILE_NAME = 'review/profileName: '
TEXT_HELPFULNESS = 'review/helpfulness: '
TEXT_SCORE = 'review/score: '
TEXT_TIME = 'review/time: '
TEXT_SUMMARY = 'review/summary: '
TEXT_TEXT = 'review/text: '


def _create_review_from_document(document):
    lines = document.split('\n')
    for line in lines:
        if line.startswith(TEXT_PRODUCT_ID):
            product_id = line.split(TEXT_PRODUCT_ID)[1]
        if line.startswith(TEXT_USER_ID):
            user_id = line.split(TEXT_USER_ID)[1]
        if line.startswith(TEXT_PROFILE_NAME):
            profile_name = line.split(TEXT_PROFILE_NAME)[1]
        if line.startswith(TEXT_HELPFULNESS):
            helpfulness = line.split(TEXT_HELPFULNESS)[1]
        if line.startswith(TEXT_SCORE):
            score = line.split(TEXT_SCORE)[1]
        if line.startswith(TEXT_TIME):
            time = line.split(TEXT_TIME)[1]
        if line.startswith(TEXT_SUMMARY):
            summary = line.split(TEXT_SUMMARY)[1]
        if line.startswith(TEXT_TEXT):
            text = line.split(TEXT_TEXT)[1]

    return Review(product_id, user_id, profile_name, helpfulness,
                  score, time, summary, text)


def _fetch_documents(filepath):
    '''
    :param filepath: path of the dataset
    :return: list of documents
    '''
    f = open(filepath, 'r')
    return f.read().split('\n\n')


def setup_data(filepath):
    documents = _fetch_documents(filepath)
    reviews = []
    for index, document in enumerate(documents):
        if document:
            reviews.append(_create_review_from_document(document))
    indexer.create_indexes(reviews)

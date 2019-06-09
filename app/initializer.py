from app import indexer
from app.review import Review


def _create_review_from_document(document):
    lines = document.split('\n')
    product_id = lines[0].split('product/productId: ')[1]
    user_id = lines[1].split('review/userId: ')[1]
    profile_name = lines[2].split('review/profileName: ')[1]
    helpfulness = lines[3].split('review/helpfulness: ')[1]
    score = lines[4].split('review/score: ')[1]
    time = lines[5].split('review/time: ')[1]
    summary = lines[6].split('review/summary: ')[1]
    text = lines[7].split('review/text: ')[1]

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

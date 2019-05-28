from store import cache


def retrieve_documents(filepath):
    '''
    :param filepath: path of the dataset
    :return: list of documents
    '''
    f = open(filepath, 'r')
    return f.read().split('\n\n')


def create_inverted_indexes(documents):
    return {}


def create_indexes_from_dataset(filepath):
    from app.store import cache
    '''
    :param filepath:
    :return:
    '''
    documents = retrieve_documents(filepath)
    documents_index = dict()
    for index, document in enumerate(documents):
        documents_index[index+1] = document
    cache.set('documents', documents_index)
    return documents


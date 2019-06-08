from .store import store


def create_documents_from_dataset(filepath):
    '''
    :param filepath: path of the dataset
    :return: list of documents
    '''
    f = open(filepath, 'r')
    return f.read().split('\n\n')


def _create_inverted_indexes():
    document_index = store.get_documents()
    word_to_document = {}
    for index, document in document_index.items():
        words = list(set(document.split()))
        for word in words:
            word_to_document[word] = word_to_document.get(word, [])
            word_to_document[word].append(index)
    store.add_word_to_document_ids(word_to_document)


def _create_document_indexes(documents):
    for document in documents:
        store.add_document(document)


def create_indexes_from_dataset(filepath):
    '''
    :param filepath:
    :return:
    '''
    documents = create_documents_from_dataset(filepath)
    _create_document_indexes(documents)
    _create_inverted_indexes()
    return documents


from werkzeug.contrib.cache import SimpleCache


class Store:
    class __Store:
        def __init__(self):
            '''
            Cache structure
            { 'documents': {
                  <id>: <document>
              },
              'word_to_document_ids': {
                  <word>: <list_of_document_ids>
              }
            }
            '''
            self.cache = SimpleCache()

        def get_documents(self):
            return self.cache.get('documents') or {}

        def get_document_by_id(self, id):
            return self.get_documents().get(id)

        def get_word_to_document_ids(self):
            return self.cache.get('word_to_document_ids') or {}

        def get_document_ids_by_word(self, word):
            return self.get_word_to_document_ids().get(word)

        def add_document(self, document):
            documents = self.get_documents()
            total_documents = len(documents)
            documents.update({
                total_documents + 1: document
            })
            self.cache.set('documents', documents)

        def add_word_to_document_ids(self, data):
            word_to_document_ids = self.get_word_to_document_ids()
            word_to_document_ids.update(data)
            self.cache.set('word_to_document_ids', word_to_document_ids)

    instance = None

    def __new__(cls):  # __new__ always a classmethod
        if not Store.instance:
            Store.instance = Store.__Store()
        return Store.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)


store = Store()
from werkzeug.contrib.cache import SimpleCache


class Store:
    class __Store:
        def __init__(self):
            '''
            Cache structure
            { 'reviews': {
                  <id>: <review>
              },
              'word_to_review_ids': {
                  <word>: <list_of_review_ids>
              }
            }
            '''
            self.cache = SimpleCache()

        def get_reviews(self):
            return self.cache.get('reviews') or {}

        def get_review_by_id(self, id):
            return self.get_reviews().get(id)

        def get_word_to_review_ids(self):
            return self.cache.get('word_to_review_ids') or {}

        def get_review_ids_by_word(self, word):
            return self.get_word_to_review_ids().get(word)

        def add_reviews(self, reviews):
            self.cache.set('reviews', reviews)

        def add_word_to_review_ids(self, word_to_review_ids):
            self.cache.set('word_to_review_ids', word_to_review_ids)

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
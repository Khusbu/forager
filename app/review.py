class Review:
    def __init__(self, product_id, user_id, profile_name, helpfulness,
                 score, time, summary, text):
        self.product_id = product_id
        self.user_id = user_id
        self.profile_name = profile_name
        self.helpfulness = helpfulness
        self.score = score
        self.time = time
        self.summary = summary
        self.text = text

    def to_dict(self):
        return self.__dict__

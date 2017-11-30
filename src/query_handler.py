class QueryHandler:

    def __init__(self, query_file, vector_rep):
        self.__load_query(query_file)
        self.vector_rep = vector_rep
        self.and_list = []
        self.not_list = []

    # def generate_file(self, answer_file):

    def __load_query(self, query_file):
        try:
            file = open(query_file, 'r')
            raw_query = file.read().replace('\n', ' ')
            self.__parse(raw_query)
        except IOError:
            raise IOError

    def __parse(self, raw_query):
        words = raw_query.split(' ')
        for word in words:
            if word.startswith('-'):
                self.not_list.append(word)
            else:
                self.and_list.append(word)



class QueryHandler:

    def __init__(self, query_file, vector_rep, index_representation):
        self.and_list = []
        self.not_list = []
        self.index_representation = index_representation
        self.__load_query(query_file)
        self.vector_rep = vector_rep
        self.matched = []

    def generate_file(self, answer_file):
        for filename, vec_rep in self.vector_rep.items():
            if len(set.intersection(set(vec_rep), set(self.and_list))) != len(self.and_list):
                continue

            if len(set.intersection(set(vec_rep), set(self.not_list))) > 0:
                continue

            self.matched.append(filename)

        self.__write_output_file(answer_file)

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
            if word.startswith('-') and word.strip('-') in self.index_representation:
                self.not_list.append(self.index_representation[word.strip('-')])
            elif word in self.index_representation:
                self.and_list.append(self.index_representation[word])

    def __write_output_file(self, answer_file):
        try:
            file = open(answer_file, 'w+')
            file.write("%s\n" % len(self.matched))
            for file_matched in self.matched:
                file.write("%s\n" % file_matched)
            file.close()
        except IOError:
            raise IOError


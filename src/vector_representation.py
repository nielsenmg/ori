from collections import OrderedDict
import os


class VectorRepresentation:

    def __init__(self, docs_paths_file, index_file):
        self.docs_paths_file = docs_paths_file
        self.index_file = index_file
        self.docs_paths = []
        self.index_representation = {}
        self.vector_representation = OrderedDict()

    def generate_file(self, vector_file):
        vector_rep = self.get_representation()
        self.__write_output_file(vector_rep, vector_file)

    def get_representation(self):
        if len(self.vector_representation) > 0:
            return self.vector_representation

        self.__load_documents_path()
        self.__load_index()

        for document_file in self.docs_paths:
            self.__create_vector_representation(document_file)

        return self.vector_representation

    def get_index_representation(self):
        if len(self.index_representation) > 0:
            return self.index_representation

        self.__load_index()
        return self.index_representation

    def __load_documents_path(self):
        try:
            file = open(self.docs_paths_file, 'r')
            self.docs_paths = file.read().split('\n')
            file.close()
        except IOError:
            raise IOError

    def __load_index(self):
        try:
            file = open(self.index_file, 'r')
            lines = file.read().split('\n')
            for line in lines:
                word, position = line.split(':')[0], len(self.index_representation) + 1
                if len(word) > 0:
                    self.index_representation[word] = position
            file.close()
        except IOError:
            raise IOError

    def __create_vector_representation(self, document_file):
        try:
            _, current_file = os.path.split(document_file)
            file = open(document_file, 'r')
            words = file.read().replace('\n', ' ').replace(',', ' ').replace('.', ' ').replace('!', ' ')\
                .replace('?', ' ').split(' ')
            file_vector = []
            for word in words:
                if word in self.index_representation:
                    file_vector.append(self.index_representation[word])

            self.vector_representation[current_file] = file_vector

        except IOError:
            raise IOError

    def __write_output_file(self, vector_representation, output_file):
        try:
            file = open(output_file, 'w+')
            for key, value in vector_representation.items():
                file.write(' '.join(str(e) for e in value))
                file.write("\n")
            file.close()
        except IOError:
            raise IOError


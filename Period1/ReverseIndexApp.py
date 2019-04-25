from ReverseIndex import ReverseIndex 
import time


class ReverseIndexApp():
    def __init__(self, file_name):
        self.__filename = file_name

    def run(self):
        m_rev_index = ReverseIndex()
        m_rev_index.make_rev_index()
        m_rev_index.write_index(self.__filename)


if __name__ == '__main__':
    start_time = time.process_time()
    re_index_app = ReverseIndexApp('RevIndex.txt')
    re_index_app.run()
    print(time.process_time() - start_time)

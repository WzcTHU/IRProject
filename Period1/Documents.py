import re
class Documents():
    def __init__(self, file_name):
        self.__filename = file_name
        self.__docu_str = ''
        self.words_list = []
    
    def __open_file(self):
        with open(self.__filename, 'r', encoding='utf-8') as document_file:
            for each in document_file.readlines():
                self.__docu_str += each

    def split_docu(self):
        self.__open_file()
        self.__docu_str = re.sub(r'\d+\s+\d+\s+\d+', ' ', self.__docu_str)
        self.__docu_str = re.sub(r'\n', ' ', self.__docu_str)    
        temp_list = re.split(r'\s+|,|\.+|[\n]+|\t+|<pre>|<html>|</pre>|</html>', self.__docu_str)
        for each in temp_list:
            if (len(each) != 0):
                self.words_list.append(each.lower())
        # print(self.words_list)

if __name__ == '__main__':
    test_doc = Documents('./cacm/CACM-0001.html')
    test_doc.split_docu()
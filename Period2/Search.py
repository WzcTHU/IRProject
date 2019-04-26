import json 
import os

class Search():
    def __init__(self):
        self.total_doc = 3204
        self.target_words_list = []
        self.RevIndexDic = {}
        self.doc_list = []

    def GetAllDoc(self, dirname='/Period1/cacm'):
        # last_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        cur = os.getcwd()
        temp_list = os.listdir(cur + dirname)
        for each in temp_list:
            self.doc_list.append(each[5:9])
        return self.doc_list
    
    def GetInput(self):
        print('Please input words or sentence to search in database: ')
        print('(Enter q to stop enter and begin search)')
        temp_list = []
        while(1):
            word = input()
            if(word == 'q'):
                break
            else:
                temp_list.extend(word.split(' '))
                # self.target_words_list.extend(word.split(' '))
        for each in temp_list:
            if(each.lower() not in self.target_words_list):
                self.target_words_list.append(each.lower())
        return self.target_words_list
        
    def LoadRevIndex(self):
        with open('RevIndex.txt', 'r') as json_file:
            self.RevIndexDic = json.load(json_file)
        return self.RevIndexDic

    

    
    
if __name__ == '__main__':
    m_s = Search()
    # li = m_s.GetInput()
    # dic = m_s.LoadRevIndex()
    # print(li)
    m_s.GetAllDoc()
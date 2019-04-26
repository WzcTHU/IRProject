import json

class Search():
    def __init__(self):
        self.total_doc = 3204
        self.target_words_list = []
        self.RevIndexDic = {}
    
    def GetInput(self):
        print('Please input words or sentence to search in database: ')
        print('(Enter q to stop enter and begin search)')
        while(1):
            word = input()
            if(word == 'q'):
                break
            else:
                self.target_words_list.extend(word.split(' '))
        
    def LoadRevIndex(self):
        with open('RevIndex.txt', 'r') as json_file:
            self.RevIndexDic = json.load(json_file)
    

class Search():
    def __init__(self):
        self.target_words_list = []
    
    def GetInput(self):
        print('Please input words or sentence to search in database: ')
        print('(Enter q to stop enter and begin search)')
        while(1):
            word = input()
            if(word == 'q'):
                break
            else:
                self.target_words_list.extend(word.split(' '))
        

import json 
import os

class Search():
    def __init__(self):
        self.total_doc_num = 3204
        self.target_words_list = []
        self.rev_index_dic = {}
        self.doc_list = []                  # 存储所有文档名称的列表
        self.sim_dic = {}                   
        self.all_words_list = []           # 存储所有词的列表
        self.words_r_dic = {}               # 存储每个单词的r值
        self.words_p_dic = {}               # 存储每个单词的p值


    def GetAllDoc(self, dirname=r'\\Period1\\cacm'):
        last_dir = os.path.abspath(os.path.dirname(os.getcwd()))
        # cur = os.getcwd()
        temp_list = os.listdir(last_dir + dirname)
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
            self.rev_index_dic = json.load(json_file)
        self.all_words_list = list(self.rev_index_dic.keys())
        # print(list(self.rev_index_dic.keys()))
        return self.rev_index_dic

    def CalPR1st(self):
        self.LoadRevIndex()
        self.GetAllDoc()
        for word in self.all_words_list:
            self.words_p_dic[word] = 0.5        # 使用初始P值
            self.words_r_dic[word] = len(self.rev_index_dic[word]['files']) / self.total_doc_num
        return self.words_p_dic, self.words_r_dic

    
if __name__ == '__main__':
    m_s = Search()
    _, rd = m_s.CalPR1st()
    print(rd['language'])
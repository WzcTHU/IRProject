import json 
import os
import math as m
from SpellCorrect import SpellCorrect

class Search():
    def __init__(self):
        self.N = 3204
        self.V = 200
        self.target_words_list = []
        self.rev_index_dic = {}
        self.doc_list = []                  # 存储所有文档名称的列表
        self.sim_dic = {}                   
        self.words_r_dic = {}               # 存储每个单词的r值
        self.words_p_dic = {}               # 存储每个单词的p值
        self.result_list = []

    def __GetAllDoc(self, dirname=r'\\cacm'):
        # last_dir = os.path.abspath(os.path.dirname(os.getcwd()))
        temp_list = os.listdir(os.getcwd() + dirname)
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
        for each in temp_list:
            if(each.lower() not in self.target_words_list):
                self.target_words_list.append(each.lower())
        
        # 进行拼写检查并纠正
        m_corrector = SpellCorrect()
        temp_list = []
        for each in self.target_words_list:
            temp_list.append(m_corrector.correct(each))
        self.target_words_list.extend(temp_list)
        self.target_words_list = list(set(self.target_words_list))      # 去重
        return self.target_words_list
        
    def __LoadRevIndex(self):
        with open('RevIndex.txt', 'r') as json_file:
            self.rev_index_dic = json.load(json_file)
        return self.rev_index_dic

    def CalPR1st(self):
        self.__LoadRevIndex()
        self.__GetAllDoc()
        for word in self.target_words_list:
            if word in self.rev_index_dic.keys():
                self.words_p_dic[word] = 0.5        # 使用初始P值
                self.words_r_dic[word] = len(self.rev_index_dic[word]['files']) / self.N
        return self.words_p_dic, self.words_r_dic

    def CalSim(self):
        '''使用初始P值第一次计算相似度，并找出相似度较高的文档'''
    
        for each_doc in self.doc_list:
            self.sim_dic[each_doc] = 0
            for each_word in self.target_words_list:
                if each_word in self.rev_index_dic.keys():      # 该索引词在词库中才进行计算
                    if(each_doc in self.rev_index_dic[each_word]['files'].keys()):  # 文档含有该词
                        pi = self.words_p_dic[each_word]
                        ri = self.words_r_dic[each_word]
                        self.sim_dic[each_doc] += m.log10((pi / (1 - pi)) * ((1 - ri) / ri))
            self.sim_dic[each_doc] = abs(self.sim_dic[each_doc])
        # 挑选50个相似度最高的文档
        self.result_list = sorted(self.sim_dic.items(), key=lambda x:x[1], reverse=True)
        return self.result_list

    def CalPR2nd(self):
        top_doc_list = self.result_list
        for word in self.target_words_list:
            if word in self.rev_index_dic.keys():
                Vi = 0
                ni = len(self.rev_index_dic[word]['files'])
                for each_doc in top_doc_list:           # 计算该word出现在几个被选中的文档中
                    if(each_doc in self.rev_index_dic[word]['files'].keys()):
                        Vi += 1
                pi = (Vi + (ni / self.N)) / (self.V + 1)
                self.words_p_dic[word] = pi
                ri = (ni - Vi + (ni / self.V)) / (self.N - self.V + 1)
                self.words_r_dic[word] = ri
        return self.words_p_dic, self.words_r_dic

    def ShowResult(self, show_num=10):
        print('The result of search: ')
        for each_doc in self.result_list[0:show_num]:
            print('CACM-' + each_doc[0] + '.html', 'Similarity: ' + str(each_doc[1]))


if __name__ == '__main__':
    m_s = Search()
    m_s.GetInput()
    m_s.CalPR1st()
    m_s.CalSim()

    print(m_s.result_list)
    m_s.CalPR2nd()
    m_s.CalSim()
    print(m_s.result_list)
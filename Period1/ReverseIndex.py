import sys 
import os
from Documents import Documents
import json


class ReverseIndex():
    def __init__(self):
        self.__stop_words = frozenset([
            'a', 'about', 'above', 'above', 'across', 'after', 'afterwards', 'again',
            'against', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although',
            'always', 'am', 'among', 'amongst', 'amoungst', 'amount', 'an', 'and', 'another',
            'any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere', 'are', 'around', 'as',
            'at', 'back', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been',
            'before', 'beforehand', 'behind', 'being', 'below', 'beside', 'besides',
            'between', 'beyond', 'bill', 'both', 'bottom', 'but', 'by', 'call', 'can',
            'cannot', 'cant', 'co', 'con', 'could', 'couldnt', 'cry', 'de', 'describe',
            'detail', 'do', 'done', 'down', 'due', 'during', 'each', 'eg', 'eight',
            'either', 'eleven', 'else', 'elsewhere', 'empty', 'enough', 'etc', 'even',
            'ever', 'every', 'everyone', 'everything', 'everywhere', 'except', 'few',
            'fifteen', 'fify', 'fill', 'find', 'fire', 'first', 'five', 'for', 'former',
            'formerly', 'forty', 'found', 'four', 'from', 'front', 'full', 'further', 'get',
            'give', 'go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her', 'here',
            'hereafter', 'hereby', 'herein', 'hereupon', 'hers', 'herself', 'him',
            'himself', 'his', 'how', 'however', 'hundred', 'ie', 'if', 'in', 'inc',
            'indeed', 'interest', 'into', 'is', 'it', 'its', 'itself', 'keep', 'last',
            'latter', 'latterly', 'least', 'less', 'ltd', 'made', 'many', 'may', 'me',
            'meanwhile', 'might', 'mill', 'mine', 'more', 'moreover', 'most', 'mostly',
            'move', 'much', 'must', 'my', 'myself', 'name', 'namely', 'neither', 'never',
            'nevertheless', 'next', 'nine', 'no', 'nobody', 'none', 'noone', 'nor', 'not',
            'nothing', 'now', 'nowhere', 'of', 'off', 'often', 'on', 'once', 'one', 'only',
            'onto', 'or', 'other', 'others', 'otherwise', 'our', 'ours', 'ourselves', 'out',
            'over', 'own', 'part', 'per', 'perhaps', 'please', 'put', 'rather', 're', 'same',
            'see', 'seem', 'seemed', 'seeming', 'seems', 'serious', 'several', 'she',
            'should', 'show', 'side', 'since', 'sincere', 'six', 'sixty', 'so', 'some',
            'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhere',
            'still', 'such', 'system', 'take', 'ten', 'than', 'that', 'the', 'their',
            'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby',
            'therefore', 'therein', 'thereupon', 'these', 'they', 'thickv', 'thin', 'third',
            'this', 'those', 'though', 'three', 'through', 'throughout', 'thru', 'thus',
            'to', 'together', 'too', 'top', 'toward', 'towards', 'twelve', 'twenty', 'two',
            'un', 'under', 'until', 'up', 'upon', 'us', 'very', 'via', 'was', 'we', 'well',
            'were', 'what', 'whatever', 'when', 'whence', 'whenever', 'where', 'whereafter',
            'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which',
            'while', 'whither', 'who', 'whoever', 'whole', 'whom', 'whose', 'why', 'will',
            'with', 'within', 'without', 'would', 'yet', 'you', 'your', 'yours', 'yourself',
            'yourselves', 'the', 'cacm'])
        self.rev_index = {}
        self.__stop_dic = {}
        self.__file_list = []

    def __make_stop_dic(self):
        for each in self.__stop_words:
            self.__stop_dic[each] = -1
        # print(self.__stop_dic)
    
    def __walk_dir(self):
        cur_dir = os.getcwd()
        self.__file_list = os.listdir(cur_dir + r'\\cacm')
        # print(self.__file_list)
    
    def make_rev_index(self):
        self.__make_stop_dic()
        self.__walk_dir()
        for i in range(0, len(self.__file_list)):
            m_doc = Documents('cacm/' + self.__file_list[i])
            m_doc.split_docu()
            for each_term in m_doc.words_list:
                if(each_term not in self.__stop_dic.keys()):
                    if(each_term not in self.rev_index):
                        self.rev_index[each_term] = \
                            {'total_num': 1, 'files': {self.__file_list[i][5:9]: 1}}
                        self.rev_index[each_term]['total_num'] += 1
                        if(self.__file_list[i][5:9] in self.rev_index[each_term]['files']):
                            self.rev_index[each_term]['files'][self.__file_list[i][5:9]] += 1
                        else:
                            self.rev_index[each_term]['files'][self.__file_list[i][5:9]] = 1
        # print(self.rev_index['computer'])

    def write_index(self, file_name):
        f_w = open(file_name, 'w')
        f_w.write(json.dumps(self.rev_index, indent=1))
        f_w.close()
        
if __name__ == '__main__':
    test_rev = ReverseIndex()
    test_rev.make_rev_index()

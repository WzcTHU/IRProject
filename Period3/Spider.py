# -*-coding:utf-8 -*-
import requests
import re
from lxml import etree
from FlushPrint import FlushPrint
import time
import json

class Spider:
    def __init__(self, deep_n=3):
        self.deep_n = deep_n
        self.result_dict = {}           # to store the result: {'url': title}
    def WriteUrlFile(self, url_list, filename):
        with open(filename, 'w') as tar_file:
            for each_url in url_list:
                each_url = each_url.replace("'", '') + '\n'
                tar_file.write(each_url)


    def OpenUrl(self, url):
        try:
            response = requests.get(url, timeout=1)
            response.encoding = response.apparent_encoding
            html = response.text
            return html
        except:
            return 'URL unable to open'

    def AnalysisHtml(self, html):
        sub_urls_processed = []
        ban_suffix = ['.png', '.jpg', '.bmp', '.css']
        regex = r'(?<=<a href=\").*?(?=\")|(?<=href=\').*?(?=\')'
        sub_urls = re.findall(regex, html)
        for each in sub_urls:
            try:
                if(each[-4:] not in ban_suffix):
                    if(each[0] == '/'):
                        each = 'http://www.tsinghua.edu.cn' + each
                    if(each not in self.result_dict.keys()):
                        if((('tsinghua' in each) | ('thu' in each)) & ('http' in each)):
                            sub_urls_processed.append(each)
                sub_urls_processed = list(set(sub_urls_processed))          # delete same urls
            except:
                return []
        return sub_urls_processed
    
    def GetTitle(self, url, html):
        try:
            page = etree.HTML(html)
            if(url[0:26] == 'http://www.tsinghua.edu.cn'):
                title = page.xpath('//h1/text()')
            else:
                title = page.xpath('/html/head/title/text()')
            title = re.findall(r'.*', title[0])
            return title[0]
        except:
            return ''

    def BFS(self, url_list):
        i_n = 0
        while(i_n < self.deep_n):
            filename = 'URLLayer_' + str(i_n) + '.txt'
            print('Grabing layer ', i_n, ', ', len(url_list), ' urls in total')
            self.WriteUrlFile(url_list, filename)
            total_url_num = len(url_list)
            count = 0
            temp_url_list = []
            for each_url in url_list:
                if(each_url not in self.result_dict.keys()):
                    each_html = self.OpenUrl(each_url)
                    each_title = self.GetTitle(each_url, each_html)
                    if(each_title != ''):
                        self.result_dict[each_url] = each_title
                    each_url_list = self.AnalysisHtml(each_html)
                    temp_url_list.extend(each_url_list)
                count += 1
                text = 'Process: Layer ' + str(i_n) + '  ------------- ' + str(round(100 * count / total_url_num, 2)) + '%' 
            
                FlushPrint(text)
            url_list = list(set(temp_url_list))
            i_n += 1
            self.WriteResults()

        return self.result_dict

    def WriteResults(self, filename='SpiderResult.txt'):
        with open(filename, 'w', encoding='utf-8') as f_w:
            f_w.write(json.dumps(self.result_dict, ensure_ascii=False, indent=1))

if __name__ == '__main__':
    m_sp = Spider()
    url = 'http://www.tsinghua.edu.cn/publish/thu2018/index.html'
    html = m_sp.OpenUrl(url)
    suburl = m_sp.AnalysisHtml(html)
    dic = m_sp.BFS(suburl)
    # print(len(dic))
    # print(len(suburl))

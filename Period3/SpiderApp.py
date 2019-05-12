from Spider import *

class SpiderApp:
    def __init__(self):
        self.spider = Spider()

    def Run(self, url='http://www.tsinghua.edu.cn/publish/thu2018/index.html'):
        html = self.spider.OpenUrl(url)
        suburl = self.spider.AnalysisHtml(html)
        dic = self.spider.BFS(suburl)
        print('Grabing finished, ' + len(dic) + ' results in total')

if __name__ == '__main__':
    m_app = SpiderApp()
    m_app.Run()
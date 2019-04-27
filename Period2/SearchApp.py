from Search import Search
import time

class SearchApp:
    def run(self):
        m_search = Search()
        m_search.GetInput()
        # start_time = time.process_time()
        m_search.CalPR1st()
        m_search.CalSim()
        m_search.CalPR2nd()
        m_search.CalSim()
        # print(time.process_time() - start_time)
        m_search.ShowResult()

if __name__ == '__main__':
    m_search_app = SearchApp()
    m_search_app.run()
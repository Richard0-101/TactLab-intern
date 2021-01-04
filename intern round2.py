import requests
from bs4 import BeautifulSoup
urls=["  https://www.youtube.com/watch?v=fRh_vgS2dFE " , "https://www.youtube.com/watch?v=k2qgadSvNyU"]
for url in urls:
    def scrape_info(url):
        r = BeautifulSoup(requests.get(url).text, "html.parser")
        viewsd=r.select_one('meta[itemprop="interactionCount"][content]')['content']
        viewss=r.select_one('meta[itemprop="interactionCount"][content]')['content']
        data_viewsd={viewsd}
        data_viewss={viewss}
        return data_viewss
    if __name__=="__main__":
        data_views = scrape_info(url)
        print(data_views)
    
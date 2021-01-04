import requests
from bs4 import BeautifulSoup
urls=["  https://www.youtube.com/watch?v=fRh_vgS2dFE " , "https://www.youtube.com/watch?v=k2qgadSvNyU"]
for url in urls:
    def scrape_info(url):
        r = BeautifulSoup(requests.get(url).text, "html.parser")#prints the data
        viewsd=r.select_one('meta[itemprop="interactionCount"][content]')['content']
        viewss=r.select_one('meta[itemprop="interactionCount"][content]')['content']
        data_viewsd={viewsd}
        data_viewss={viewss}
        
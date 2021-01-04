import requests
from bs4 import BeautifulSoup
urls=["https://www.youtube.com/watch?v=fRh_vgS2dFE"]
for url in urls:
    def scrape_info(url):
        r = BeautifulSoup(requests.get(url).text, "html.parser")#prints the data
        views=r.select_one('meta[itemprop="interactionCount"][content]')['content']
        data_views={views}
        return data_views
    if __name__=="__main__":
        data_views = scrape_info(url)
        print(data_views)
    
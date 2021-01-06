import json
import requests
import influxdb
from influxdb import InfluxDBClient
from datetime import datetime
from bs4 import BeautifulSoup
urls=["  https://www.youtube.com/watch?v=fRh_vgS2dFE " , "https://www.youtube.com/watch?v=k2qgadSvNyU"]
for url in urls:
    def scrape_info(url):
        r = BeautifulSoup(requests.get(url).text, "html.parser")
        title1=r.select_one('meta[itemprop="name"][content]')['content']
        views1=r.select_one('meta[itemprop="interactionCount"][content]')['content']
        data1={'title':title1, 'views':views1}
        
        client = InfluxDBClient('localhost', 8086, 'root', 'root', 'songcompare')
        

        json_body = [
            {
                "measurement":"data",
                






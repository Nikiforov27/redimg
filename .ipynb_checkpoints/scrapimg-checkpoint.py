#!/usr/bin/python
import re
import os

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def scrap(url: str):
    user_agent = UserAgent()
    headers = {"User-Agent": user_agent.random}

    full_page = requests.get(url, headers=headers)
    soup = BeautifulSoup(full_page.content, 'lxml')
    #convert = soup.find_all("div", {"class": "loaded"})
    

   # for i in soup:
    #    img_url = soup.get("img")
     # #  return data_url
    #return soup

   # with open("tag_soup.txt", "w") as tag_file:
    #    tag_file.write(str(soup))
     #   return "yee"

print(scrap("https://www.reddit.com/search/?q=qtile"))

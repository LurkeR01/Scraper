import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

url = 'https://animego.org/anime/season/2023/spring'

# options = webdriver.ChromeOptions()
# options.headless = True
# driver = webdriver.Chrome(service=ChromeService(
#     ChromeDriverManager().install()))
#
# driver.get(url)
#
# last_height = driver.execute_script('return document.body.scrollHeight')
#
# itemTargetCount = 5
# try:
#     while True:
#         driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
#
#         time.sleep(1)
#
#         new_height = driver.execute_script('return document.body.scrollHeight')
#
#         if new_height == last_height:
#             break
#
#         last_height = new_height
#
#         with open('source-page.html', 'w', encoding='utf-8') as file:
#             file.write(driver.page_source)
# except Exception as _ex:
#     print(_ex)

with open('source-page.html', 'r', encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
row = soup.find_all('div', class_='col-12')
anime_names_list = dict()

for i in range(len(row) - 1):
    anime = row[i]
    anime_name = anime.find('div', class_='h5 font-weight-normal mb-1')
    anime_rating = anime.find('div', class_='p-rate-flag__text')
    if anime_rating is not None:
        if anime_rating.text[0] == "9":
            anime_names_list[anime_name.text] = anime_rating.text

with open('anime_names_list.txt', 'w') as file:
    file.write('Топ аниме этого сезона:\n')
    for key, value in anime_names_list.items():
        file.write(key + ': ' + value + '\n')
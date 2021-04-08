import requests
from bs4 import BeautifulSoup

# 상영작 리스트 가져오기
# movie_url = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
# movie_list = BeautifulSoup(movie_url.text, "html.parser").select('.tit3 > a')
# for movie in movie_list:
#     print(movie.text)

# Genie 차트 가져오기(headers 정보를 요청하는 사이트)
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# genie_url = requests.get('https://www.genie.co.kr/chart/top200', headers = headers)
# song_list = BeautifulSoup(genie_url.text, 'html.parser').select('#body-content > div.newest-list > div > table > tbody > tr')
# for song in song_list:
#     rank = song.select_one('td.number').text[0:2].strip()
#     title = song.select_one('td.info > a.title.ellipsis').text.strip()
#     artist = song.select_one('td.info > a.artist.ellipsis').text
#     print(rank, title, artist)

# naver 증권 인기검색
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
stock_url = requests.get('https://finance.naver.com/sise/lastsearch2.nhn', headers = headers)
stock_list = BeautifulSoup(stock_url.text, 'lxml').select('#contentarea > div.box_type_l > table > tr')
for stock in stock_list:
    rank = stock.select_one('td.no')
    company = stock.select_one('td > a')
    price = stock.select_one('td:nth-of-type(4)') # 4번째 td 요소 선택(nth-of-type)
    rate = stock.select_one('td:nth-of-type(6)') 
    if rank and company and price and rate:
        print(rank.text, company.text, price.text, rate.text.strip())


import requests, sys
import codecs

#search_word = sys.argv[1] # api_params = {'titles'} 콘솔에서 실행시 검색어 입력
search_word = input("검색어를 입력하세요. >>>  ")
api_url = 'https://en.wikipedia.org/w/api.php'
api_params = {'format':'xmlfm', 'action':'query', 'prop':'revisions', 'rvprop':'content' }
api_params['titles'] = search_word
wiki_data = requests.get(api_url, params=api_params)

# 검색 결과를 'request_result.html'로 출력
result = codecs.open(search_word + '.html', 'w', 'utf-8')
result.write(wiki_data.text)
result.close()



# # 웹브라우저 열기
# import webbrowser
# url = 'https://en.wikipedia.org/w/api.php'
# webbrowser.open(url)
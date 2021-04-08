import requests, pprint

# 기상청 RSS로 xml 데이터 수집
url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp'
payload = {'zone' : '4117355000'}
weather_data = requests.get(url, payload).text
# pprint.pprint(weather_data)

# xml.etree.ElementTree 모듈을 사용해서 xml 자료 가공 : 시간, 온도, 날씨 정보만 출력
import xml.etree.ElementTree as ET
xml_data = ET.fromstring(weather_data)
print("안양시 동안구 오늘의 날씨")
for tag in xml_data.iter("data"):
    print(tag.find('hour').text + "시")
    print(f"온도 {tag.find('temp').text}, 날씨 {tag.find('wfKor').text}")
import requests
import json

def get_masknum():
    servicekey = "5v6MONBHXlp5NB4c9ODMCB0an4DkBsIbrOk5e9O45h7z1MnuuO0X9YRj44GYHGYtbMzzMGC3zn+Hhzxk1Sfhzg=="
    url = 'http://apis.data.go.kr/B552584/ArpltnStatsSvc/getCtprvnMesureLIst'
    pm10_params ={'serviceKey' : servicekey, 'returnType' : 'json', 'numOfRows' : '100', 'pageNo' : '1', 'itemCode' : 'PM10', 'dataGubun' : 'HOUR', 'searchCondition' : 'MONTH' }

    pm10_response = requests.get(url, params=pm10_params).content
    pm10_result = json.loads(pm10_response)

    print(pm10_result['response']['body']['items'][0])
    pm10_incheon = pm10_result['response']['body']['items'][0]['incheon']
    pm10_gyeonggi = pm10_result['response']['body']['items'][0]['gyeonggi']
    pm10_avg = (int(pm10_incheon) + int(pm10_gyeonggi)) / 2
    print(f"미세먼지 인천 : {pm10_incheon}, 경기 : {pm10_gyeonggi}, 평균 : {pm10_avg}")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    pm25_params ={'serviceKey' : servicekey, 'returnType' : 'json', 'numOfRows' : '100', 'pageNo' : '1', 'itemCode' : 'PM25', 'dataGubun' : 'HOUR', 'searchCondition' : 'MONTH' }
    pm25_response = requests.get(url, params=pm25_params).content
    pm25_result = json.loads(pm25_response)
    pm25_incheon = pm25_result['response']['body']['items'][0]['incheon']
    pm25_gyeonggi = pm25_result['response']['body']['items'][0]['gyeonggi']
    pm25_avg = (int(pm25_incheon) + int(pm25_gyeonggi)) / 2
    print(f"초미세먼지 인천 : {pm25_incheon}, 경기 : {pm25_gyeonggi}, 평균 : {pm25_avg}")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # 미세먼지 기준 : 0 ~ 30 ==> 좋음(1단계) / 31 ~ 80 ==> 보통(2단계) / 81 ~ 150 ==> 나쁨(3단계) / 151이상 ==> 매우나쁨(4단계)
    # 초미세먼지 기준 : 0 ~ 15 ==> 좋음(1단계) / 16 ~ 35 ==> 보통(2단계) / 36 ~ 75 ==> 나쁨(3단계) / 76이상 ==> 매우나쁨(4단계)
    for n, pm10_sd in enumerate([30, 80, 150,float('inf')],start=1):
        if pm10_avg <= pm10_sd:
            pm10_n = n
            break
    for n, pm25_sd in enumerate([15, 35, 75,float('inf')],start=1):
        if pm25_avg <= pm25_sd:
            pm25_n = n
            break

    return pm10_avg, pm25_avg
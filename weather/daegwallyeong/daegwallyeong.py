# -*- coding: utf-8 -*-

import pandas as pd

file = open('대관령.txt', 'r')
read = file.read()
split = read.split()

def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

list_chunked = list_chunk(split, 56)
print(list_chunked)

df = pd.DataFrame(list_chunked)
print(df)

df.columns = ['관측일', '국내 지점번호', '일 평균 풍속', '일 풍정', '최대풍향', '최대풍속', '최대풍속 시각', '최대순간풍향', '최대순간풍속', '최대순간풍속 시각', '일 평균기온', '최고기온', '최고기온 시각', '최저기온', '최저기온 시각', '일 평균 이슬점온도', '일 평균 지면온도', '일 최저 초상온도', '일 평균 상대습도', '최저습도', '최저습도 시각', '일 평균 수증기압', '소형 증발량', '대형 증발량', '안개계속시간', '일 평균 현지기압', '일 평균 해면기압', '최고 해면기압', '최고 해면기압 시각', '최저 해면기압', '최저 해면기압 시각', '일 평균 전운량', '일조합', '가조시간', '캄벨 일조', '일사합', '최대 1시간일사', '최대 1시간일사 시각', '일 강수량', '9-9 강수량', '강수계속시간', '1시간 최다강수량', '1시간 최다강수량 시각', '10분간 최다강수량', '10분간 최다강수량 시각', '최대 강우강도', '최대 강우강도 시각', '최심 신적설', '최심 신적설 시각', '최심 적설', '최심 적설 시각', '0.5m 지중온도', '1.0m 지중온도', '1.5m 지중온도', '3.0m 지중온도', '5.0m 지중온도']

df1 = df[['관측일', '국내 지점번호', '일 평균기온', '최고기온', '최저기온', '일 평균 전운량', '일조합', '일 강수량']]
print(df1)

df1.to_csv('대관령.csv')

file.close()
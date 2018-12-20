import random
import requests
import json

url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
res = requests.get(url).text
lotto_dict = json.loads(res)
bonus = lotto_dict["bnusNo"]
week_format_num = []

for i in range(1,7):
    num = lotto_dict["drwtNo{}".format(i)]
    week_format_num.append(num)

    

def pickLotto():
    num_list = range(1,46)
    pick = random.sample(num_list,6)
    matched = len(set(pick) & set(week_format_num))
    
    if matched == 6:
        print("1등입니다.")
    elif matched == 5:
        if bonus in pick:
            print("2등입니다.")
        else:
            print("3등입니다.")
    elif matched == 4:
        print("4등입니다.")
    
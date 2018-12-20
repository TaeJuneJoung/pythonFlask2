from flask import Flask, render_template, request
import random
import requests
import json
from faker import Faker

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
    return "hello"

@app.route("/lotto")
def lotto():

    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
    res = requests.get(url).text
    data = json.loads(res,encoding="UTF-8")
    
    count = 0
    
    # print(data)
    # print(type(data))
    # print(data["drwNoDate"])
    
    # print(data["drwtNo1"])
    
    result = [data["drwtNo1"],data["drwtNo2"],data["drwtNo3"],data["drwtNo4"],data["drwtNo5"],data["drwtNo6"]]
    bouns = data["bnusNo"]
    result.sort()
    
    lotto_num_list = range(1,46)
    pick = random.sample(lotto_num_list,6)
    pick.sort()
    
    winningNumber = list()
    isBouns = False
    
    
    for i in pick:
        for j in result:
            if(i==j):
                winningNumber.append(i)
                count += 1
            if(i==bouns):
                isBouns = True
            
    
    if(count==6):
        checking = str(winningNumber)+str(count)+"개가 일치합니다. 1등입니다"
    elif(count==5 and isBouns):
        checking = str(winningNumber)+str(count)+"개가 일치합니다. 2등입니다"
    elif(count==5):
        checking = str(winningNumber)+str(count)+"개가 일치합니다. 3등입니다"
    elif(count==4):
        checking = str(winningNumber)+str(count)+"개가 일치합니다. 4등입니다"
    elif(count==3):
        checking = str(winningNumber)+str(count)+"개가 일치합니다. 5등입니다"
    else:
        checking = str(winningNumber)+str(count)+"개가 일치합니다. 아쉽지만, 다음에..."

    return render_template("lotto.html",lotto = pick, result = result, check = checking)

      
      
@app.route('/lotto.do')
def lotto_do():

    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
    res = requests.get(url).text
    lotto_dict = json.loads(res)

    week_num = []
    week_format_num = []
    drwtNo = ["drwtNo1","drwtNo2","drwtNo3","drwtNo4","drwtNo5","drwtNo6"]
    for num in drwtNo:
        number = lotto_dict[num]
        week_num.append(number)
        
    for i in range(1,7):
        num = lotto_dict["drwtNo{}".format(i)]
        week_format_num.append(num)
    
    # pick = 우리가 생성한 번호
    # week_num = 이번주 당첨번호 
    # 위의 두 값을 비교해서 로또 당첨 등수 출력!!!
    # sorted()
    # 1등 : 6개의 숫자를 다 맞출때
    # 2등 : 5개의 숫자 + 보너스 번호
    # 3등 : 5개의 숫자
    # 4등 : 4개의 숫자
    # 5등 : 3개
    
    # print(type(res))
    # print(type(json.loads(res)))
    
    num_list = range(1,46)
    pick = random.sample(num_list,6)
    pick.sort()
    
    pick_set = set(pick)
    week_format_num_set = set(week_format_num)
    pick_inse = pick_set.intersection(week_format_num)#intersection을 쓰지 않고 &을 사용할 수 있다.
    # | -> 합집합 효과
    
    pick_inse = sorted(pick_inse)
    
    bonus = [lotto_dict["bnusNo"]]
    
    pick_bnus = pick_set.intersection(bonus)
    
    pick_len = len(pick_inse)
    
    
    
    if(pick_len==6):
        result = "1등입니다"
    elif(pick_len==5 and len(pick_bnus)==1):
        result = "2등입니다"
    elif(pick_len==5):
        result = "3등입니다"
    elif(pick_len==4):
        result = "4등입니다"
    elif(pick_len==3):
        result = "5등입니다"
    else:
        result = "아쉽지만 다음기회에..."
    
    
    return render_template("lotto_do.html",lotto = pick, week_format_num = week_format_num, intersectionNumber = pick_inse,resultString=result)
    

@app.route("/ping")
def ping():
    return render_template("ping.html")
    
@app.route("/pong")
def pong():
    input_name = request.args.get('name')
    fake = Faker('ko_KR')#한국어 출력
    fake_job = fake.job()
    number = random.randrange(1,6)
    return render_template("pong.html", html_name = input_name, user_job = fake_job, data = number)
import random

phonebook = {
    "one" : "010-0000-0001",
    "two" : "010-0000-0002"
}
print(phonebook["two"])


twice = {
    "다현" : 21,
    "사나" : 22,
    "지효" : 23,
    "쯔위" : 22,
    "모모" : 22
}

winner = {
    "강승윤" :20,
    "송민호":21,
    "김진우":22,
    "이승훈":23
}

idol = {
    "twice":twice,
    "winner":winner
}

#print(idol)
print(idol["twice"]["다현"])

score = {
    "국어" : 70,
    "수학" : 50,
    "영어" : 100
}

for key, value in score.items():
    #print(key,value)
    pass

for value in score.keys():
    #print(score[value])
    pass
    
sumNum = 0
count = 0
for key,value in score.items():
    sumNum += value
    count += 1
    avgValue = sumNum/count
    print(avgValue)
    
    
ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scrapying": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "gj1":  {
            "lecturer": "ChangE",
            "manager": "pro1",
            "class president": "서희수",
            "groups": {
                "두드림": ["구종민", "김녹형", "윤은솔", "이준원", "이창훈"],
                "런치타임": ["문영국", "박나원","박희승", "서희수", "황인식"],
                "Friday": ["강민지", "박현진", "서상준", "안현상", "최진호"],
                "TMM": ["김훈", "송건희", "이지선", "정태준", "조호근"],
                "살핌": ["문동식", "이중봉", "이지희", "차상권", "최보균"]
            }
        },
        "gj2": {
            "lecturer": "teacher2",
            "manager": "pro2"
        },
        "gj3": {
            "lecturer": "teacher3",
            "manager": "pro3"
        }
    }
}

"""
# 1. ssafy를 진행하는 지역(location)은 몇개 인가요?
# 2. python standard library 'requests'가 있나요??
# 3. gj1반의 반장의 이름을 출력하세요
# 4. ssafy에서 배우는 언어들을 출력하세요 : dictionary.keys활용
# 5. ssafy gj2의 강사와 매니저의 이름을 출력하세요
    # 예시) teacher2
    #       pro2
# 6. framework들의 이름과 설명을 다음과 같이 출력하세요
    # 예시) 
    # flask는 micro이다.
    # django는 full-functioning이다.
# 7. 오늘 당번을 뽑기 위해 '살핌'조원중 1명을 랜덤으로 뽑아주세요
    # 예시)
    # 오늘 당번은 문동식입니다.
"""
print("----------")
#1번
print(len(ssafy["location"]))
#2번
data = ssafy["language"]["python"]["python standard library"]
if "requests" in data:
    print("True")
else:
    print("False")
#3번
data = ssafy["classes"]["gj1"]["class president"]
print(data)

#4번
data = ssafy["language"].keys()
for i in data:
    print(i)

#5번
data = ssafy["classes"]["gj2"].values()
print(data)
#for i in data:
#    print(i)

#6번
data = ssafy["language"]["python"]["frameworks"].items()
for key, value in data:
    print(key+"는 "+value+"이다.")
    
#7번
data = ssafy["classes"]["gj1"]["groups"]["살핌"]
result = random.choice(data)
print(type(result))
print("오늘 당번은 "+result+"입니다.")
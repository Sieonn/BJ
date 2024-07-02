# 삼성전자 = 50000
# print(삼성전자*10)

# 시가총액=2980000000000
# 현재가=50000
# PER=15.79
# print(시가총액,type(시가총액))
# print(현재가,type(현재가))
# print(PER,type(PER))

# s="hello"
# t="python"
# print(s,"!",t)

# print(2+2*3)

# a="123"
# print(type(a))

# num_str="720"
# print(int(num_str), type(int(num_str)))

# num=100
# print(str(num), type(str(num)))

# str = "15.79"
# print(float(str))

# year="2020"
# year = int(year)
# print(year,year-1,year-2)

# ac = 48584
# print("총금액: ",ac*36)
# letters = 'python'
# print(letters[0], letters[2])
# license_plate = "24가 2210"
# print(license_plate[-4:])
# string ="홀짝홀짝홀짝"
# print(string[::2])

# str =  "PYTHON"
# print(str[::-1])

# phone = "010-1111-2222"
# phone=phone.replace("-","")
# print(phone)

# url="http://sharebook.kr"
# url1 = url.split(".") #리스트
# print(url1[-1])

# lang = 'python'
# lang[0] = 'P' #문자열을 수정할 수 없다.
# print(lang)

# string = 'abcdfe2a354a32a'
# str = string.replace("a","A")
# print(str)
# str = "-"
# print(str*80)

# t1="python"
# t2 = "java"
# t3 = t1+" "+t2+" "
# print(t3*4)
# name1 = '김민수'
# age1 = 10
# name2 = '이철희'
# age2 = 13
# print("이름: %s 나이: %d"%(name1, age1))
# print("이름: %s 나이: %d"%(name2, age2))

# print("이름:{} 나이:{}".format(name1, age1))
# print("이름:{} 나이:{}".format(name2, age2))
# print(f"이름:{name1} 나이:{age1}")
# print(f"이름:{name2} 나이:{age2}")

# 상장주식수 = "5,969,782,550"
# result = int(상장주식수.replace(",",""))
# print(result, type(result))

# 분기 = "2020/03(E) (IFRS연결)"
# print(분기[:7])
# data = "      삼성전자      "
# data= data.strip()
# print(data)

# ticker = "btc_krw"
# ticker = ticker.upper()
# print(ticker)
# ticker = "btc_krw"
# ticker = ticker.lower()
# print(ticker)

# str = "hello"
# str = str.capitalize()
# print(str)

# file_name = "보고서.xlsx"
# print(file_name.endswith(".xlsx" or".xls"))

# f = "2020_보고서.xlsx"
# print(f.startswith("2020"))

# a = "hello world"
# a =  a.split(" ")
# print(a)

# ticker = "btc_krw"
# ticker = ticker.split("_")
# print(ticker)
# date = "2020-05-01"
# date = date.split("-")
# print(date)

data = "039490 "
data = data.rstrip()
print(data)
temp = input('请输入一个年份：')

while not temp.isdigit():
    temp = input('你输入的数字有误')

year = int(temp)
if  year/400 == int(year/400):
    print(temp + '是闰年')
else:
    if (year/4 == int(year/4)) and (year/100 != int(year/100)):
        print(temp + '是闰年')
    else:
        print(temp + '不是闰年')

    

# game.py
import random

print('*' * 30)
print('欢迎进入赌场')
print('*' * 30)

username = input('请输入顾客名')
money = 0
answer = input("确实能够进入游戏吗")

if answer == 'y' or 'Y':
    while money < 2:
        n = int(input('请充值（100的倍数）'))
        if n % 100 == 0 and n > 0:
            money = (n // 100) * 10
    print('当前金币剩余：', money)
    print('进入游戏....')

    while True:
        money -= 2
        t1 = random.randint(1, 6)
        t2 = random.randint(1, 6)

        print('洗牌完毕')
        guess = input('请输入大小')

        if ((t1 + t2) > 6 and guess == '大') or ((t1 + t2) <= 6 and guess == '小'):
            print('恭喜{}，猜对了，获得一个游戏币'.format(username))
            money += 1
        else:
            print('很遗憾游戏结束')
        print('现在金币剩余：%d' % money)
        answer = input('是否继续')
        if (answer != 'y' or 'Y') and money < 2:
            print('退出游戏！')
            break

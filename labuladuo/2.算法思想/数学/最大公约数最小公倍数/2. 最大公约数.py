"""
最小公倍数为两数的乘积除以最大公约数。
"""


def gcd(a:int ,b:int):
    return a if b ==0 else gcd(b,a%b)

def lcd(a:int,b:int):
    return a*b/gcd(a,b)

if __name__ == '__main__':
    a = 2000
    b = 24
    print(lcd(a,b))
"""
204. Count Primes (Easy)
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        notPrimes = [False]*(n+1)
        count = 0
        for i in range(2,n):
            if notPrimes[i]:
                continue
            count +=1
            for j in range(i*i,n,i):
                notPrimes[j] = True
        return count


if __name__ == '__main__':
    n = 20
    print(Solution().countPrimes(n))

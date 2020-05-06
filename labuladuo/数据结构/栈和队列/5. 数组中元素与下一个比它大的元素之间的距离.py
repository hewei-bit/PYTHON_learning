"""
739. Daily Temperatures (Medium)
根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。
如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，
你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。
每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。


"""


class Solution:
    def dailyTemperatures(self, T: list) -> list:
        l = len(T)
        stack = []  # 这里定义一个栈就不用说了
        res = [0] * l  # 这里是最后要返回的result，因为题目中说没有匹配的就返回0，
        # 所以这里初始化一个全是0的list，然后把那些有匹配的替换掉即可。

        for idx, t in enumerate(T):  # 下面是关键
            while stack and t > T[stack[-1]]:  # 当stack为空时，运行stack.append(idx)，则stack=[0]
                # 然后仅当遍历元素 t 小于stack顶端的值时append进去，
                # 这会导致stack中idx代表的元素是单调递减的，
                # 如果此时遍历到一个 t，大于stack顶端的值，那这个t就是离stack
                # 顶端值最近的那个大值。
                res[stack.pop()] = idx - stack[-1]  # 然后pop出来，还是要注意stack.pop出来的是idx，这样res这
                # 一串0里对应位置的0就会被替换成应有的值。
                # 再进入while循环判断t和stack.pop后的新的顶端值哪个大。
                # 如此反复。
            stack.append(idx)
        return res


T = [73, 74, 75, 71, 69, 72, 76, 73]
obj = Solution().daliyTemperature(T)
print(obj)

"""
93. Restore IP Addresses(Medium)


给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
"""
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        track = ""
        self.backtrack(0, 4, res, track, s)
        return res

    def backtrack(self, count: int, flag: int, res: List[str], track: str, s: str):
        if flag == 0 and len(s) == count:
            res.append(track[:-1])
            return
        if flag < 0:
            return
        for i in range(count, count + 3):
            if i < len(s):
                if i == count and s[i] == "0":
                    self.backtrack(i + 1, flag - 1, res, track + s[i] + ".", s)
                    break
                if 0 < int(s[count:i + 1]) <= 255:
                    self.backtrack(i + 1, flag - 1, res, track + s[count:i + 1] + ".", s)

if __name__ == '__main__':
    s = "25525511135"
    obj = Solution().restoreIpAddresses(s)
    print(obj)
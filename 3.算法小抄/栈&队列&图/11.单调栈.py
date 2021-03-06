# vector<int> nextGreaterElement(vector<int>& nums) {
#     vector<int> ans(nums.size()); //
#     stack<int> s;
#     for (int i = nums.size() - 1; i >= 0; i--) { // 倒着往栈里放
#         while (!s.empty() && s.top() <= nums[i]) { // 判定个子高矮
#             s.pop(); // 矮个起开，反正也被挡着了。。。
#         }
#         ans[i] = s.empty() ? -1 : s.top(); // 这个元素身后的第一个高个
#         s.push(nums[i]); // 进队，接受之后的身高判定吧！
#     }
#     return ans;
# }


def nextGreaterElement(nums: list):
    ans = [0] * len(nums)  # 存放答案的数组
    stack = []
    for i in range(len(nums), -1, -1):
        while stack and stack[-1] < nums[i]:
            stack.pop()
        ans[i] = 0 if stack is None else stack[-1]
        stack.append(nums[i])
    return ans

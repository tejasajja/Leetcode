class Solution(object):
    def jump(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\
        # max_index = 0
        # for i in range(len(nums)):
        #     if i > max_index:
        #         break
        #     max_index = max(max_index, i + nums[i])
        #     while j
        # return True
        n = len(nums)
        if n ==1:
            return 0
        cur = 0
        jump= 0
        maxReach = 0
        maxReachidx = 0

        for i in range(n):
            if (cur + nums[cur] >= n-1):
                return jump+1
            if i > cur + nums[cur] :
                cur =  maxReachidx
                jump+=1
            reach = i+nums[i]
            if reach>maxReach:
                maxReach = reach
                maxReachidx = i
        return jump+1


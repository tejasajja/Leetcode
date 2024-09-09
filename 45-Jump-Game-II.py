class Solution(object):
    def jump(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\
        # n = len(nums)
        # if n ==1:
        #     return 0
        # cur = 0
        # jump= 0
        # maxReach = 0
        # maxReachidx = 0

        # for i in range(n):
        #     if (cur + nums[cur] >= n-1):
        #         return jump+1
        #     if i > cur + nums[cur] :
        #         cur =  maxReachidx
        #         jump+=1
        #     reach = i+nums[i]
        #     if reach>maxReach:
        #         maxReach = reach
        #         maxReachidx = i
        # return jump+1
        res =0 
        l = r =0
        while r < len(nums)-1:
            farthest = 0 
            for i in range(l,r +1):
                farthest = max(farthest, i + nums[i])
            l = r+1
            r = farthest
            res +=1
        return res

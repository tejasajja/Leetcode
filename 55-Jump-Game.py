class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_index = 0
        # Iterate through each
        # index of the array
        for i in range(len(nums)):
            # If the current index is greater
            # than the maximum reachable index
            # it means we cannot move forward
            # and should return false
            if i > max_index:
                return False

            # Update the maximum index
            # that can be reached by comparing
            # the current max_index with the sum of
            # the current index and the
            # maximum jump from that index
            max_index = max(max_index, i + nums[i])

        # If we complete the loop,
        # it means we can reach the
        # last index
        return True

        
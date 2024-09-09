class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        min_n = {min(rows) for rows in matrix}
        max_n = {max(columns) for columns in zip(*matrix)} 
        
        return list(min_n & max_n)
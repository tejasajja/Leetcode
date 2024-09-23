class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # res =[]
        # stack =[]

        # def backtrack (openN, closedN):
        #     if openN == closedN ==n:
        #         res.append(''.join(stack))
        #         return 

        #     if openN < n:
        #         stack.append('(')
        #         backtrack(openN + 1,closedN)
        #         stack.pop()

        #     if closedN < openN:
        #         stack.append(')')
        #         backtrack(openN,closedN + 1)
        #         stack.pop()

        # backtrack(0,0)
        # return res
        com = []
        def backtracking(o,c, path):
            if o > n or c >n or o < c:
                return 
            if o ==n and c == n:
                com.append(path)
                return
            backtracking(o +1 , c , path+'(')
            backtracking(o , c +1  ,path+')')

        backtracking(0,0,'')
        return com
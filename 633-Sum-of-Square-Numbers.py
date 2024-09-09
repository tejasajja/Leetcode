
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        # sqroot= set()


        # for i in range(int(sqrt(c))+1):
        #     sqroot.add(i*i)

        # a =0 
        # while a*a <=c:
        #     target = c- a*a
        #     if target in sqroot:
        #         return True
        #     a+=1
        # return False

        left, right = 0 , int(sqrt(c))

        while left <= right:
            total = left * left +right *right

            if total > c:
                right -=1
            elif total <c:
                left +=1

            else:
                return True
        return False



                

        
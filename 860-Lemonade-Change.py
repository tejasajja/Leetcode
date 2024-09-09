class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = 0 
    
        # Initialize a counter
        # for $10 bills
        ten = 0   
        
        # Iterate through each customer's bill
        for bill in bills:
            
            # If the customer's
            # bill is $5
            if bill == 5:
                
                # Increment the
                # count of $5 bills
                five += 1  
            
            # If the customer's
            # bill is $10
            elif bill == 10:
                
                # Check if there are $5
                # bills available to give change
                if five:
                    # Use one $5 bill
                    # to give change
                    five -= 1 
                    # Receive one $10 bill
                    ten += 1   
                
                # If no $5 bill
                # available, return false
                else:
                    return False  
            
            # If the customer's
            # bill is $20
            else:
                # Check if there are both
                # $5 and $10 bills
                # available to give change
                if five and ten:
                    # Use one $5 bill
                    five -= 1 
                    # Use one $10 bill
                    ten -= 1   
                
                # If there are not enough $10 bills,
                # check if there are at least
                # three $5 bills available
                elif five >= 3:
                    # Use three $5 bills
                    # to give change
                    five -= 3  
                
                # If unable to give
                # change, return false
                else:
                    return False  
        
        # Return true if all customers
        # are served with correct change
        return True 
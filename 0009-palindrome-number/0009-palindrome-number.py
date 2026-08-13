class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            print("Not Palindrome")
        
        return str(x) == str(x)[::-1]
        
            
        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filter: keep only alphanumeric characters and lowercase them
        cleaned = "".join(char.lower() for char in s if char.isalnum())
        
        # Directly return the boolean comparison
        return cleaned == cleaned[::-1]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr=""
        for i in s[::-1]:
            if i.isalnum():
                newstr+=i.lower()

        if newstr==newstr[::-1]:
            return True
        return False

        
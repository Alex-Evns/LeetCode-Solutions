class Solution(object):

    def isPalindrome(self, x):
        int_string = str(x)

        reversed_int = int_string[::-1]

        if(int_string == reversed_int):
            return True
        else:
            return False

    def isPalindromeInt(self, x):
        original = x
        reversed_num = 0

        if x < 0:
            return False

        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit 
            x //=10

        if original == reversed_num:
            return True
        else:
            return False

        

        
class Solution(object):

    def isPalindrome(self, x):
        int_string = str(x)

        reversed_int = int_string[::-1]

        if(int_string == reversed_int):
            return True
        else:
            return False
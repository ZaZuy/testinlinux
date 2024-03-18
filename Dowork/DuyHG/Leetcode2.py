class Leetcode2():
    def isPalindrome(self, x):
        if type(x) == int:
            copyx = x
            if x // 10 == 0 or x < 0:
                return False
            n = 0
            while x != 0:
                n = n * 10 + x % 10
                x = x // 10
            return n == copyx
        else:
            print("Please enter a numbers")
Leetcode2 = Leetcode2()
print("Palindrome Number: ",Leetcode2.isPalindrome(121))
class Leetcode5():
    def reverseParentheses(self, s):
        stack = []
        i = 0
        getstr = ""
        while s[i] != ")":
            getstr = getstr + s[i]
            if s[i] == "(":
                stack.append(getstr.replace("(", ""))
                getstr = ""
            if s[i + 1] == ")":
                stack.append(getstr)
                while len(stack) != 2:
                    result = stack.pop()[::-1]
                    result = stack.pop() + result
                    stack.append(result)
                str = stack.pop()
                dem = i
                while dem < len(s):
                    getstr = getstr + s[dem]
                    if s[dem] == ")":
                        if getstr != "":
                            result = (str + getstr.replace(")", ""))[::-1]
                        getstr = ""
                    dem = dem + 1
            i = i + 1
        return result
Leetcode5 = Leetcode5()
print("Reverse Substrings Between Each Pair of Parentheses: ",Leetcode5.reverseParentheses("(ed(et(oc))el)"))
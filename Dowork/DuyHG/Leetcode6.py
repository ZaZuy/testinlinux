import math
class Leetcode6():
    def pathInZigZagTree(self):
        label_int_str = input("Please enter an integer: ")
        label = int(label_int_str)
        if label > 1:
            way = []
            way.append(label)
            while label > 1:
                Row = int(math.log2(label))
                maxRow = 2 ** Row
                y = (label - maxRow)
                p = (label - (y + y / 2) - 1)
                label = p
                way.append(math.ceil(p))
        else:
            print("Invalid number, please enter a number greater than 0: ")
        return way[::-1]
        # result = ""
        # for i in range(len(s) - 1, -1, -1):
        #     if ord(s[i]) >= 48 and ord(s[i]) <= 122:
        #         result= result + s[i]
        # return stack
Leetcode6 = Leetcode6()
print("Path In Zigzag Labelled Binary Tree: ",Leetcode6.pathInZigZagTree())
class Leetcode3():
    def findLonely(self, arr):
        # result = []
        # pos = 0
        # x = 0
        # for i in range(1, len(arr)):
        #     x = arr[i]
        #     pos = i
        #     while pos > 0 and x < arr[pos -1]:
        #         arr[pos] = arr[pos-1]
        #         pos = pos - 1
        #     arr[pos] = x
        # for z in range(0, len(arr)-1):
        #     if()
        result = []
        dictionary = {}
        for value in arr:
            if value not in dictionary:
                dictionary[value] = 1
            else:
                dictionary[value] += 1

        for key, value in dictionary.items():
            if value == 1:
                if key + 1 not in dictionary.keys():
                    result.append(key)
        return result
Leetcode3 = Leetcode3()
try:
    print("Find All Lonely Numbers in the Array: ",Leetcode3.findLonely([7,6,8,8,10,10,12]))
except:
    print("Wrong! You probably entered an array as a character or a special character.")
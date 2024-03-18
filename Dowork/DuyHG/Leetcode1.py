class Leetcode1():
    #Do phuc tap O(n)
    def twoSum(self, nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
    # Bài học: sử dụng từ điển băm sẽ giảm độ phức tạp của thuật toán nhược điểm chỉ băm các số khác nhau
    #Do phuc tap O(n^2)
    # def twoSum(self, nums, target):
    #     stores = []
    #     numtest = nums.copy()
    #     for n in range(0, len(nums)):
    #         x = target - nums[n]
    #         numtest.pop(0)
    #         if n != nums.__len__() and x in numtest:
    #             print("[", n, ",", n + numtest.index(x) + 1, "]")
    #             break
Leetcode1 = Leetcode1()
try:
    print("Two Sum : ", Leetcode1.twoSum([2, 7, 11, 15], 9))
except:
    print("Please enter numbers")
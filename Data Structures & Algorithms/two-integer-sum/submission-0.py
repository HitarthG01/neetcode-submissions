class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        
        for i, num in enumerate(nums):
            look_for = target - num
            
            if look_for in my_dict:
                return [my_dict[look_for], i]
                
            my_dict[num] = i
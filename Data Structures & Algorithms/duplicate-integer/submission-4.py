class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    
        counter_dict={}

        for num in nums:
            counter_dict[num]=counter_dict.get(num,0)+1
            if counter_dict[num]>1:
                return True
        
        return False
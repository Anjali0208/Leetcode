class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ltemp = 0
        temp1 = 0

        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in nums:
                temp1 = nums.index(temp)
                if(i!=temp1):
                    return i, temp1
            

        
                
        
        
        

                
    

        
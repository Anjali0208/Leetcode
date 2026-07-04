class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        read = 0
        write = 0
        temp = 0

        for i in range(len(nums)):
            if nums[read] == 0 and nums[write] !=0:
                temp = nums[read]
                nums[read] = nums[write]
                nums[write] = temp
                read+=1
                write+=1
            elif nums[read]!=0 and nums[write]!=0:
                write+=1
                read+=1
            else:
                write+=1
                
        return nums
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index, value in enumerate(nums):
            
            if value in dict:
                return [dict[value],index]			#Return index of the matched key and the current index
            else:
                dict[target - value] = index		#Store difference along with index
				
----------------------------------------------------------------------------------------------------------------				
# Here we are maintaining a dictionary in which we store..
#	key => Remaining value 
#	value  => index of the value

# For example our nums = [2,7,1,4,6,8,3,5,5,4]
# target = 9
# Solution:
# 	How much we add in 2 so that we will reached our target => 9-2 = 7
#   So we store 7 as remainning  and 0 as index => [dict[value],index]  => 7:0
	Similarly for 2nd element => 9-7 = 2  =>  2:1
	
#  Finally our dict will be like => {7:0, 2:1, 8:3, .... } => {Remaining, Index}

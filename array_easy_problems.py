#The cumulative sum of an array at index i is defined as the sum of all elements of the array from index 0 to index i.
from typing import List
class Solution:
	def getCumulativeSum(self, arr: List[int]) -> List[int]:
		# add your logic here
		if len(arr) <= 1 :
			return arr
		else :
			for i in range(1,len(arr)):
				arr[i]=arr[i-1]+arr[i]
			return arr

arr=[1,2,3,4,5]
testcase=Solution()
print(testcase.getCumulativeSum(arr))

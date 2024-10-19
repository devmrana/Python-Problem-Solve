def findFirstAndLast(arr, n, x):
    first = -1
    last = -1
    for i in range(0, n):
        if (x != arr[i]):
            continue
        if (first == -1):
            first = i
        last = i
 
    if (first != -1):
        print("First Occurrence = ", first," \nLast Occurrence = ", last)
    else:
        print("Not Found")

# Driver code
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
n = len(arr)
x = 2
findFirstAndLast(arr, n, x)
print('------------------------')
class Solution(object):
   def searchRange(self, nums, target):
      res = [-1,-1]
      low = 0
      high = len(nums)
      while low<high:
         mid = int(low + (high-low)//2)
         if nums[mid] == target:
            high = mid
            res[0]=mid
            res[1]=mid
         elif nums[mid]<target:
            low = mid+1
         else:
            high = mid
      if res[0] == -1:
         return res
      low = res[0]+1
      high = len(nums)
      while low<high:
         mid = int(low + (high-low)//2)
         if nums[mid] == target:
            low = mid+1
            res[1] = mid
         elif nums[mid] < target:
            low = mid + 1
         else:
            high = mid
      return res
ob1 = Solution()
print(ob1.searchRange([2,2,2,3,3,4,4,4,4,5,5,6], 4))
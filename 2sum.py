def twoSum(nums, target):
   seen = set()
   results = []
   
   for i in range(len(nums)):
     curr = []
     temp = target - nums[i]
     if (temp in seen):
        curr.append(temp)
        curr.append(nums[i])

     seen.add(nums[i])

     if (len(curr) > 0):
        results.append(curr)
  
   print(results)
   return results


nums = [1, 2, 3, 4, 5]
print(twoSum(nums,6))

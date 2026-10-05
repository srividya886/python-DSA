arr=[2,1,5,1,3,2,8,1,3]
k=3
def max_sum_subarray(arr,k):
  window_sum=sum(arr[:k])
  max_sum=window_sum
  for i in range(k,len(arr)):
    window_sum=window_sum-arr[i-k]+arr[i]
    max_sum=max(max_sum,window_sum)
  return max_sumarr=[2,1,5,1,3,2,8,1,3]
k=3
def max_sum_subarray(arr,k):
  window_sum=sum(arr[:k])
  max_sum=window_sum
  for i in range(k,len(arr)):
    window_sum=window_sum-arr[i-k]+arr[i]
    max_sum=max(max_sum,window_sum)
  return max_sum
a=max_sum_subarray(arr,k)
print(a)  
a=max_sum_subarray(arr,k)
print(a)  
a=[2,7,11,12]
target=18
def two_pointers(a, target):
    left,right=0,len(a)-1
    while left < right:
        s = a[left] +a[right]
        if s == target:
            return[left,right]
        elif s < target:
            left +=1
        else:
            right -=1
        return []   
print(two_pointers(a,target)) 
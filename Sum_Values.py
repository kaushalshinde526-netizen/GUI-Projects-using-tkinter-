#find out pairs with given sum values of an array
#arr=[5,7,4,3,9,8,19,21] value-arry=3+11 =14<17
def two_sum(arr,sum):
    arr.sort()
    left=0
    right=len(arr)-1
    while left<right:
        if(arr[left]+arr[right]>sum):
            right=right-1
        elif(arr[left]+arr[right]<sum):
            left=left+1
        else:
            print("Pair found:", arr[left], arr[right])
            left=left+1
            right=right-1
arr=[5,7,4,3,9,8,19,21]
sum=17
two_sum(arr,sum)
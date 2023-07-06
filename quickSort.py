class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if(low<high):
            pivotIndex=self.partition(arr,low,high)
            self.quickSort(arr,low,pivotIndex-1)
            self.quickSort(arr,pivotIndex+1,high)
    def partition(self,arr,low,high):
        # code here
        i=low-1
        pivot=arr[high]
        
        for j in range(low,high):
            if(arr[j]<=pivot):
                i+=1
                arr[i],arr[j]=arr[j],arr[i]
        
        i+=1
        arr[i],arr[high]=arr[high],arr[i]
        return i

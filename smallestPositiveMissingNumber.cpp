class Solution
{
    public:
    int checkPresent(int arr[],int n,int num){
        for(int i=0;i<n;i++){
            if(arr[i]==num){
                return 1;
            }
        }
        return 0;
    }
    //Function to find the smallest positive number missing from the array.
    int missingNumber(int arr[], int n) 
    { 
        int max_num=-1;
        for(int i=0;i<n;i++){
            if(arr[i]>max_num){
                max_num=arr[i];
            }
        }
        if(max_num<=0){
            return 1;
        }
        for(int i=1;i<=max_num;i++){
            if(checkPresent(arr,n,i)==0){
                return i;
            }
        }
        return max_num+1;
    } 
};
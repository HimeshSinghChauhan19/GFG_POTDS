class Solution{
public:

	void pushZerosToEnd(int arr[], int n) {
	    // code here
	    int k=0;
        for(int i=0;i<n;i++){
            if(arr[i]!=0){
                swap(arr[i],arr[k++]);
            }
        }	    
	}
};
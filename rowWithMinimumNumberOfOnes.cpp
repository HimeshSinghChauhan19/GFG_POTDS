class Solution {
  public:
    int minRow(int N, int M, vector<vector<int>> A) {
        // code here
        int ansIndex=0,minOneCount=INT_MAX;
        for(int i=0;i<N;i++){
            int oneCount=0;
            for(int j=0;j<M;j++){
                if(A[i][j]==1){
                    oneCount+=1;
                }
            }
            if(oneCount<minOneCount){
                ansIndex=i+1;
                minOneCount=oneCount;
            }
        }
        return ansIndex;
    }
};
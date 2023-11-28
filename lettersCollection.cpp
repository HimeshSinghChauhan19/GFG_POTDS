class Solution{
    public:
    vector<int> matrixSum(int n, int m, vector<vector<int>> mat, int q, vector<int> queries[])
    {
        // code here
        vector<int>ans;
        int arr[5]={1,-1,0,-2,2};
        for(int i=0;i<q;i++)
        {
            int type=queries[i][0];
            int x=queries[i][1],y=queries[i][2];
            int sum=0,last=0;
            if(type==2) last=5;
            else last=3;
            for(int j=0;j<last;j++)
            {
                for(int k=0;k<last;k++)
                {
                    int absx=abs(arr[j]),absy=abs(arr[k]);
                    int hori=x+arr[j],vert=y+arr[k];
                    if((hori>=0) && (vert>=0) && (hori<n) && (vert<m))
                    if((type==1 && (absx==1 || absy==1))  || (type==2 && (absx==2 || absy==2)))
                    sum+=mat[hori][vert];
                }
            }
            ans.push_back(sum);
        }
        return ans;
    }
};
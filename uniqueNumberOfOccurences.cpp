class Solution
{
    public:
    bool isFrequencyUnique(int n, int arr[])
    {
        /*
        Time: 0.14
        */
        map<long long, int> mp1;
        for(int i=0;i<n;i++){
            mp1[arr[i]]=0;
        }
        for(int i=0;i<n;i++){
            
            mp1[arr[i]]+=1;
        }
        map<long long,int>::iterator iter;
        
        map<int,int> mp2;
        
        for(iter=mp1.begin();iter!=mp1.end();iter++){
        // while(iter!=mp1.end()){
            // cout<<iter->first<<" and "<< iter->second<<endl;
            mp2[iter->second]=0;
        }
        for(iter=mp1.begin();iter!=mp1.end();iter++){
        // while(iter!=mp1.end()){
            // cout<<iter->first<<" and "<< iter->second<<endl;
            mp2[iter->second]+=1;
        }
        
        map<int,int>::iterator iter1;
        // cout<<"Freqs\n";
        for(iter1=mp2.begin();iter1!=mp2.end();iter1++){
        // while(iter!=mp1.end()){
            if(iter1->second>1){
                return false;
            }    
        }
        return true;
    }
};
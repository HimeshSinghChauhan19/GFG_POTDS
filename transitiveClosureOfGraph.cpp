class Solution{
public:
    vector<vector<int>> transitiveClosure(int N, vector<vector<int>> graph)
    {
        // It's a straighforward prob of Floyd Warshall Algorithm
        
        // i: The through Vertex
        for(int i=0;i<N;i++){
            
            // j: The current Vertex
            for(int j=0;j<N;j++){
                
                // k: The vertex to reach( destination vertex )
                for(int k=0;k<N;k++){
                    if(graph[j][k]==0)
                    graph[j][k]=(((graph[j][i]!=0 && graph[j][i]+graph[i][k]>=2) || j==k )?1:0);
                    
                }
            }
        }
        return graph;
    }
};
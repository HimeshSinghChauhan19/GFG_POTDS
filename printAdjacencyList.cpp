class Solution {
  public:
    // Function to return the adjacency list for each vertex.
    vector<vector<int>> printGraph(int V, vector<pair<int,int>>edges) {
        // Code here 
        vector<vector<int>> vect(V,vector<int>(0));
        for(auto itr=edges.begin();itr!=edges.end();itr++){
            vect[itr->first].push_back(itr->second);
            vect[itr->second].push_back(itr->first);
        }
        return vect;
    }
};
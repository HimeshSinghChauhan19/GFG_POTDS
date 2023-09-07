class Solution {
public:
    void dfs(int i, vector<int> adj[], vector<int>& vis, vector<int>& topo) {
        vis[i] = 1;
        for (auto edge : adj[i]) {
            if (!vis[edge])
                dfs(edge, adj, vis, topo);
        }
        topo.push_back(i);
    }
    int findMotherVertex(int V, vector<int> adj[]) {
        vector<int> vis(V, 0), topo;
        for (int i = 0; i < V; ++i) {
            if (!vis[i])
                dfs(i, adj, vis, topo);
        }
        if (topo.size() == V) {
            int motherVer = topo.back();
            vis.assign(V, 0);
            topo.clear();
            dfs(motherVer, adj, vis, topo);
            if (topo.size() == V)
                return motherVer;
        }
        return -1;
    }
};
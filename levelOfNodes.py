class Solution:
    def __init__(self):
        self.ans=-1
        
    #Function to find the level of node X.
    def dfs(self,adj,visited,X,curr_vertex,curr_level):
        
        # Now this vertex is visited
        visited[curr_vertex]=1
        
        # exploring the vertices that we can go from this vertex
        # Here adj[curr_vertex] is a list which contains the negihbours of the vertex curr_vertex
        for i in adj[curr_vertex]:
            if(i==X):
                # I am getting the desired vertex at the curr_level vertex,
                # means X is gonna be at the level curr_level+1
                self.ans=curr_level+1
                return True
            
            # If this vertex is not yet visited, then explore this, if returns true
            # then just return true, means we got the ans somewhere later
            if( visited[i]!=1 and self.dfs(adj,visited,X,i,curr_level+1) ):
                return True
                
            # if this vertex doesn't lead us to the desired X vertex then I'll have to explore further vertices too
            
        # if there is no possible path from curr_vertex to X vertex, then we are gonna be here and will return False
        return False
    
    def nodeLevel(self, V, adj, X):
        # code here
        
        # so that I don't take the ans of the previous Test Case
        self.ans=-1
        
        # print(adj)
        # print(f"X: {X}")
        # print(f"V: {V}")
        
        # To store which vertices are visited till now, if the vertex is visited then its index will have 1 else -1
        visited=[-1 for i in range(V)]
        
        # Starting to go to the depth from the 0th vertex at 0 level
        self.dfs(adj,visited,X,0,0)
        # print(f"The ans after dfs is {self.ans}")
        return self.ans
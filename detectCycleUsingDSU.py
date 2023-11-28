class Solution:
    
    def getParent(self,vertex,parents):
        if(parents[vertex]!=vertex):
            parent=self.getParent(parents[vertex],parents)
            return parent
            
        return vertex
    
    def union(self,ver1,ver2,par1,par2,parents,ranks):
        if(ranks[par1]>ranks[par2]):
            # if ver1 should be the parent
            parents[par2]=par1
            ranks[par1]+=ranks[par2]
            
        elif(ranks[par2]>ranks[par1]):
            # if ver2 should be the parent
            parents[par1]=par2
            ranks[par2]+=ranks[par1]
            
        else:
            # will make ver1 as the parent of ver2
            parents[par2]=par1
            # now that ver1 is the parent, it's rank will be increased
            ranks[par1]+=ranks[par2]
    
    def detectCycleUtil(self,edges,parents,ranks):
        for u,v in edges:
            par1=self.getParent(u,parents)
            par2=self.getParent(v,parents)
            if(par1==par2):
                return True
            self.union(u,v,par1,par2,parents,ranks)
        return False
        
    def detectCycle(self, V, adj):
        #Code here
        '''
        Here adj is a 2D list having the connected vertices of 0th vertex as a list in 0th place
        '''
        # print(adj)
        # print(f"V is {V}")
        visited=[-1 for i in range(V)]
        edges=list()
        
        for u,ls in enumerate(adj):
            for v in ls:
                if(visited[v]==-1):
                    edges.append([u,v])
            # now we are done with this u'th vertex, won't be considering this an end ver of 
            # any other vertex
            visited[u]=1
            
        # print(f"Edge set is {edges}")
        
        parents=[i for i in range(V)]
        ranks=[1 for i in range(V)]
        ans=self.detectCycleUtil(edges,parents,ranks)
        
        # for i in range(V):
        #     print(self.getParent(i,parents))
        return 1 if(ans) else 0
        
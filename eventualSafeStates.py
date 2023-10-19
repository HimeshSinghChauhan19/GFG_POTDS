class Solution:    
    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
        # code here
        WHITE, GRAY, BLACK = 0, 1, 2

        def isSafe(node):
            if color[node] != WHITE:
                return color[node] == BLACK
            
            color[node] = GRAY
            
            for neighbor in adj[node]:
                if color[neighbor] == GRAY or (not isSafe(neighbor)):
                    return False
            
            color[node] = BLACK
            return True

        color = [WHITE] * V
        result = [node for node in range(V) if isSafe(node)]
        return sorted(result)
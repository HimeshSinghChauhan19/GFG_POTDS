from collections import deque

class Solution:
    
    def helper(self, node, target):
        if node.data==target and not self.target_node:
            self.target_node = node
        
        if node.left:
            self.ancestor[node.left] = node
            self.helper(node.left, target)
        
        if node.right:
            self.ancestor[node.right] = node
            self.helper(node.right, target)

    def KDistanceNodes(self, root, target, k):
        self.ancestor = {}
        self.target_node = None
        self.helper(root, target)

        q = deque()
        q.append([self.target_node, 0])
        res = []
        visited = {self.target_node}

        while q:
            node, distance = q.popleft()

            if distance==k:
                res.append(node.data)
                continue

            if self.ancestor.get(node, None):
                if self.ancestor[node] not in visited:
                    q.append([self.ancestor[node], distance+1])
                    visited.add(self.ancestor[node])
            
            if node.left and node.left not in visited:
                q.append([node.left, distance+1])
                visited.add(node.left)
            
            if node.right and node.right not in visited:
                q.append([node.right, distance+1])
                visited.add(node.right)
        
        return sorted(res)
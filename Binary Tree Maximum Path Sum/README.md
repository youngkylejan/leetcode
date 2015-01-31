# Binary Tree Maximum Path Sum

**Tree, Depth-first Search**

> for each node, potential max sum is node.val + left.val + right.val    
> dfs each node to get potential max sum  
> **parent max sum should be node.val + left.val or node.val + right.val**  
> **remember ignore the node with negative value**  


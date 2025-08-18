class Solution145:
    def postorderTraversal(self, root) :
        res=[]
        if root is None:
            return res
        main_stack=[]
        sup_stack=[]
        sup_stack.append(root)
        while len(sup_stack)>0:
            node=sup_stack.pop()
            main_stack.append(node.val)
            
            if node.left is not None:
                sup_stack.append(node.left)
            if node.right is not None:
                sup_stack.append(node.right)
        while main_stack:
            res.append(main_stack.pop())
        return res
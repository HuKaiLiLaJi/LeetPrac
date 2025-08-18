class Solution107:
    def levelOrderBottom(self, root) :
        true_res=[]
        res=[]
        if root is None:
            return res
        sup_que=[]
        sup_que.append(root)
        while sup_que:
            level_size=len(sup_que)
            cur_level=[]
            for i in range(0,level_size):
                node=sup_que.pop(0)
                cur_level.append(node.val)
                if node.left is not None: 
                    sup_que.append(node.left )
                if node.right is not None:
                    sup_que.append(node.right)
            if cur_level:
                res.append(cur_level)
        while res:
            true_res.append(res.pop())
        return true_res
class Solution209:
    def minSubArrayLen(self, target: int, nums) -> int:
        left = 0
        cur_sum = 0
        min_len = float('inf')  # 用无穷大更好
        
        for right in range(len(nums)):
            # 扩展窗口
            cur_sum += nums[right]
            
            # 当满足条件时，尝试收缩窗口
            while cur_sum >= target:
                # 更新最小长度
                min_len = min(min_len, right - left + 1)
                
                # 收缩窗口
                cur_sum -= nums[left]
                left += 1
        
        # 如果没找到满足条件的子数组
        return 0 if min_len == float('inf') else min_len
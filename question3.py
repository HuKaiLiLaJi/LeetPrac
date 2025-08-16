class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sup_map={}
        left=0
        if(len(s)==0 ):
            return 0 
        if(len(s)==1):
            return 1
        
        max_len=0
        for right in range(0,len(s)):
            if s[right] not in sup_map:
                sup_map[s[right]]=right
            else:
                pre=sup_map.get(s[right])
                sup_map.pop(s[right])
                sup_map[s[right]]=right
                left=max(left,pre+1)
            current_len=right-left+1
            if current_len>max_len:
                max_len=current_len
        return max_len
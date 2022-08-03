class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        post = []
        
        for i in range(len(nums)):
            if i == 0:
                pre.append(1)
                continue
                
            pre.append(pre[i-1] * nums[i-1])
            
        for i in range(len(nums)-1, -1, -1):
            print(i)
            if i == len(nums)-1:
                post.append(1)
                continue
                
            post.append(post[len(nums)-i-2] * nums[i+1])
            
        post = list(reversed(post))
        
        res = []
        
        for i in range(len(nums)):
            res.append(pre[i] * post[i])
            
        return res
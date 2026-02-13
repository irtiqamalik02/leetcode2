class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        # area = min (maxL, maxR) * height at that point
        l,r = 0, len(height)-1
        maxL,maxR = height[l], height[r]
        area = 0

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL,height[l])
                area += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                area += maxR - height[r]

        return area        


        
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            # 1. Calculate current width and height
            width = right - left
            h = min(height[left], height[right])

            # 2. Calculate current area and update max
            current_water = width * h
            max_water = max(max_water, current_water)

            # 3. Move the pointer pointing to the shorter bar
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
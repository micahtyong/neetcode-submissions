# Two pointers: Naive
# Area between two bars = min(h1, h2) * (h1 - h2)
# maxArea = max(currMax, new)
# Runtime is O(n^2)

# Opt
# When to shift left vs shift right?
# Then worst case is O(n) because we always move right

# [1,7,2,5,4,7,3,6]
# area = 1
# - moving h1 right : area is 0
# - moving h2 right : area is 2
# area = 2
# - moving h1 right : area is 2
# - moving h2 right : area is 3
# area = 3
# - moving h1 right : area is 10
# - moving h2 right : area is 5
# area = 10; h1 is now at 1
# - moving h1 right : area is 2
# - moving h2 right : area is 8
# area = 8, maxArea = 10
# - moving h1 right : area is 4
# - moving h2 right : area is 28
# area = 28
# - moving h1 
# ...
# at some point we cannot move h2 right anymore
# and thus can only move h1

# counter: height=[1,7,2,5,12,3,500,500,7,8,4,7,3,6]
# seeing some very large number, but rules will pass right by this...
# area := 13
# shiftH1Right => area, 6 x 12
# shiftH2Left => area, 12

# [1,7,2,5,4,7,3,6]
# close in, try to maximize height. track maxArea along the way
# area := 7
# shiftH1Right => area, 36
# shiftH2Left => area, 6

# probably stop trying to find potentialArea max?
# try moving shorter bar only

class Solution:
    # Idea: Move shorter bar only
    def maxArea(self, heights: List[int]) -> int:
        h1, h2 = 0, len(heights) - 1

        def getArea(h1, h2):
            # h1 and h2 are indices into heights
            return min(heights[h1], heights[h2]) * (h2 - h1)
        
        maxArea = getArea(h1, h2)
        # print("start", maxArea)

        while h1 < h2:
            maxArea = max(maxArea, getArea(h1, h2))
            print(getArea(h1, h2), maxArea, h1, h2)
            if heights[h1] < heights[h2]:
                h1 += 1
            else:
                h2 -= 1
        
        return maxArea

    # Problem is that we only find a local max, not a global one.
    def maxAreaNaive(self, heights: List[int]) -> int:
        h1, h2 = 0, 1

        def getArea(h1, h2):
            # h1 and h2 are indices into heights
            return min(heights[h1], heights[h2]) * (h2 - h1)
        
        maxArea = getArea(h1, h2)
        print("start", maxArea)

        while h1 < len(heights) - 1:
            shiftH1 = getArea(h1 + 1, h2) 

            # h2 reached the end
            if h2 >= len(heights) - 1:
                maxArea = max(shiftH1, maxArea)
                print("h2 reached the end, shifting h1...", h1, h2, shiftH1, maxArea)
                h1 += 1
                continue
            
            shiftH2 = getArea(h1, h2 + 1)
            if shiftH1 > shiftH2:
                maxArea = max(shiftH1, maxArea)
                print("shiftH1 yields larger area", h1, h2, shiftH1, maxArea)
                h1 += 1
            else:
                maxArea = max(shiftH2, maxArea)
                print("shiftH2 yields larger area", h1, h2, shiftH2, maxArea) 
                h2 += 1
        
        return maxArea



            
'''
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
'''

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor:int) -> List[List[int]]:
        if image == None or image[sr][sc] == newColor:
            return image
        self.fill(image,sr,sc, image[sr][sc],newColor)
        return image
    def fill(self, image, r, c, initial, newColor):
        if r<0 or r >= len(image) or c<0 or c >= len(image[0]) or image[r][c] != initial:
            return
        image[r][c] = newColor
        self.fill(image, r+1, c, initial, newColor)
        self.fill(image, r-1, c, initial, newColor)
        self.fill(image, r, c-1, initial, newColor)
        self.fill(image, r, c+1, initial, newColor)

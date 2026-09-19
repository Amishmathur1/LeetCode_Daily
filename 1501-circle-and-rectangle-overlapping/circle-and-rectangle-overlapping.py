class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        
        #x min and y min => x1, y1
        #x max and y max => x2, y2
        # if x1 <= xCenter <= x2 and y1 <= yCenter <= y2:
        #     return True

        # x_circle = xCenter
        # y_circle = yCenter

        # for i in range(radius):
        #     new_x, new_y = x_circle + 1, x_circle + 1
        #     if x1 <= new_x <= x2 and y1 <= new_y<= y2:
        #         return True
        
        # return False

        close_x = max(x1, min(xCenter, x2))
        close_y = max(y1, min(yCenter, y2))

        #Euclidean Distance 
        d = (xCenter - close_x)**2 + (yCenter - close_y)**2

        if d <= radius**2:
            return True
        else:
            return False
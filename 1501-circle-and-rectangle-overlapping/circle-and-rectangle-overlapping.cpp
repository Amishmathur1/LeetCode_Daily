class Solution {
public:
    bool checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
        int close_x = max(x1, min(xCenter, x2));
        int close_y = max(y1, min(yCenter, y2));

        int dx = xCenter - close_x;
        int dy = yCenter - close_y;

        return (dx * dx + dy * dy) <= (radius * radius);
    }
};
class Solution {
    public int findContentChildren(int[] g, int[] s) {

        Arrays.sort(g);
        Arrays.sort(s);

        int i = 0, j = 0, cnt = 0;

        for (i = 0; i < g.length; i++) {

            for (j = 0; j < s.length; j++) {

                if (s[j] == 0)
                    continue;
                else {
                    if (s[j] >= g[i]) {
                        cnt++;
                        s[j] = 0;
                        break;
                    }
                }
            }
        }

        return cnt;
    }
}
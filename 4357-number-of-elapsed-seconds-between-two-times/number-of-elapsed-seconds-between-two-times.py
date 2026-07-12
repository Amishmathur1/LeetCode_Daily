class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        s = startTime.split(':')
        e = endTime.split(':')
        s = [int(i) for i in s]
        e = [int(i) for i in e]

        end = (3600*e[0]) + (60*e[1]) + e[2]
        start = (3600*s[0]) + (60*s[1]) + s[2]

        return (end-start)
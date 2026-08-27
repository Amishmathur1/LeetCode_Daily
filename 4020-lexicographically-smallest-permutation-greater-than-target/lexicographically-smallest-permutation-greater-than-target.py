# class Solution:
#     def lexGreaterPermutation(self, s: str, target: str) -> str:
#         s = [i for i in s]

#         ans = []
#         path = []
#         F = [False] * len(s)

#         min_val = None

#         def backtrack():
#             nonlocal min_val
#             if len(path) == len(s):
#                 if ''.join(path) > target:
#                     candidate = ''.join(path)

#                     if min_val is None or candidate < min_val:
#                         min_val = candidate

#             for i in range(len(s)):
#                 if F[i] == False:
#                     path.append(s[i])
#                     F[i] = True

#                     backtrack()

#                     path.pop()
#                     F[i] = False

#         backtrack()
#         if min_val == None:
#             return ''
        
#         return min_val
#         # min_ans = ''.join(ans[0])

#         # for i in ans:
#         #     if ''.join(i) < min_ans:
#         #         min_ans = ''.join(i)

#         # return (min_ans) 

# from collections import Counter

# class Solution:
#     def lexGreaterPermutation(self, s: str, target: str) -> str:
#         n = len(s)
#         counts = Counter(s)
#         prefix_counts = Counter()
        
#         for i in range(n + 1):
#             # Try to place a character strictly greater than target[i] at index i
#             if i < n:
#                 for ch_code in range(ord(target[i]) + 1, ord('z') + 1):
#                     ch = chr(ch_code)
#                     if counts[ch] - prefix_counts[ch] > 0:
#                         # Found a valid choice! Construct the answer.
#                         res = list(target[:i]) + [ch]
                        
#                         # Update remaining character counts
#                         rem_counts = counts - prefix_counts
#                         rem_counts[ch] -= 1
                        
#                         # Append remaining characters in sorted order
#                         for char_code in range(ord('a'), ord('z') + 1):
#                             c = chr(char_code)
#                             res.extend([c] * rem_counts[c])
                            
#                         return "".join(res)
            
#             # Match current position with target[i] if possible
#             if i < n and counts[target[i]] - prefix_counts[target[i]] > 0:
#                 prefix_counts[target[i]] += 1
#             else:
#                 # Cannot extend the exact prefix match further
#                 break
                
#         return ""

from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        total_counts = Counter(s)
        
        # Step 1: Precompute prefix character frequencies required to match target[:i]
        # prefix_counts[i] stores frequencies used by target[0...i-1]
        prefix_counts = [Counter()]
        curr = Counter()
        
        valid_prefix_len = 0
        for i in range(n):
            curr[target[i]] += 1
            # Check if total_counts has enough characters to form target[:i+1]
            if all(curr[ch] <= total_counts[ch] for ch in curr):
                prefix_counts.append(curr.copy())
                valid_prefix_len = i + 1
            else:
                break
                
        # Step 2: Iterate backwards from the maximum possible prefix length
        for i in range(valid_prefix_len, -1, -1):
            if i == n:
                continue
                
            used = prefix_counts[i]
            
            # Find the smallest character strictly greater than target[i]
            for ch_code in range(ord(target[i]) + 1, ord('z') + 1):
                ch = chr(ch_code)
                if total_counts[ch] - used[ch] > 0:
                    # Found the pivot point! Construct the result
                    res = list(target[:i]) + [ch]
                    
                    rem_counts = total_counts - used
                    rem_counts[ch] -= 1
                    
                    # Fill the remaining positions in sorted order
                    for char_code in range(ord('a'), ord('z') + 1):
                        c = chr(char_code)
                        res.extend([c] * rem_counts[c])
                        
                    return "".join(res)
                    
        return ""
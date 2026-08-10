class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(s) < len(t):
            return ""

        # Step 1: Count frequency of characters in t
        countT = {}
        for char in t:
            countT[char] = countT.get(char, 0) + 1

        window = {}
        have, need = 0, len(countT)
        res, res_len = [-1, -1], float("inf")
        l = 0

        # Step 2: Expand the right pointer
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1

            # If current character satisfies requirement in t
            if char in countT and window[char] == countT[char]:
                have += 1

            # Step 3: Shrink the left pointer when all requirements are met
            while have == need:
                # Update our minimum window result
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                # Pop from left of window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if res_len != float("inf") else ""
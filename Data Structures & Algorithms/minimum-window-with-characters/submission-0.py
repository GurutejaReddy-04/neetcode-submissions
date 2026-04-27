class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        need_count = {}
        for char in t:
            need_count[char] = need_count.get(char, 0) + 1

        window_count = {}

        have = 0
        need = len(need_count)

        result = [-1, -1]
        result_length = float("inf")

        left = 0

        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1

            if char in need_count and window_count[char] == need_count[char]:
                have += 1

            while have == need:
                # update result
                if (right - left + 1) < result_length:
                    result = [left, right]
                    result_length = right - left + 1

                # shrink from left
                window_count[s[left]] -= 1

                if s[left] in need_count and window_count[s[left]] < need_count[s[left]]:
                    have -= 1

                left += 1

        left, right = result

        return s[left:right + 1] if result_length != float("inf") else ""
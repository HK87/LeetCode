class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmp_answer = start_index = 0
        used_words = {}
        for i, char in enumerate(s):
            if char in used_words:
                tmp_answer = max(tmp_answer, i - start_index)
                # need to think about 2nd "a" about "abba".
                start_index = max(start_index, used_words[char] + 1)
            used_words[char] = i
        return max(tmp_answer, len(s) - start_index)
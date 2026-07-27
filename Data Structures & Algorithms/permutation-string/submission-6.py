class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = {}
        freq_window = {}
        left = 0
        for ch in s1:
            freq_s1[ch] = freq_s1.get(ch, 0) + 1
        for right in range(len(s2)):
            ch = s2[right]
            freq_window[ch] = freq_window.get(ch, 0) + 1
            while freq_window.get(ch, 0) > freq_s1.get(ch, 0):
                left_char = s2[left]
                freq_window[left_char] = freq_window.get(left_char, 0) - 1
                left += 1
            if right - left + 1 == len(s1):
                return True
        return False



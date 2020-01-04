class Solution:
    def myAtoi(self, s: str) -> int:
        s = list(s.strip())
        if len(s) == 0:
            return 0
        if s[0] == '-':
            sign = -1
        else:
            sign = 1

        if s[0] in ['-','+'] :
            del s[0]

        number, i = 0, 0
        while i < len(s) and s[i].isdigit() :
            # number*10 + int(s[i])だと桁あふれに対応できないので
            # 一度Unicodeに変換して、0との差分をとるロジックになっている
            number = number*10 +  int(ord(s[i]) - ord('0'))
            i += 1
        return max(-2**31, min(sign * number,2**31-1))
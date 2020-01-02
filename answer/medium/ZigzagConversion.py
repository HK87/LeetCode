class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1 or num_rows >= len(s):
            return s

        answer = [''] * num_rows
        i = 0
        up_down = 1 # index = 0 に向かって進む時 +1, index = 0から離れる時 -1
        for x in s:
            answer[i] += x
            if i == 0:
                up_down = 1
            elif i == num_rows -1:
                up_down = -1
            i += up_down

        return ''.join(answer)


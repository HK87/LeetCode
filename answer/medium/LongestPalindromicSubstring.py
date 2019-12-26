class Solution:
    def longestPalindrome(self, s):
        len_s = len(s)
        if len_s <= 1: return s
        ans_start, ans_len, i = 0, 1, 0
        while i < len_s:
            # 確認時の最大文字数の半分より残りが少ない =
            # 最大文字数を超える答えはありえないのでチェック終了
            if len_s - i <= ans_len / 2:
                break
            tmp_s, tmp_e = i, i
            # abba, acccaのように同じ文字列が続く場合を考慮
            # この考慮を行うことによって、答えが奇数の場合も偶数の場合も吸収できる
            # この考慮を行わない場合、答えが奇数の場合と偶数の場合用にループを2回回さないといけなくなってしまう
            while tmp_e < len_s - 1 and s[tmp_e] == s[tmp_e + 1]:
                tmp_e += 1
            # この後、起点となる箇所を答えの中心地点と想定して左右に探索を広げる
            # 実施済のwhile文で、同じ文字列が続いている場合のチェックは完了しているため不要な確認
            i = tmp_e + 1
            # 左右に探索を広げる
            while tmp_e < len_s - 1 and tmp_s and s[tmp_e + 1] == s[tmp_s - 1]:
                tmp_e, tmp_s = tmp_e + 1, tmp_s - 1
            if tmp_e - tmp_s + 1 > ans_len:
                ans_start, ans_len = tmp_s, tmp_e - tmp_s + 1
        return s[ans_start: ans_start + ans_len]
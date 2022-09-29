s = "abcabcbb"

class Tack:
    def __init__(self, s):
        self.s = s
    def not_replied(self):
        d = {}
        max_l = start = 0
        for i, c in enumerate(self.s):
            if c in d and start <= d[c]:
                start = d[c] + 1
            else:
                max_l = max(max_l, i - start + 1)

            d[c] = i

        return max_l

tc = Tack(s)
print(tc.not_replied())

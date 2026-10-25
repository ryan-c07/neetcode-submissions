class Solution:
    def reverseBits(self, n: int) -> int:
        decimal = 0
        print(len(str(n)), str(n), n)
        len_decimal = len(format(n, "b"))
        final = "0"*(32-len_decimal) + str(format(n, "b"))
        for i in range(len(str(final))):
            decimal += 2**i * int(str(final)[i])
            print(2**i, int(str(final)[i]))
        return decimal
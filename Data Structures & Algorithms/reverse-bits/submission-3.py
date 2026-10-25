class Solution:
    def reverseBits(self, n: int) -> int:
        binary = "0"*(32-len(format(n, "b"))) + format(n, "b")
        num = 0
        for i in range(len(binary)):
            num += 2**i * int(binary[i])

        return num
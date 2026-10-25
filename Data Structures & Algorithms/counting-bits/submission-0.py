class Solution:
    def countBits(self, n: int) -> List[int]:
        list = []
        for i in range(n+1):
            list.append(format(i, "b").count("1"))
        return list
        
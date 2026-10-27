class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        res = []
        for string in strs:
            alphabet = [0]*26
            for i in range(len(string)):
                alphabet[ord(string[i]) - 97] += 1
            key = tuple(alphabet)
            if key in d:
                res[d[key]].append(string)
            else:
                d[key] = len(res)
                res.append([string])
        return res
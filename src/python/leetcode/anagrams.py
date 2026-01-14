

class Solution:
    def groupAnagrams(self, strs):
        hashMap = {}
        for string in strs:
            key = "".join(sorted(string))
            if key in hashMap:
                hashMap[key].append(string)
            else:
                hashMap[key] = [string]
        print(list(hashMap.values()))           
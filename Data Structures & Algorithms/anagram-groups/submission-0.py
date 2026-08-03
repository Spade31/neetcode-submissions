class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()
            
        def count(s : str):
            _res = [0] * 26
            for i in s:
                _res[ord(i) - 97] += 1
            return tuple(_res)
        
        for i in strs:
            _tmp = count(i)
            if _tmp not in res.keys():
                res[_tmp] = [i]
            else:
                res[_tmp].append(i)
      
        output = []

        for ky, val in res.items():
            output.append(val)

        return output
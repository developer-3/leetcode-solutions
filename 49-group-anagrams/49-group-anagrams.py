class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters = {}
        anagrams = {}
        
        for s in strs:
            s_sort = sorted(list(s))
            if s_sort in letters.values():
                k = list(letters.values()).index(s_sort)
                anagram = anagrams[k]
                anagram.append(s)
                anagrams[k] = anagram
            else:
                letters[len(letters)] = s_sort
                anagrams[len(letters)-1] = [s]
            
        return [a for a in anagrams.values()]
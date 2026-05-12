class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                 count[ord(c) - ord('a')] += 1 # unique count for each group of anagrams

            
            anagrams[tuple(count)].append(s) # convert list -> tuple so its hashable
        return list(anagrams.values())





        
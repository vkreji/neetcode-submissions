class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
            # dictionary with key: number -> value: frequency

        new = []
        for num, freq in count.items():
            new.append([freq,num])

        new.sort()

        ans = []

        while len(ans) < k:
            ans.append(new[-1][1]) # add the num with the highest freq
            new.pop(-1) # keep removing most freq till k is reached

        return ans


        


        
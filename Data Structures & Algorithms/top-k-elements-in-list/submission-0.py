class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if(len(nums) == 1):
            return nums
        di = dict(Counter(nums))
        d = dict(sorted(di.items(),key=lambda item: item[1], reverse=True))
        return list(d)[:k]

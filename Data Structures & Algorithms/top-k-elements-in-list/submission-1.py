class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        sorted_hashmap = sorted(hashmap, key=hashmap.get, reverse=True)

        return sorted_hashmap[:k]
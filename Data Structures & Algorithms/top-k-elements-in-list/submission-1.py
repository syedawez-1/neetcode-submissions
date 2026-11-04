class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency = {}

        # Count frequency
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        # Sort based on frequency
        sorted_nums = sorted(frequency, key=frequency.get, reverse=True)

        # Return top k elements
        return sorted_nums[:k]
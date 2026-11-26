class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # Immediate thought is brute-forcing it and use a dict keeping track of all unique numbers
        # # in num. The key would be the num and the val would be
        # # the frequency

        # num_to_freq = {}

        # # Establishes the dict
        # for num in nums:
        #     if num in num_to_freq.keys():
        #         num_to_freq[num] += 1
        #     else:
        #         num_to_freq[num] = 1

        # # Now I need to know what freq is the highest. Can I sort the dict
        # # by keys? 
        # # This is O(nlogn) -- bad
        # desc_sorted_num_to_freq = dict(sorted(num_to_freq.items(), key=lambda item: item[1], reverse=True))

        # # Now I can grab the first k items in the keys
        # keys = list(desc_sorted_num_to_freq)
        # return keys[:k]

        # Now is there a faster and more storage efficient way?
        # The recommended Time & Space complexity is O(n) for both.
        # Means I should essentially work with the list itself.
        # What if I traverse the list and keep a running winner. But I 
        # need to keep k running winners. I will take a hint

        # Hint 1 - Hint 1 is above lol. Open Hint 2.
        # Hint 2 - Algorithm which involves grouping numbers based on 
        # their frequency. The topics include Divide and Conquer,
        # Bucket Sort, Heap. Time to watch a video. Bucket Sort. 
        # The index is the count, the values are arrays of numbers 
        # which have that count. Use sets? No we still use a dict and list

        count = {}
        frequency = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            frequency[c].append(n)
        
        top_k_frequent = []
        for c in range(1, len(frequency)):
            if frequency[-c]:
                top_k_frequent += frequency[-c]
            
            if len(top_k_frequent) >= k:
                return top_k_frequent[:k]

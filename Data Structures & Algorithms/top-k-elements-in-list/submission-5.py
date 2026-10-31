class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1. count how often each element appears using dictionary
        #2. Find the top k frequencies, use buckets index by frequencies
            #a. create the buckets using for loop, should end up with n+1 buckets in one bucket like a matrix
                # N+1 BUCKETS, BECAuse 0 bucket is unused and to get n freq bucket we need to go one up
            #b. fill those buckets with the frequencies, which was the dictionaries value
                #1 appears 3 times is coded as freq[3].append(1)
            #c. Collect top k freq elements by appending to result array
                #the bucket has the most frequent elements is the the one with the highest index
                # so thats why we check each bucket from reverse, but need a nested for loop if multiple numbers in bucket, appending the num, if thhere is nothing in the bucket we are auto skipping. we keep appending until our resulting array ==k then return

            counter = {}

            for num in nums:
                if num not in counter:
                    counter[num] = 1
                else:
                    counter[num] +=1

            freq = []
            for i in range(len(nums) +1):
                freq.append([])
            
            for num, value in counter.items():
                freq[value].append(num)
            
            res = []
            #stop at the fist bucket because we aren't using the last bucket (freq = 0), because each num appears at least once
            for i in range(len(freq)-1, 0, -1):
                for num in freq[i]:
                    res.append(num)
                    if len(res) == k:
                        return res
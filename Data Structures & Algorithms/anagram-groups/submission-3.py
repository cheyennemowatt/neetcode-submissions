class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        #input: list of strinsg
        #output: list of lists

        """
        How are we comparing frequency of characters in one string to another?
        How do we group the ones with same character frequency?
        If we are later down the line, and have added a string to a sulist, how do we check which sublist it belongs to?
        """

        res = defaultdict(list) # maps key (charCount) to value (list of anagrams)
        #use defaultdict(list) instead of {} just incase we try to add a key to the dictionary that doesn't exist yet
        #default value for each new key is a list
        for word in strs:
            # we need to count how many of each character from a - z it has so initialize empty list with 26 spots
            count = [0] * 26
            for char in word:
                # where we actually count the frequency
                # Since we want to map a to index 0 and z to index 25 we use [ord(c) - ord("a")] is taking the ascii values 
                count [ord(char) - ord("a")] += 1
            
            res[tuple(count)].append(word) #need to do a tuple since can't add lists as keys since they are mutable and we don't want keys to be changing
        
        return list(res.values())

    


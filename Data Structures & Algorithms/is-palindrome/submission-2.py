class Solution:
    def isPalindrome(self, s: str) -> bool:
        #create an empty string that will hold the
        #alphanumeric string without spaces/punctiation
        new_s = ""

        #iterate through old string and if char is a
        #alphanumeric string then add to new string

        for char in s:
            if char.isalnum():
                # we only add the lower because we want to be case insenstitive
                new_s += char.lower()

        #we return if new str equals the reverse of the new str new_s[::-1]
        # we don't compare with the original str 
        #because that has extra characters
        #will automatically return true or false
          

        return new_s  == new_s[::-1]
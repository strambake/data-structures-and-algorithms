# Given a string s, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Example 4:

# Input: s = ""
# Output: 0
#
# @Author: Swapnil Trambake, trambake.swapnil@gmail.com


class Solution(object):
    def __init__(self) -> None:
        super().__init__()


    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        output = 0
        charsWithoutRepeat = 0
        visited = {}
        index = 0
        while(index < len(s)):
            char = s[index]
            if char in visited:
                charsWithoutRepeat = 0
                index = visited[char] 
                visited.clear()
            else:
                charsWithoutRepeat  += 1
                visited[char] = index
                
            index += 1
            
            if output < charsWithoutRepeat:
                    output = charsWithoutRepeat

        return output


sol = Solution()


def lengthOfLongestSubstring(input):
    print ('Length of longest substring without repeating characters of string \"{}\" is {}'.format(input, sol.lengthOfLongestSubstring(input)))


if __name__ == "__main__":
    lengthOfLongestSubstring("abcabcbb")
    lengthOfLongestSubstring("bbbbb")
    lengthOfLongestSubstring("pwwkew")
    lengthOfLongestSubstring("")
    lengthOfLongestSubstring(" ")
    lengthOfLongestSubstring("dvdf")

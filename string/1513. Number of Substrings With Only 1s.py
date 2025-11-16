# Given a binary string s, return the number of substrings with all characters 1's. Since the answer may be too large, return it modulo 109 + 7.

# Example 1:
# Input: s = "0110111"
# Output: 9
# Explanation: There are 9 substring in total with only 1's characters.
# "1" -> 5 times.
# "11" -> 3 times.
# "111" -> 1 time.

# Example 2:
# Input: s = "101"
# Output: 2
# Explanation: Substring "1" is shown 2 times in s.

# Example 3:
# Input: s = "111111"
# Output: 21
# Explanation: Each substring contains only 1's characters.

def numSub(s): 
  modulo = (10**9 + 7) 
  result = 0 
  cons_ones = 0 #consecutive ones 

  for i in range(len(s)): 
    if s[i] == "1": 
      cons_ones += 1 
    elif s[i] == "0" or (i == (len(s) - 1 )) : 
      result += (((cons_ones+1)*cons_ones)//2)
      cons_ones = 0 
    
  return result 


print(numSub("0110011110011010101"))
      
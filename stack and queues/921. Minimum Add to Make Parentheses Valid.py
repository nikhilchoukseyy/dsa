# A parentheses string is valid if and only if:

# It is the empty string,
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

# For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
# Return the minimum number of moves required to make s valid.

# Example 1:
# Input: s = "())"
# Output: 1


# Example 2:
# Input: s = "((("
# Output: 3


def minAddToMakeValid(s):

# first approach TC = O(2n)
  # n = len(s)
  # count = 0 
  # open_p = 0 
  # for i in range(n): 
  #     if s[i] == "(": 
  #         open_p += 1 
  #     else : 
  #         if open_p == 0 : 
  #             count += 1 
  #         else : 
  #             open_p -=1 
          
  # close_p = 0 
  # for i in range(n-1,-1,-1): 
  #     if s[i] == ")": 
  #         close_p += 1 
  #     else : 
  #         if close_p == 0 : 
  #             count +=1 
  #         else : 
  #             close_p -= 1 
          
  
  # return count 

#second approach TC = O(n)

  stack = []
  for ch in s : 
      if ch == "(": 
          stack.append(ch)
      else : 
          if stack and stack[-1] == "(": 
              stack.pop()
          else : 
              stack.append(ch)
          
  return len(stack)

print(minAddToMakeValid("(())))("))
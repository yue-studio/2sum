#
# from: https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/


# This function prints the longest palindrome
# substring of st[]. It also returns the length
# of the longest palindrome
def longestPalSubstr(st):
  n = len(st) # get length of input string
  # table[i][j] will be false if substring
  # str[i..j] is not palindrome. Else
  # table[i][j] will be true
  table = [[0 for x in range(n)] for y in range(n)]
  
  # All substrings of length 1 are palindromes
  
  maxLength = 1
  i = 0
  while (i < n) :
    table[i][i] = True
    i = i + 1
	
  print("length = 2")
  # check for sub-string of length 2.
  start = 0
  i = 0
  while i < n - 1 :
    print("checking", st[i], st[i+1])
    if (st[i] == st[i + 1]) :
      table[i][i + 1] = True
      print("TRUE", st[i], st[i+1])
      start = i
      maxLength = 2
    i = i + 1
  
  
  print(">>>start max", start, maxLength, st[start:start + maxLength])

  print("length > 2")
  # Check for lengths greater than 2.
  # k is length of substring
  k = 3
  while k <= n :
    # Fix the starting index
    i = 0
    print("gap", k)
    while i < (n - k + 1) :
      # Get the ending index of
      # substring from starting
      # index i and length k
      j = i + k - 1

      # checking for sub-string from
      # ith index to jth index iff
      # st[i + 1] to st[(j-1)] is a
      # palindrome

      print("checking", st[i], st[j])
      if (table[i + 1][j - 1] and st[i] == st[j]) :
        table[i][j] = True
        print(">> TRUE", st[i+1], st[j-1], st[i], st[j])
        if (k > maxLength) :
          start = i
          maxLength = k
          print(">>>start max", start, maxLength, st[start:start + maxLength])
      i = i + 1
    k = k + 1
  
  print ("Longest palindrome substring is: ", st[start:start + maxLength])
  print(table)
  return maxLength # return length of LPS


# Driver program to test above functions
st = "forgeeksskeegfor"
st = "cabccba"
l = longestPalSubstr(st)
print ("Length is:", l)

# This code is contributed by Nikita Tiwari.()

#
# https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/
#
# Python3 program to find the length
# of the longest substring
# without repeating characters
def longestUniqueSubsttr(string):
    # last index of every character
    last_idx = {}
    max_len = 0
    
    # starting index of current
    # window to calculate max_len
    start_idx = 0
    
    for i in range(0, len(string)):
        print("checking", string[i])
		# Find the last index of str[i]
		# Update start_idx (starting index of current window)
		# as maximum of current value of start_idx and last
		# index plus 1
        if string[i] in last_idx:
           print(string[i],"repeat")
           start_idx = max(start_idx, last_idx[string[i]] + 1)
        
        print("start_idx", start_idx)
		    # Update result if we get a larger window
        max_len = max(max_len, i-start_idx + 1)

		    # Update last index of current char.
        last_idx[string[i]] = i
        print(last_idx)
    return max_len


# Driver program to test the above function
string = "geeksforgeeks"
print("The input string is " + string)
length = longestUniqueSubsttr(string)
print("The length of the longest non-repeating character" +
	" substring is " + str(length))

# from https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/

# A Simple Merge based O(n) solution to find
# median of two sorted arrays

""" This function returns median of ar1[] and ar2[].
Assumption in this function:
Both ar1[] and ar2[] are sorted arrays """
def getMedian(ar1, ar2, n, m) :
    i = 0 # Current index of input array ar1[]
    j = 0 # Current index of input array ar2[]
    m1, m2 = -1, -1
    # Since there are (n+m) elements,
    # There are following two cases
    # if n+m is odd then the middle
    # index is median i.e. (m+n)/2
    if((m + n) % 2 == 1) :
      for count in range(((n + m) // 2) + 1) :
        print("count", count)
        if(i != n and j != m) :
          print("comparing", i, ar1[i],j,ar2[j])
          if ar1[i] > ar2[j] :
            m1 = ar2[j]
            j += 1
          else :
            m1 = ar1[i]
            i += 1
        elif(i < n) :
          m1 = ar1[i]
          i += 1
		    # for case when j<m,
        else :
          m1 = ar2[j]
          j += 1
      return m1
    # median will be average of elements
    # at index ((m + n)/2 - 1) and (m + n)/2
    # in the array obtained after merging ar1 and ar2
    else :
      for count in range(((n + m) // 2) + 1) :
        print("count", count)
        m2 = m1
        if(i != n and j != m) :
          print("comparing", i, ar1[i],j,ar2[j])
          if ar1[i] > ar2[j] :
            m1 = ar2[j]
            j += 1
          else :
            m1 = ar1[i]
            i += 1
        elif(i < n) :
          m1 = ar1[i]
          i += 1
          
        # for case when j<m,
        else :
          m1 = ar2[j]
          j += 1
      return (m1 + m2)//2

# Driver code	
ar1 = [1,900]
ar2 = [5, 8, 10, 20]

n1 = len(ar1)
n2 = len(ar2)
print(getMedian(ar1, ar2, n1, n2))

# This code is contributed by divyesh072019

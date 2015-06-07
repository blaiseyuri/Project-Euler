# Function to return sum of multiples that are within a certain range
def MultiplesSum(multiple, end, start=1):
    mSum = 0
    naturals = range(start, end)
    offset = -start 
    if start == 0:
      raise ZeroDivisionError('Cannot start with the number 0')
    for num in multiple:
      for i in naturals:
        if i % num == 0 and naturals[i+offset] != 0:
          # print mSum,"+", i,"=",i+mSum
          mSum += i
          naturals[i+offset] = 0
        i += 1
    return mSum


# print MultiplesSum([3,5,2], 16)
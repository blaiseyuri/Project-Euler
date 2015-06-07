def MultipleFib(multiple, end, start=1):
  fSum = 0
  a = 0
  b = 1
  c = 0
  while a <= end:
    a = b + c
    c = b
    b = a
    if a % multiple == 0:
      fSum += a
  return fSum

print MultipleFib(2,4000000)



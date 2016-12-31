def squaredSequence(x):
  squaredSum = list()
  for i in range(1, x + 1):
    squaredNumber = (i**2)
    squaredSum.append(squaredNumber)
  return(sum(squaredSum))
  
def squareofSum(x):
  seriesSum = list()
  for i in range(1, x + 1):
    seriesSum.append(i)
  summation = sum(seriesSum)
  return(summation**2)


def factorial(n):
  returnVar = 1
  for i in range(1,n+1):
    returnVar = returnVar * i
  return returnVar

print(factorial(1))
print(factorial(4))
print(factorial(13))
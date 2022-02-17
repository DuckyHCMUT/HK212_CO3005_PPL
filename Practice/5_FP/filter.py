def lstSquare(L):
  return [L[0]**2] + lstSquare(L[1:]) if L else []

print(lstSquare([1,2,3]))
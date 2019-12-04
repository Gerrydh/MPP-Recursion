x = [1,2,3,4,5,6]

# def square(num):
  #  return num*num

square = lambda x: x * x

result = map(square, x)

print(result)

print(map(square, result))
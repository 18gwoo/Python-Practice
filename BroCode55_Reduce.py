# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeats process until 1 value remains. Recycle elements within an iterable until a single function remains
#
# reduce(function, iterable)

import functools

letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x, y,:x + y,letters) #x and y are first 2 elements within the iterable (H and E). It then performs the expression. In essence we are left with
print(word)                                         #"HE" + "L" + "L" + "O". it then repeats the process with HE and L and keeps going
                                                    # until we get "HELLO". Recycle each letter and get finished product (HELLO)
print()
factorial = [5,4,3,2,1]
result = functools.reduce(lambda x, y,:x * y,factorial)
print(result)
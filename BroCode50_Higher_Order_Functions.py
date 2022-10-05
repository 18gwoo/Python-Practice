#  Higher Order Function =  a function that either:
#                           1. accepts a function as an argument
#                               or
#                           2. returns a function
#                           (In python, functions are also treated as objects)

# ----- 1. accepts a function as an argument -----
def loud(text):
   return text.upper()

def quiet(text):
   return text.lower()

def hello(func): #accepts function as an argument
   text = func("Hello") #loud or quiet is called func while in this functions. "Hello" acts as text from the above functions
   print(text)


hello(loud) #loud is argument
hello(quiet)

# ------------ 2. returns a function -------------
def divisor(x):
   def dividend(y):
       return y / x
   return dividend


divide = divisor(2) # x = 2. Skips dividend function since it was not called yet. dividend is returned
print(divide(10)) # y = 10. Calls dividend and passes in 10
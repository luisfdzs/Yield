"""
  This function returns a list of the even values between the specified minimum and maximum

"""
def getEvenNumbers(min,max):
  for i in range (min,max):
    if not i%2:
      yield i

#Keeps a list with the even values between 0 and 10
myList = getEvenNumbers(0,10)

#prints the entire list
print(myList)

print(next(myList))
print(next(myList))
print(next(myList))
print(next(myList))
print(next(myList))

"""

  When the function getEvenNumbers(min,max) is called, the variable myList will store a generator object. This object does not contain the complete list of even numbers between 0 and 10, but contains the generator object of this list. Then, the next(myList) statement will return the next value of this list. This means that the for loop is executed only once, keeping the last value for the next time we use the next(myList) statement to return the next value in the list.

  The output will be: 

    <generator object getEvenNumbers at 0x00000241F0CE3BC0>
    0
    2
    4
    6
    8

"""
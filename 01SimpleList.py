"""
  This function returns a list of the even values between the specified minimum and maximum

"""
def getEvenNumbers(min,max):
  list = []
  for i in range (min,max):
    if not i%2:
      list.append(i)
  return list

#Keeps a list with the even values between 0 and 10
myList = getEvenNumbers(0,10)

#prints the entire list
print(myList)

#Prints some elements
print(myList[1])
print(myList[2])
print(myList[3])

"""
  When the function getEvenNumbers(min,max) is called, the for loop is executed from the beginning to the end
  before the function returns. Because of this, we have the entire list of even numbers between 0 and 10 stored
  in our variable 'myList'

  The output will be: 

    [0, 2, 4, 6, 8]
    2
    4
    6

"""
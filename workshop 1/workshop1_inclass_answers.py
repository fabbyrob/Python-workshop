#Function answers
#1
def hello():
    print("Hello World!")

#2
def hello2():
    return("Hello World!")

#3 
def product(x, y):
    return (x*y)

#4
def square(n):
    return(n**2)

#5
def sum_diff(x, y):
    return(x+y, x-y)

#6
def second(ls):
    return(ls[1])

#7
def nth(ls, n):
    return(ls[n])

#8
def strLen(aStr):
    return(len(aStr))

#Function tests
testList = ["apple","bottom","jeans",56,78]
testList2 = [1,4,6,2,9,7,0,187,65,1278,65,2,2]

print("~~~~~~~~~~~~Function exercises~~~~~~~~~~~~")
print("\nNumber 1 result:")
hello()

print("\nNumber 2 result:")
result = hello2()
print(result)

print("\nNumber 3 result:")
print(product(3,4))

print("\nNumber 4 result:")
print(square(3))

print("\nNumber 5 result:")
print(sum_diff(3, 45))

print("\nNumber 6 result:")
print(second(testList))
print(second(testList2))

print("\nNumber 7 result:")
print(nth(testList, 2))
print(nth(testList2, 6))

print("\nNumber 8 result:")
print(strLen("Hey there, cowboy."))

#####
#####

#If exercises
#1
def allTrue():
    if True:
        print("True was True")
    
    if 198:
        print("Number was True")

    if [1, 3, 4, "ajd", 0]:
        print("List was True")
  
#2      
def allFalse():
    if False:
        print("False was True")
    else:
        print("False was False")
    
    if 0:
        print("Number was True")
    else:
        print("Number was False")

    if []:
        print("List was True")
    else:
        print("List was False")

#3
def bigger(w, k):
    if w > k:
        return (w)
    return(k)

#4
def even(p):
    if p % 2 == 0:
        return (True)
    return (False)

#5
def moreThan10(ls):
    if len(ls) > 10:
        return(True)
    return(False)

#6
def moreThanN(ls, n):
    if len(ls) > n:
        return(True)
    return(False)

#if tests
print("\n\n~~~~~~~~~~~~If exercises~~~~~~~~~~~~")
print("\nNumber 1 result:")
allTrue()
print("\nNumber 2 result:")
allFalse()
print("\nNumber 3 result:")
print(bigger(10,15))
print(bigger(16,-12))
print("\nNumber 4 result:")
print(even(10))
print(even(-15))
print("\nNumber 5 result:")
print(moreThan10(testList))
print(moreThan10(testList2))
print("\nNumber 6 result:")
print(moreThanN(testList, 3))
print(moreThanN(testList2, 37))

#For exercises
#1
def print1to50():
    for n in range(1,51):
        print(n)
        
#2
def printFirst5(ls):
    for i in range(0,5):
        print(ls[i])

#3
def printFirst5_2(ls):
    if len(ls) < 5:
        return(None)
    for i in range(0,5):
        print(ls[i])        
      
#4
def allNum(n):
    myList = []
    for i in range(1, n+1):
        myList.append(i)
    return(myList)
 
#5
def printAll(ls):
    for banana in ls:
        print(banana)
  
#6
def harmonicMean(n):
    if n < 1:
        return(None)
    
    total = 0
    for i in range(1,n+1):
        total += 1/float(i)
        #I use += throughout, this is just short hand for 'add to this'
        #so saying total += 1, is like saying add one to total, or
        #the same as saying: total = total + 1
        #so this line is equivalent to:
        #total = total + 1/float(i)
    return(total)
      
#7
def mean(ls):
    if len(ls) == 0:
        return(None)
    
    total = 0
    for n in ls:
        total += n
        
    return(float(total)/len(ls))
  
#8
def numEven(ls):
    evens = 0
    for n in ls:
        if even(n):
            evens += 1
            
    return(evens)
     
#9
def sum(ls):
    total = 0
    for n in ls:
        total += n
    return(total)
     
#10
def search(ls, n):
    i = 0
    for num in ls:
        if num == n:
            return (i)
        i += 1
    return (None)
        
##Just a note, this last one is not very pythonic. We would normally write this function like this
#Look at the documentation for enumerate, it is a very helpful function
def search2(ls, n):
    for i, num in enumerate(ls):
        if num == n:
            return (i)
    return(None)
        
#For tests
print("\n\n~~~~~~~~~~~~For exercises~~~~~~~~~~~~")
print("\nNumber 1 result:")
print1to50()
print("\nNumber 2 result:")
printFirst5(testList)
print("\nNumber 3 result:")
printFirst5_2(testList)
printFirst5_2([1,2,3])
print("\nNumber 4 result:")
print(allNum(14))
print("\nNumber 5 result:")
printAll(testList2)
print("\nNumber 6 result:")
print(harmonicMean(5))
print(harmonicMean(26))
print("\nNumber 7 result:")
print(mean(testList2))
print(mean([]))
print("\nNumber 8 result:")
print(numEven(testList2))
print(numEven([]))
print("\nNumber 9 result:")
print(sum(testList2))
print(sum([]))
print("\nNumber 10 result:")
print(search(testList2, 2))
print(search(testList2, 345))
print(search2(testList2, 2))
print(search2(testList2, 345))
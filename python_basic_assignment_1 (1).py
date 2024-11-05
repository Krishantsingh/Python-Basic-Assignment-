
1. Explain the key features of Python that make it a popular choice for programming.

  =There are several key features of python that make it a popular choice for programming. Some of them are as folow,
- A lot of libraries
- Automation
- Easy to learn
- Huge active community

2. Describe the role of predefined keywords in Python and provide examples of
   how they are used in a program.

   =  Keywords are predifined words that hold a specific meaning and have specific
   purpose.predefined keywords are reserved words that have special meanings and cannot be used as identifiers.

   Some major roles of predifined keywords in python are as follow,
   
   i.Control Flow: Keywords like if, else, elif, for, while, and break are used to control the flow of execution in a program, allowing for decision-making and iteration.
   
   for example,
    a=4
    b=7
    if b>a:
        print("b is greater than a")
    elif a+b>10:
        print("The sum of a and b is greatre than 10")
    else:
        print("None of the above")

3. Compare and contrast mutable and immutable objects in Python with examples.

  = Mutable Objects:
  -objects or container whose value can be changed after they are created are
  called as Mutable objects. List is a type of mutable Objects.

  Example:
a=[1,2,3.5,"Ajay"]
#if we want to change "Ajay" with "Bijay" then,
a[3]="Bijay"
print(a)

     Immutable Objects:
    The objects or container whose value cant't be changed after they are created are called as Immutable Objects. string is an immutable object.
     Example:
b="Ram"
#if we have to change 'a' in "Ram" with 3 then we can't do this
b[1]=3
print(b)

#here we got an error

4. Discuss the different types of operators in Python and provide examples of how they are used.

   -There are different types of operators in python. Some of them are as follow,
  
  i. Arithmatic Operators:

  -This operator is used to perform Additio, Subtraction, Division and Multiplication in python.This operator are +, -, *, / etc.
  
  example:
a=1
b=3
a+b

a-b

a*b

a/b



ii. Modulos Operator:
 - -This operator is used to calculate the remainder of the division between two numbers. It is  represented by % this sign.

 example,
a=20
b=3
a%b

iii. Floor Operator:

   - This operatpr is used to get the value at lower side of a float value. It
     is represented by (//) this sign.

     example:

a=21
b=2
a/b

a//b

iv. Comparison Operator:
   
  -This operator returns a boolean value as a return of comparison of two value. This operaor are ==, !=, <=, >= etc.

  example:
a=2
b=3
a==b

a!=b

b>=a

a<=b

v. Assignment Operator:
  - This operator is used to assign some value to any variable. Such as +=, -=, *=, /= etc.

  example:

a=4
a+=2
a

a-=1
a

a*=2
a

5.  Explain the concept of type casting in Python with examples.

  - The process of changing the data type of a value/object is known is Type casting. While executing or computing using operator, there can be mismatch between data type. So type casting is used to match convert the data type into another required data type.

   it is of two types:

     i. Implicit Type Casting:
  
     -In this type casting, we don't need to define variable data type, Python itself understand the data type.
   

     example:
#here we dot't need to change the data type
a=2
b=3.5
a+b

ii. Explicit Type Casting:

  -In this type casting we have to define variabe data type to perform any function.

  Example
#here we have to define data type of variable
a=2
b="3.5"
a+b

a+float(b)


6.  How do conditional statements work in Python? Illustrate with examples.
  
   = Conditional Statement helps us to code decision based on some  
     precondition. Some of conditional statements are if statement, elif statement and else statement.

     Example:
a=1
b=5
if a>b:
  print("a is greater than b")
elif a==b:
  print("a is equals to b")
else:
  print("a is less than b")
7. Describe the different types of loops in Python and their use cases with
   examples.
   = Loop is construct that aloows you to execute a block of code repeatedly. It is of two types, They are as follow;
   1. While loop:
   - It repeatedly execute a block of code untill a condition is meet.
   
     example:
n=7
i=1
while i<n:
  print(i)
  i=i+1
   2. For loop:
       -  It iterate over a sequence of element and execute a block of code for each item in that sequence. Some of its example are as follow,

       Example:

for i in "pwskills":
  print(i)

l=[1,2,3,4.66,"Bijay"]
for i in l:
  if l==4:
    continue
  print(i)
else:
  print("this is else")


Fraction Class
In this lab session, you'll code a new Python class to represent Fraction objects.

The main topics you'll practice during this lab are:

Defining magic and non-magic methods.
Creating methods that generate new objects.
Creating methods that modify the caller object (a.k.a mutators).
Read the instructions carefully and ask for clarification from your TA/LA if necessary.

IMPORTANT: Remember to use type hinting in your method headers specifying the argument types and the return type.

## Coding Step 1: Class definition and constructor method __init__
Define a new Python class named Fraction.

As you already know, fractions have 2 parts: the numerator and the denominator.

The class should then have 2 integer attributes attributes "num" and "den".

For this particular exercise, we won't deal with negative fractions. Hence, neither the numerator nor the denominator can be < 0.

Also remember that division by 0 is undefined. Thus, the denominator cannot be <= 0.

When coding your constructor method, make sure you check for these cases and return an appropriate error message.

Make sure to test your code constantly. At this point, you should be able to execute code like this:

<img width="843" alt="Screen Shot 2022-04-04 at 11 20 44 PM" src="https://user-images.githubusercontent.com/86554954/161691342-ca1b36e0-fdc2-4387-8ad6-2dea4b66e6a6.png">

## Coding Step 2: __str__ and __repr__ magic methods
The __str__ magic method is used whenever you print an object. For our Fraction objects, we want the output of the __str__ method to be a string of the numerator and the denominator separated by a forward slash, like so:

<img width="548" alt="Screen Shot 2022-04-04 at 11 23 40 PM" src="https://user-images.githubusercontent.com/86554954/161691743-30a75008-9f1b-4189-a74d-9eba2f1011a4.png">

The __repr__ magic method is used by the debugger and should return a string that looks like a call to the constructor of the class. For our Fraction object, it should look like this:

<img width="548" alt="Screen Shot 2022-04-04 at 11 24 47 PM" src="https://user-images.githubusercontent.com/86554954/161691899-5d77e481-b5b3-4f32-9f1d-453a57869570.png">


## Coding Step 3: __mul__ and __add__ magic methods
Fraction multiplication is pretty straight forward: multiply both numerators by each other and both denominators by each other:


<img width="177" alt="Screen Shot 2022-04-04 at 11 25 13 PM" src="https://user-images.githubusercontent.com/86554954/161691961-22d16bc5-f9fb-47cc-a2ad-bcd7c321cb08.png">

The fraction __mul__ magic method should then receive a second Fraction object as an argument and perform the multiplication operation for fractions.

## IMPORTANT: This method should create a NEW Fraction object and NOT modify the original fractions:

<img width="554" alt="Screen Shot 2022-04-04 at 11 25 52 PM" src="https://user-images.githubusercontent.com/86554954/161692050-63fd8bc2-fdda-4c85-a007-80b15f5fc8b9.png">

For fraction addition, the resulting denominator is again the multiplication of both the original denominators. The resulting numerator is obtained by multiplying each numerator by its counterpart denominator and then adding them together like so:

<img width="330" alt="Screen Shot 2022-04-04 at 11 26 29 PM" src="https://user-images.githubusercontent.com/86554954/161692131-c27a0bbb-cdea-4efc-8431-23a31ffb87b6.png">

Same as with __mul__, the __add__ magic method must create a NEW Fraction object:

<img width="552" alt="Screen Shot 2022-04-04 at 11 27 00 PM" src="https://user-images.githubusercontent.com/86554954/161692178-7d2e4217-9daf-4133-9525-79dc6a7a994b.png">

## Coding Step 4: The Simplify method
Finally, we'll code a 'simplify' method that reduces a fraction to its simplest terms. For example:

<img width="309" alt="Screen Shot 2022-04-04 at 11 29 29 PM" src="https://user-images.githubusercontent.com/86554954/161692575-2ced5b50-7174-4177-9af2-856c65af7a4d.png">

To achieve this we simply must find the Greatest Common Divisor (GCD) of both the numerator and denominator in the fraction.

Here's some code that finds the gcd for two numbers:

<img width="552" alt="Screen Shot 2022-04-04 at 11 28 55 PM" src="https://user-images.githubusercontent.com/86554954/161692494-a1663d99-0c95-4faa-b8fc-ef8c00d80210.png">

Once you have the GCD, simplifying the fraction means dividing both the numerator and denominator by the GCD. For example:

<img width="309" alt="Screen Shot 2022-04-04 at 11 30 31 PM" src="https://user-images.githubusercontent.com/86554954/161692709-d0724e5f-8c95-4df7-96c6-a7aa25091b03.png">


## IMPORTANT: the simplify method DOES NOT create a new object, instead it MODIFIES the object that calls it:

<img width="552" alt="Screen Shot 2022-04-04 at 11 28 34 PM" src="https://user-images.githubusercontent.com/86554954/161692430-b3b84df0-0271-4693-93ea-8b6171ba1a35.png">


## Coding Step 5: Integrate simplify into __init__, __add__, and __mul__
Modify the code for __init__, __add__, and __mul__ so that only minimal fractions are returned:

<img width="552" alt="Screen Shot 2022-04-04 at 11 28 05 PM" src="https://user-images.githubusercontent.com/86554954/161692355-1a188d2f-bbe5-47fd-b98a-4c5005deafec.png">

## Upload your code
When you finish, upload a file named "Fraction.py" with your code to Canvas.

Remember, it's ok if you do not finish the full exercise. Simply upload whatever you managed to complete with your group.

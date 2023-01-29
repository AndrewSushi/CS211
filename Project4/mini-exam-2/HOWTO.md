# Mini-exam 2 HOWTO

Nile.com is a retailer named after a major river.  It sells 
physical and electronic books and fine tea; in the future 
it may also sell electronics.  Although pythons
are native to South America, and the Nile is in Africa,
Nile.com has decided to reimplement its e-commerce system in Python. 
This Python implementation is not very complete yet, but you will
write and test some critical code for calculating base cost (before 
shipping) and shipping cost for the items in a shopping cart. 

## Items

Each kind of item that Nile.com sells is represented by a subclass
of class `Item`.  There is a subclass `PaperBook` for physical books,
a subclass `EBook` for electronic books, and a subclass `Tea` for 
tea.  Each is somewhat different in its internal representation, 
but each subclass of `Item` must implement the following methods
as specified in the abstract class

* `cost(self) -> float` returns the cost of an item.  For physical
   and electronic books, this is just the price of the book.  For tea,
   it is the number of grams of tea times the price per gram. 
  
* `shipping_weight(self) -> int` returns the shipping weight of
   of the item.  Each physical book has a weight that is set by its 
  constructor.  The weight of tea is the amount specified in its
  constructor.  We consider electronic books to have zero weight,
  because what we actually sell are unlock codes that we transmit
  by email. 
  
You must implement these. 

## Shipping Rates

I have implemented a class `RateTable` that can be used to calculate
the total shipping cost for an order, which could include a mix of
electronic books, physical books, and tea.  Shipping cost is based
on the *total* weight of items in the shopping cart, because we put
all the physical items in a single box to ship them.  Any virtual
goods, like electronic book download codes, are transmitted 
electronically instead. 

For example, let's say that USPS charges $0.75 for each gram up to
10, then $0.50 for each of the next 100 grams.  Then shipping 15 
grams would cost $10: $7.50 for the first 10 grams, and $2.50 
for the remaining 5 grams. This calculation has been implemented for 
you in class `RateTable`.  

A rate table can also determine whether a package is too heavy to be 
shipped by a particular shipper, but for simplicity we will ignore
the `can_ship` method and assume that our boxes are not heavy enough 
to be a problem. 

## Shopping Carts 

A shopping cart holds a list of items to be purchased.  There are two
important methods that you must implement: 

*  `base_cost(self) -> float` returns the total of the price of
    items in the cart. 
   
*  `shipping(self, rates: RateTable) -> float` returns the 
    total shipping cost for items in the cart, based on the rates
    in the provided rate table.  Note that you must determine the
    total weight of items in the cart, rather than calculating a
    shipping cost for each individual item.  Generally it is cheapest
    to ship several items in the same box. We do not include a 
    weight for the box itself; you can treat it as if the box had
    no weight.)
   
It is very important to implement `base_cost` and `shipping` in
a general way that does *not* check the type of each item.  If 
Nile.com begins shipping televisions and earbuds next year, creating
new concrete subclasses of `Item` for these new products, your methods
`base_cost` and `shipping` must continue to work without change, because
they should depend only on each item in the cart being some subclass
of `Item`.   Also you must not modify the abstract class `Item`.  

## Reminders and partial credit

Remember to turn in *working code* even if you cannot pass all test
cases. I cannot debug non-working code fast enough to grade and return
mini-exams in a timely manner, so non-working code earns very few 
points.  Consider saving a working version of your code before you
try any major revisions. 

Points for effort and correctness are allocated in 
proportion to the project grade rubric at 
[https://classes.cs.uoregon.edu/21S/cis211/]
(https://classes.cs.uoregon.edu/21S/cis211/)  (open the "grade rubrics
and scales" details), except that weight for coding standards and
fluency is reduced considering the limited time for revision. 

For code that runs (executes all test cases) but fails some tests,
partial credit will be awarded as follows: 

* Up to 5 points for methods `cost` and `shipping_weight`
* Up to 5 points for method `base_cost`
* Up to 10 points for method `shipping`









Explain your project in 2 minutes
---------------------
i have built a clinical management system using oops concept
with python as my frontend and backend and mysql as database.

first i created seperate classes for each entity like doctor ,receptionist,etc.
    
second i created objects based on the user login.if doctor 
login then object for doctor class will be created .same for receptionist...
i used constructor to initialze the objects.

Encapsulation is the process of binding data and the methods that operate
on that data into a single class while hiding the internal details from 
outside access In my project, I implemented encapsulation in the Login class by 
declaring username and password as private attributes using double underscores (__)
and accessing them through getter and setter methods.
    

Inheritance is the process by which one class inherits the attributes
and methods of another class, allowing code reuse and establishing a parent-child relationship.
I used inheritance by creating a Person parent class and deriving Doctor and Staff classes from it.


I used abstraction by creating an abstract class Person using Python's abc module. 
The Person class contains an abstract method dashboard(), which hides the implementation
 details and forces all child classes such as Doctor and Staff to provide their own implementation
of the dashboard method.

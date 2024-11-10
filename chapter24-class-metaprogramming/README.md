Classes are first-class objects in Python, so a function can be used to create a 
new class at any time without using the class keyword

Class decorators are designed to inspect, change and even replace the decorated class
with another class

Metaclasses let you create whole new categories of classes with special traits, such as 
the abstract base classes we've already seen

From [PEP 487 - Simpler customization of class creation](https://peps.python.org/pep-0487/): 

``` 
While there are many possible ways to use a metaclass, the vast majority of use cases falls into just three categories: some initialization code running after class creation, the initialization of descriptors and keeping the order in which class attributes were defined.
```


Note: Metaclasses should not be something used for application code. However, if you're writing a 
framework, this might make sense

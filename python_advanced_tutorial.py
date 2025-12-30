"""
PYTHON ADVANCED FEATURES TUTORIAL
==================================

This tutorial covers advanced Python features including decorators and special methods.
Designed for beginners who want to level up their Python skills.

Topics Covered:
1. Basic Decorators
2. Property Decorators (@property, @setter, @deleter)
3. Static Methods (@staticmethod)
4. Class Methods (@classmethod)
5. Abstract Methods (@abstractmethod)
6. Function Overloading (@overload)
7. Final Classes and Methods (@final)
8. Override Decorator (@override)
"""

# ============================================================================
# SECTION 1: BASIC DECORATORS
# ============================================================================

print("=" * 60)
print("SECTION 1: BASIC DECORATORS")
print("=" * 60)

"""
What is a Decorator?
--------------------
A decorator is a function that takes another function and extends its behavior
without explicitly modifying it. Think of it like gift wrapping - the gift 
stays the same, but you add something extra around it.
"""


def my_decorator(func):
    """
    A simple decorator that adds behavior before and after a function call.
    
    Args:
        func: The function to be decorated
        
    Returns:
        wrapper: A new function that wraps the original function
    """
    def wrapper():
        print("🎁 Something is happening before the function is called.")
        func()
        print("🎁 Something is happening after the function is called.")
    return wrapper


@my_decorator
def say_hello():
    """A simple function that will be decorated."""
    print("👋 Hello!")


# Using the decorator
print("\nExample 1: Basic Decorator")
say_hello()


def repeat_three_times(func):
    """
    A decorator that repeats a function call three times.
    
    Args:
        func: The function to be repeated
        
    Returns:
        wrapper: A function that calls the original three times
    """
    def wrapper(*args, **kwargs):
        for i in range(3):
            print(f"  Call #{i+1}:")
            func(*args, **kwargs)
    return wrapper


@repeat_three_times
def greet(name):
    """Greet someone by name."""
    print(f"  Hello, {name}!")


print("\nExample 2: Decorator with Arguments")
greet("Alice")


# ============================================================================
# SECTION 2: PROPERTY DECORATORS (@property, @setter, @deleter)
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 2: PROPERTY DECORATORS")
print("=" * 60)

"""
What are Property Decorators?
------------------------------
Property decorators allow you to define methods that can be accessed like 
attributes. This is useful for:
- Data validation
- Computed attributes
- Controlling access to private data
"""


class Person:
    """
    A class demonstrating property decorators.
    
    Properties allow us to add validation and logic when getting/setting
    attributes, while still using simple attribute syntax.
    """
    
    def __init__(self, name, age):
        """
        Initialize a Person object.
        
        Args:
            name (str): The person's name
            age (int): The person's age
        """
        self.__name = name  # Private attribute (convention: starts with __)
        self.__age = age
    
    @property
    def name(self):
        """
        Getter for name property.
        
        The @property decorator allows us to access _name like a regular
        attribute (person.name) instead of calling a method (person.name()).
        
        Returns:
            str: The person's name
        """
        print("  📖 Getting name...")
        return self.__name
    
    @name.setter
    def name(self, value):
        """
        Setter for name property with validation.
        
        This is called when you try to assign a value: person.name = "John"
        We can add validation logic here.
        
        Args:
            value (str): The new name value
            
        Raises:
            ValueError: If name is empty or not a string
        """
        print(f"  ✏️  Setting name to: {value}")
        if not isinstance(value, str):
            raise ValueError("Name must be a string!")
        if len(value.strip()) == 0:
            raise ValueError("Name cannot be empty!")
        self.__name = value
    
    @name.deleter
    def name(self):
        """
        Deleter for name property.
        
        This is called when you use: del person.name
        Useful for cleanup operations.
        """
        print("  🗑️  Deleting name...")
        self.__name = None
    
    @property
    def age(self):
        """
        Getter for age property.
        
        Returns:
            int: The person's age
        """
        return self.__age
    
    @age.setter
    def age(self, value):
        """
        Setter for age property with validation.
        
        Args:
            value (int): The new age value
            
        Raises:
            ValueError: If age is negative or not an integer
        """
        if not isinstance(value, int):
            raise ValueError("Age must be an integer!")
        if value < 0:
            raise ValueError("Age cannot be negative!")
        if value > 150:
            raise ValueError("Age seems unrealistic!")
        self.__age = value
    
    @property
    def is_adult(self):
        """
        A computed property (read-only).
        
        This property doesn't have a setter - it's calculated from age.
        This demonstrates how properties can compute values on-the-fly.
        
        Returns:
            bool: True if person is 18 or older
        """
        return self.__age >= 18


# Using property decorators
print("\nExample 3: Using @property")
person = Person("Bob", 25)
print(f"Name: {person.name}")  # Calls the getter
print(f"Age: {person.age}")
print(f"Is adult? {person.is_adult}")

print("\nExample 4: Using @setter")
person.name = "Robert"  # Calls the setter
person.age = 26

print("\nExample 5: Property validation")
try:
    person.age = -5  # This will raise an error
except ValueError as e:
    print(f"  ❌ Error: {e}")

print("\nExample 6: Using @deleter")
del person.name  # Calls the deleter
print(f"Name after deletion: {person.name}")


# ============================================================================
# SECTION 3: STATIC METHODS (@staticmethod)
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 3: STATIC METHODS")
print("=" * 60)

"""
What is @staticmethod?
----------------------
A static method is a method that belongs to a class but doesn't access
or modify the class or instance. It's like a regular function, but it's
organized inside the class because it's related to the class's purpose.

Use @staticmethod when:
- The method doesn't need access to instance (self) or class (cls)
- The method is a utility function related to the class
"""


class MathOperations:
    """A class containing math utility functions."""
    
    @staticmethod
    def add(x, y):
        """
        Add two numbers.
        
        This is a static method because it doesn't need access to
        any instance or class variables - it just performs a calculation.
        
        Args:
            x (float): First number
            y (float): Second number
            
        Returns:
            float: Sum of x and y
        """
        return x + y
    
    @staticmethod
    def multiply(x, y):
        """
        Multiply two numbers.
        
        Args:
            x (float): First number
            y (float): Second number
            
        Returns:
            float: Product of x and y
        """
        return x * y
    
    @staticmethod
    def is_even(number):
        """
        Check if a number is even.
        
        Args:
            number (int): Number to check
            
        Returns:
            bool: True if even, False if odd
        """
        return number % 2 == 0


# Using static methods
print("\nExample 7: Static Methods")
print(f"5 + 3 = {MathOperations.add(5, 3)}")
print(f"5 * 3 = {MathOperations.multiply(5, 3)}")
print(f"Is 4 even? {MathOperations.is_even(4)}")
print(f"Is 7 even? {MathOperations.is_even(7)}")

# You can also call static methods on instances (but it's not common)
math_ops = MathOperations()
print(f"Instance call: 10 + 5 = {math_ops.add(10, 5)}")


# ============================================================================
# SECTION 4: CLASS METHODS (@classmethod)
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 4: CLASS METHODS")
print("=" * 60)

"""
What is @classmethod?
---------------------
A class method receives the class itself as the first argument (cls)
instead of an instance (self). It can access and modify class-level data.

Use @classmethod for:
- Alternative constructors (factory methods)
- Methods that need to access or modify class variables
"""


class Pizza:
    """A class demonstrating class methods for alternative constructors."""
    
    # Class variable (shared by all instances)
    total_pizzas_made = 0
    
    def __init__(self, ingredients):
        """
        Initialize a Pizza with given ingredients.
        
        Args:
            ingredients (list): List of ingredient strings
        """
        self.ingredients = ingredients
        Pizza.total_pizzas_made += 1
    
    def __repr__(self):
        """String representation of the pizza."""
        return f"Pizza({', '.join(self.ingredients)})"
    
    @classmethod
    def margherita(cls):
        """
        Factory method to create a Margherita pizza.
        
        This is a class method that acts as an alternative constructor.
        Instead of Pizza(['tomato', 'mozzarella', 'basil']), you can
        simply call Pizza.margherita().
        
        Returns:
            Pizza: A Margherita pizza instance
        """
        return cls(['tomato sauce', 'mozzarella', 'basil'])
    
    @classmethod
    def pepperoni(cls):
        """
        Factory method to create a Pepperoni pizza.
        
        Returns:
            Pizza: A Pepperoni pizza instance
        """
        return cls(['tomato sauce', 'mozzarella', 'pepperoni'])
    
    @classmethod
    def get_total_pizzas(cls):
        """
        Get the total number of pizzas created.
        
        This class method accesses the class variable total_pizzas_made.
        
        Returns:
            int: Total number of pizzas created
        """
        return cls.total_pizzas_made


# Using class methods
print("\nExample 8: Class Methods as Factory Methods")
pizza1 = Pizza.margherita()
pizza2 = Pizza.pepperoni()
pizza3 = Pizza(['BBQ sauce', 'chicken', 'onions'])

print(f"Pizza 1: {pizza1}")
print(f"Pizza 2: {pizza2}")
print(f"Pizza 3: {pizza3}")
print(f"Total pizzas made: {Pizza.get_total_pizzas()}")


# ============================================================================
# SECTION 5: ABSTRACT METHODS (@abstractmethod)
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 5: ABSTRACT METHODS")
print("=" * 60)

"""
What is @abstractmethod?
------------------------
An abstract method is a method declared in a base class that must be
implemented by any concrete (non-abstract) subclass. It's like a contract.

Use @abstractmethod when:
- You want to define an interface that subclasses must follow
- You want to prevent instantiation of the base class
- You want to ensure certain methods are implemented in subclasses
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class for animals.
    
    This class cannot be instantiated directly. Any subclass must
    implement all abstract methods.
    """
    
    def __init__(self, name):
        """
        Initialize an animal with a name.
        
        Args:
            name (str): The animal's name
        """
        self.name = name
    
    @abstractmethod
    def make_sound(self):
        """
        Abstract method for making a sound.
        
        Every animal subclass must implement this method.
        This ensures all animals can make a sound, but each
        animal makes their own unique sound.
        """
        pass
    
    @abstractmethod
    def move(self):
        """
        Abstract method for movement.
        
        Every animal subclass must implement this method.
        """
        pass
    
    def sleep(self):
        """
        Concrete method (not abstract).
        
        This method has an implementation and doesn't need to be
        overridden by subclasses (but it can be).
        """
        print(f"  {self.name} is sleeping... 😴")


class Dog(Animal):
    """Concrete implementation of Animal for dogs."""
    
    def make_sound(self):
        """Dogs bark."""
        print(f"  {self.name} says: Woof! Woof! 🐕")
    
    def move(self):
        """Dogs run."""
        print(f"  {self.name} is running on four legs! 🏃")


class Bird(Animal):
    """Concrete implementation of Animal for birds."""
    
    def make_sound(self):
        """Birds chirp."""
        print(f"  {self.name} says: Tweet! Tweet! 🐦")
    
    def move(self):
        """Birds fly."""
        print(f"  {self.name} is flying in the sky! 🦅")


# Using abstract methods
print("\nExample 9: Abstract Methods")
dog = Dog("Buddy")
dog.make_sound()
dog.move()
dog.sleep()

print()
bird = Bird("Tweety")
bird.make_sound()
bird.move()
bird.sleep()

print("\nExample 10: Cannot instantiate abstract class")
try:
    # This will raise an error because Animal is abstract
    animal = Animal("Generic")
except TypeError as e:
    print(f"  ❌ Error: {e}")


# ============================================================================
# SECTION 6: FUNCTION OVERLOADING (@overload)
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 6: FUNCTION OVERLOADING")
print("=" * 60)

"""
What is @overload?
------------------
Python doesn't have traditional function overloading like Java or C++.
The @overload decorator is used for type hints to indicate that a function
can accept different combinations of argument types.

Note: @overload only provides type hints for static type checkers (like mypy).
You still need to write one actual implementation.
"""

from typing import overload, Union


class Calculator:
    """A calculator demonstrating function overloading with type hints."""

    @overload
    def add(self, a: int, b: int) -> int:
        ...

    @overload
    def add(self, a: int, b: int, c: int) -> int:
        ...

    def add(self, a: int, b: int, c: int | None = None) -> int:
        if c is None:
            return a + b
        return a + b + c
    
    @overload
    def process(self, value: int) -> int:
        """Process an integer."""
        ...
    
    @overload
    def process(self, value: str) -> str:
        """Process a string."""
        ...
    
    def process(self, value: Union[int, str]) -> Union[int, str]:
        """
        Process a value (actual implementation).
        
        The @overload decorators above are just type hints.
        This is the actual implementation that handles both cases.
        
        Args:
            value: Either an int or a str
            
        Returns:
            If int: returns value * 2
            If str: returns value in uppercase
        """
        if isinstance(value, int):
            print(f"  Processing integer: {value}")
            return value * 2
        elif isinstance(value, str):
            print(f"  Processing string: {value}")
            return value.upper()
        else:
            raise TypeError("Value must be int or str")


# Using overloaded functions
print("\nExample 11: Function Overloading")
calc = Calculator()
result1 = calc.process(5)
print(f"  Result: {result1}")

result2 = calc.process("hello")
print(f"  Result: {result2}")


# ============================================================================
# SECTION 7: FINAL CLASSES AND METHODS (@final)
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 7: FINAL DECORATOR")
print("=" * 60)

"""
What is @final?
---------------
The @final decorator indicates that a class should not be subclassed,
or a method should not be overridden. This is a type checking hint
for static type checkers like mypy.

Note: Python won't prevent you from subclassing or overriding at runtime,
but type checkers will warn you.
"""

from typing import final


class BaseGame:
    """A base game class with final and non-final methods."""
    
    def start(self):
        """Start the game - can be overridden by subclasses."""
        print("  🎮 Game starting...")
    
    @final
    def calculate_score(self, points: int) -> int:
        """
        Calculate score - marked as final.
        
        This method should NOT be overridden by subclasses because
        the scoring logic must remain consistent.
        
        Args:
            points (int): Base points earned
            
        Returns:
            int: Final score with bonus
        """
        bonus = 100
        return points + bonus
    
    def end(self):
        """End the game - can be overridden by subclasses."""
        print("  🏁 Game over!")


class MyGame(BaseGame):
    """A specific game implementation."""
    
    def start(self):
        """Override start method (this is allowed)."""
        print("  🎮 MyGame starting with custom intro!")
    
    # If you uncomment this, a type checker would warn you:
    # def calculate_score(self, points: int) -> int:
    #     # ❌ Type checker warning: Cannot override final method
    #     return points * 2


@final
class SecretAlgorithm:
    """
    A class marked as final - should not be subclassed.
    
    Use @final on classes when you don't want them to be extended,
    perhaps for security or consistency reasons.
    """
    
    def process(self):
        """Process data with secret algorithm."""
        print("  🔒 Processing with secret algorithm...")


# Using final decorator
print("\nExample 12: Final Methods")
game = MyGame()
game.start()
score = game.calculate_score(50)
print(f"  Final score: {score}")
game.end()

print("\nExample 13: Final Class")
secret = SecretAlgorithm()
secret.process()

# If you uncomment this, a type checker would warn you:
# class MySecretAlgorithm(SecretAlgorithm):  # ❌ Type checker warning
#     pass


# ============================================================================
# SECTION 8: OVERRIDE DECORATOR (@override)
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 8: OVERRIDE DECORATOR")
print("=" * 60)

"""
What is @override?
------------------
The @override decorator (available in Python 3.12+) explicitly marks
that a method is intended to override a parent class method. This helps
catch errors where you think you're overriding a method but actually aren't
(due to typos or signature mismatches).

Note: If your Python version is < 3.12, you can use typing_extensions.
"""

try:
    from typing import override
except ImportError:
    # For Python < 3.12, use typing_extensions
    from typing_extensions import override


class Shape:
    """Base class for shapes."""
    
    def area(self) -> float:
        """
        Calculate area of the shape.
        
        Returns:
            float: The area
        """
        return 0.0
    
    def perimeter(self) -> float:
        """
        Calculate perimeter of the shape.
        
        Returns:
            float: The perimeter
        """
        return 0.0


class Rectangle(Shape):
    """Rectangle shape implementation."""
    
    def __init__(self, width: float, height: float):
        """
        Initialize a rectangle.
        
        Args:
            width (float): Width of the rectangle
            height (float): Height of the rectangle
        """
        self.width = width
        self.height = height
    
    @override
    def area(self) -> float:
        """
        Calculate rectangle area.
        
        The @override decorator tells type checkers: "I'm intentionally
        overriding the parent's area method." If there was no area method
        in the parent, the type checker would warn you.
        
        Returns:
            float: Width times height
        """
        return self.width * self.height
    
    @override
    def perimeter(self) -> float:
        """
        Calculate rectangle perimeter.
        
        Returns:
            float: 2 * (width + height)
        """
        return 2 * (self.width + self.height)


class Circle(Shape):
    """Circle shape implementation."""
    
    def __init__(self, radius: float):
        """
        Initialize a circle.
        
        Args:
            radius (float): Radius of the circle
        """
        self.radius = radius
    
    @override
    def area(self) -> float:
        """
        Calculate circle area.
        
        Returns:
            float: π * radius²
        """
        import math
        return math.pi * self.radius ** 2
    
    @override
    def perimeter(self) -> float:
        """
        Calculate circle circumference.
        
        Returns:
            float: 2 * π * radius
        """
        import math
        return 2 * math.pi * self.radius


# Using override decorator
print("\nExample 14: Override Decorator")
rect = Rectangle(5, 3)
print(f"Rectangle (5x3):")
print(f"  Area: {rect.area():.2f}")
print(f"  Perimeter: {rect.perimeter():.2f}")

print()
circle = Circle(4)
print(f"Circle (radius=4):")
print(f"  Area: {circle.area():.2f}")
print(f"  Perimeter: {circle.perimeter():.2f}")


# ============================================================================
# BONUS SECTION: COMBINING DECORATORS
# ============================================================================

print("\n" + "=" * 60)
print("BONUS: COMBINING MULTIPLE DECORATORS")
print("=" * 60)

"""
You can stack multiple decorators on the same function or method.
They are applied from bottom to top (closest to the function first).
"""


def multiply_decorator(func):
    def wrapper(x: int):
        return func(x) * 2
    return wrapper


def other_decorator(func):
    def wrapper(x: int):
        return func(x) * 4
    return wrapper


@multiply_decorator
@other_decorator
def calculate(x: int):
    return x * 2


print(calculate(10))

# ============================================================================
# SUMMARY AND BEST PRACTICES
# ============================================================================

print("\n" + "=" * 60)
print("SUMMARY AND BEST PRACTICES")
print("=" * 60)

print("""
📚 What We Learned:

1. BASIC DECORATORS
   - Functions that modify other functions
   - Use: Adding functionality without changing original code

2. @property, @setter, @deleter
   - Access methods like attributes
   - Use: Data validation, computed properties

3. @staticmethod
   - Methods that don't need instance or class access
   - Use: Utility functions related to a class

4. @classmethod
   - Methods that receive the class as first argument
   - Use: Alternative constructors, accessing class variables

5. @abstractmethod
   - Methods that must be implemented by subclasses
   - Use: Defining interfaces, ensuring implementation

6. @overload
   - Type hints for functions with multiple signatures
   - Use: Better type checking and IDE support

7. @final
   - Prevent overriding methods or subclassing
   - Use: Ensuring critical methods remain unchanged

8. @override
   - Explicitly mark overridden methods
   - Use: Catch errors in method overriding

💡 Best Practices:
- Use @property for data validation and computed values
- Use @staticmethod for utility functions
- Use @classmethod for alternative constructors
- Use @abstractmethod to define clear interfaces
- Use @override to make intentions clear
- Don't overuse decorators - keep code readable
- Add clear docstrings to explain decorator purposes

🎯 When to Use What:
- Need validation? → @property + @setter
- Need utility function? → @staticmethod
- Need factory method? → @classmethod
- Need interface/contract? → @abstractmethod
- Need type hints? → @overload
- Need to prevent override? → @final
- Overriding parent method? → @override

Happy coding! 🐍✨
""")

print("\n" + "=" * 60)
print("END OF TUTORIAL")
print("=" * 60)


#1
"""class Watch:
    def __init__(self, brand, cost):
        self.brand=brand
        self.cost=cost
my_watch=Watch("Seiko", "58k")
print(my_watch.brand)
print(my_watch.cost)"""

#2
"""class Watch :
    def __init__(self, brand, cost):
        self.brand=brand
        self.cost=cost
    def full_name(self):
        return f"{self.brand} {self.cost}"
my_watch=Watch("Seiko", "58k")
print(my_watch.brand)
print(my_watch.cost)
print(my_watch.full_name())"""

#3
"""class ElectricCar(Watch):
    def __init__(self, battery_size, brand, cost):
        super().__init__(brand, cost)
        self.battery_size=battery_size

my_car=ElectricCar("Seiko", "58k", "20kMhz")
print(my_car.full_name())"""

#4
# Base class
"""class Animal:
    def __init__(self, name):
        self.name = name  # Attribute defined in the base class
    
    def display_info(self):
        print(f"Animal Name: {self.name}")

# Child class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Passing name to the base class
        self.breed = breed  # Additional attribute specific to the child class
    
    def display_info(self):
        # Overriding the method to include child class details
        super().display_info()
        print(f"Breed: {self.breed}")

# Taking input from the user
dog_name = input("Enter the dog's name: ")
dog_breed = input("Enter the dog's breed: ")

# Creating an object of the child class
my_dog = Dog(dog_name, dog_breed)

# Displaying the data using the method
my_dog.display_info()"""

#5

# Base class
"""class StringProcessor:
    def __init__(self, a):
        self.a = a  # Attribute to store the input string
    
    def display_string(self):
        print(f"String: {self.a}")

# Child class
class PalindromeChecker(StringProcessor):
    def __init__(self, a):
        super().__init__(a)  # Initialize the base class attribute
    
    def is_palindrome(self):
        # Remove non-alphanumeric characters and convert to lowercase for uniformity
        cleaned_string = ''.join(filter(str.isalnum, self.a)).lower()
        return cleaned_string == cleaned_string[::-1]

# Taking input from the user
input_string = input("Enter a string: ")

# Creating an object of the child class
checker = PalindromeChecker(input_string)

# Displaying the string
checker.display_string()

# Checking and displaying whether it is a palindrome
if checker.is_palindrome():
    print(f"The string '{checker.a}' is a palindrome!")
else:
    print(f"The string '{checker.a}' is not a palindrome.") """

#6

class Payment:
    def __init__(self, amount: float):
        """
        Initialize the Payment object with the total amount.
        :param amount: Total payment amount in float.
        """
        self.amount = amount

    def calculate_total(self) -> float:
        """
        Calculate the total payment amount.
        :return: Total amount without any additional fee.
        """
        return self.amount


class CreditCardPayment(Payment):
    def calculate_total(self) -> float:
        """
        Override the calculate_total method to include a 3.5% processing fee.
        :return: Total payment amount including the processing fee.
        """
        processing_fee = self.amount * 0.035
        return self.amount + processing_fee


# Example Usage
if __name__ == "__main__":
    # Cash Payment
    cash_payment = Payment(1000)
    print(f"Total for cash payment: ${cash_payment.calculate_total():.2f}")

    # Credit Card Payment
    credit_card_payment = CreditCardPayment(100)
    print(f"Total for credit card payment: ${credit_card_payment.calculate_total():.2f}")
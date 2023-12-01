# Object-Relations-Code-Challenge---Restaurants
This Python code provides a simple implementation of a Restaurant Review System with classes for `Customer`, `Restaurant`, and `Review`. The system allows customers to add reviews for restaurants, and it provides methods to retrieve information about reviews, customers, and restaurants.


## Table of Contents

- [Classes](#classes)
  - [Customer](#customer)
  - [Restaurant](#restaurant)
  - [Review](#review)
- [Example Usage](#example-usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Classes

### Customer

The `Customer` class represents a customer who can add reviews for restaurants.

- `__init__(given_name, family_name)`: Initializes a new customer with given and family names.
- `given_name()`: Returns the given name of the customer.
- `family_name()`: Returns the family name of the customer.
- `full_name()`: Returns the full name of the customer.
- `all()`: Returns a list of all customer instances.
- `restaurants()`: Returns a unique list of all restaurants reviewed by the customer.
- `add_review(restaurant, rating)`: Adds a new review for a given restaurant with a star rating.

### Restaurant

The `Restaurant` class represents a restaurant that can be reviewed by customers.

- `__init__(name)`: Initializes a new restaurant with a name.
- `name()`: Returns the name of the restaurant.
- `reviews()`: Returns a list of all reviews for the restaurant.
- `customers()`: Returns a unique list of all customers who have reviewed the restaurant.
- `average_star_rating()`: Returns the average star rating for the restaurant based on its reviews.

### Review

The `Review` class represents a review given by a customer for a restaurant.

- `__init__(customer, restaurant, rating)`: Initializes a new review with a customer, restaurant, and a rating.
- `rating()`: Returns the rating for the review.
- `customer()`: Returns the customer object for the review.
- `restaurant()`: Returns the restaurant object for the review.

## Example Usage

customer1 = Customer("Dean", "Socrates")
customer2 = Customer("Johnnie", "Walker")
customer3 = Customer("Mike", "Johnson")
customer4 = Customer("Barrack", "Obama")

restaurant1 = Restaurant("Kwa Mathee")
restaurant2 = Restaurant("Fogo Gaucho")
restaurant3 = Restaurant("Sushi World")
restaurant4 = Restaurant("Pizza Haven")

customer1.add_review(restaurant1, 4)
customer2.add_review(restaurant2, 5)
customer3.add_review(restaurant1, 3)
customer4.add_review(restaurant3, 4)
customer2.add_review(restaurant4, 5)
customer3.add_review(restaurant3, 4)

print("Restaurants reviewed by customer1:", [restaurant.get_name() for restaurant in customer1.restaurants()]) # Output: Restaurants reviewed by customer1: ['Kwa Mathee']
print("Customers who reviewed restaurant1:", [customer.full_name() for customer in restaurant1.customers()])  # Output: Customers who reviewed restaurant1: ['Dean Socrates', 'Mike Johnson']
print(f"Average Star Rating for {restaurant1.get_name()}: {restaurant1.average_star_rating()}") # Output: Average Star Rating for Kwa Mathee: 3.5


## Project Structure 

The project follows a basic structure with three main classes: Customer, Restaurant, and Review. The classes are designed to allow customers to add reviews for restaurants, and they provide methods for retrieving information about reviews, customers, and restaurants.

## Contribution

Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

from Restaurant import Restaurant
from Review import Review
class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.all_customers.append(self)

    def get_given_name(self):
        return self.given_name

    def get_family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"
    @classmethod
    def all(cls):
        return cls.all_customers

    def restaurants(self):
        reviewed_restaurants = [review.restaurant() for review in Review.all_reviews if review.customer() == self]
        return list(set(reviewed_restaurants))

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)

    def num_reviews(self):
        return len([review for review in Review.all_reviews if review.customer() == self])

    @classmethod
    def find_by_name(cls, name):
        return next((customer for customer in cls.all_customers if customer.full_name() == name), None)

    @classmethod
    def find_all_by_given_name(cls, given_name):
        return [customer for customer in cls.all_customers if customer.given_name == given_name]
    
# Example:
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


print(customer1.restaurants())
print(restaurant1.customers())
print(f"Average Star Rating for {restaurant1.get_name()}: {restaurant1.average_star_rating()}")


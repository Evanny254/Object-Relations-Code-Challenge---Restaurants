class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer_ = customer
        self.restaurant_ = restaurant
        self.rating_ = rating
        Review.all_reviews.append(self)

    def rating(self):
        return self.rating_

    def customer(self):
        return self.customer_

    def restaurant(self):
        return self.restaurant_

    @classmethod
    def all(cls):
        return cls.all_reviews
    
# Example
customer1 = "Evans"
restaurant1 = "Pepinos"
rating1 = 3


review1 = Review(customer1, restaurant1, rating1)

print(review1.customer())
print(review1.restaurant())
print(review1.rating())

for review in Review.all():
    print(f"Customer: {review.customer()}, Restaurant: {review.restaurant()}, Rating: {review.rating()}")
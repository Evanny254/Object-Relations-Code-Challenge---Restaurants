from Review import Review
class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name_ = name
        Restaurant.all_restaurants.append(self)

    def get_name(self):
        return self.name_

    def reviews(self):
        return [review for review in Review.all_reviews if review.restaurant() == self]

    def customers(self):
        reviewers = [review.customer() for review in self.reviews()]
        return list(set(reviewers))

    def average_star_rating(self):
        ratings = [review.rating() for review in self.reviews()]
        if not ratings:
            return 0
        return sum(ratings) / len(ratings)


# Example
restaurant1 = Restaurant("Pepinos")
restaurant2 = Restaurant("Sushi Delight")

review1 = Review("Kevo", restaurant1, 4)
review2 = Review("Chris", restaurant1, 5)
review3 = Review("Jay", restaurant1, 3)
review4 = Review("David", restaurant2, 2)
review5 = Review("Emma", restaurant2, 4)
review6 = Review("Frank", restaurant2, 5)


print(f"Restaurant Name: {restaurant1.get_name()}")
print(f"Customers: {restaurant2.customers()}")
print(f"Average Star Rating: {restaurant1.average_star_rating()}")

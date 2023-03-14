class Restaurant:

    def __init__(self, r_name, cuisine_type):
        self.r_name = r_name
        self.cuisine_type = cuisine_type
        self.number_served = 32

    def describe_restaurant(self):
        print(f"{self.r_name} serves {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.r_name} is opened!")

    def served(self):
        print(f"Total number of clients served {str(self.number_served)}")

    def set_number_served(self, served_client):
        if served_client >= self.number_served:
            self.number_served = served_client
        else:
            print(f"No new clients!")

    def increment_number_served(self, new_client_served):
        self.number_served += new_client_served


my_restaurant = Restaurant("Ga! DarkStreet", "Kelewele")

print(my_restaurant.r_name.title())
print(my_restaurant.cuisine_type)

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.served()
my_restaurant.set_number_served(60)
my_restaurant.served()
my_restaurant.increment_number_served(3)
my_restaurant.served()
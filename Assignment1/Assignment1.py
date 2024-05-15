import sys

class Product:
    supermarket_name = "XYZ Supermarket"
    
    def __init__(self, product_ID, name, price, manufacturer, weight, expiration_date, year):
        self._product_ID = product_ID
        self.name = name
        self.price = price
        self.manufacturer = manufacturer
        self.weight = weight
        self.expiration_date = expiration_date
        self.year = year

    def show_details(self):
        details = (
            f"Supermarket Name: {self.supermarket_name}\n"
            f"Product ID: {self._product_ID}\n"
            f"Name: {self.name}\n"
            f"Price: ${self.price}\n"
            f"Manufacturer: {self.manufacturer}\n"
            f"Weight: {self.weight} grams\n"
            f"Expiration Date: {self.expiration_date}\n"
            f"Year: {self.year}"
        )
        print(details)

    def change_product_ID(self):
        self._product_ID = int(input("Enter the new Product ID: "))
        print(f"Updated Product ID: {self._product_ID}")

class Healthy(Product):
    def __init__(self, product_ID, name, price, manufacturer, weight, expiration_date, year, calories, components):
        super().__init__(product_ID, name, price, manufacturer, weight, expiration_date, year)
        self.calories = calories
        self.components = components

    def show_healthy_details(self):
        self.show_details()
        print(f"Calories: {self.calories} per gram")
        print(f"Components: {', '.join(self.components)}")

    def change_calories(self):
        self.calories = int(input("Enter new calories per gram: "))

    def calculate_total_calories(self, weight):
        print(f"Total Calories: {self.calories * weight}")

    def display_components_and_calories(self):
        print(f"Components: {', '.join(self.components)}")
        print(f"Calories: {self.calories}")

product_instance = None
healthy_instance = None

def add_product():
    global product_instance
    product_details = {
        "product_ID": input("Enter Product ID: "),
        "name": input("Enter Product Name: "),
        "price": float(input("Enter Price: ")),
        "manufacturer": input("Enter Manufacturer: "),
        "weight": int(input("Enter Weight: ")),
        "expiration_date": input("Enter Expiration Date: "),
        "year": int(input("Enter Year: "))
    }
    product_instance = Product(**product_details)
    print("Product added successfully!")
    product_instance.show_details()

def add_healthy_product():
    global healthy_instance
    product_details = {
        "product_ID": input("Enter Product ID: "),
        "name": input("Enter Product Name: "),
        "price": float(input("Enter Price: ")),
        "manufacturer": input("Enter Manufacturer: "),
        "weight": int(input("Enter Weight: ")),
        "expiration_date": input("Enter Expiration Date: "),
        "year": int(input("Enter Year: "))
    }
    components = input("Enter Components (comma-separated): ").split(',')
    healthy_instance = Healthy(**product_details, calories=0, components=components)
    print("Healthy product added successfully!")
    healthy_instance.show_healthy_details()

def main():
    print("Welcome to XYZ Supermarket")
    while True:
        subsystem_choice = int(input("Choose the Subsystem:\n1. Product\n2. Healthy\n3. Exit\nEnter Your Choice: "))
        if subsystem_choice == 1:
            while True:
                product_choice = int(input("\nProduct Subsystem:\n1. Add New Product\n2. Display Product Details\n3. Change/Edit Product ID\n4. Exit Subsystem\n5. Exit System\nEnter Your Choice: "))
                if product_choice == 1:
                    add_product()
                elif product_choice == 2:
                    if product_instance:
                        product_instance.show_details()
                    else:
                        print("No product added yet.")
                elif product_choice == 3:
                    if product_instance:
                        product_instance.change_product_ID()
                    else:
                        print("No product added yet.")
                elif product_choice == 4:
                    break
                elif product_choice == 5:
                    sys.exit()
        elif subsystem_choice == 2:
            while True:
                healthy_choice = int(input("\nHealthy Subsystem:\n1. Add New Healthy Product\n2. Display Healthy Product Details\n3. Change/Edit Calories\n4. Show Components and Calories\n5. Calculate Total Calories\n6. Exit Subsystem\n7. Exit System\nEnter Your Choice: "))
                if healthy_choice == 1:
                    add_healthy_product()
                elif healthy_choice == 2:
                    if healthy_instance:
                        healthy_instance.show_healthy_details()
                    else:
                        print("No healthy product added yet.")
                elif healthy_choice == 3:
                    if healthy_instance:
                        healthy_instance.change_calories()
                    else:
                        print("No healthy product added yet.")
                elif healthy_choice == 4:
                    if healthy_instance:
                        healthy_instance.display_components_and_calories()
                    else:
                        print("No healthy product added yet.")
                elif healthy_choice == 5:
                    if healthy_instance:
                        weight = int(input("Enter Weight (grams): "))
                        healthy_instance.calculate_total_calories(weight)
                    else:
                        print("No healthy product added yet.")
                elif healthy_choice == 6:
                    break
                elif healthy_choice == 7:
                    sys.exit()
        elif subsystem_choice == 3:
            print("Exiting the Supermarket Cashier System.")
            break

if __name__ == "__main__":
    main()
1
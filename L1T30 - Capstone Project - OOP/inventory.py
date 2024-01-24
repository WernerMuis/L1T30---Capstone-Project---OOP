from tabulate import tabulate 


class Shoe:
    """ 
    Shoe class containing:
    country:  Where the shoes are based
    code:     The SKU code of the shoe
    product:  The name of the shoe
    cost:     Cost of the shoe
    quantity: The quantity of the shoe
    
    Contains def __init__, get_cost, get_quantity and __str__.
    """


    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity


    def get_cost(self):
        return self.cost


    def get_quantity(self):
        return self.quantity


    def __str__(self):
        return f"""
Country:    {self.country}
Code:       {self.code}
Product:    {self.product}
Cost:       {self.cost}
Quantity:   {self.quantity}
"""


# Empty list to store shoe objects
shoe_list = []


def read_shoes_data():
    """Retrieves data form inventory.txt."""
    try:
        with open("inventory.txt", "r") as file:
            next(file)
            for line in file:
                data = line.strip().split(',')
                country, code, product, cost, quantity = data
                shoe = Shoe(country, code, product, float(cost), int(quantity))
                shoe_list.append(shoe)
        print("Data has been loaded successfully.")
    except FileNotFoundError:
        print("File 'inventory.txt' was not found.")


def capture_shoes():
    """Enables user to capture data for a new shoe."""
    country = input("Please enter the country: ")
    code = input("Please enter the code of the shoe: ")
    product = input("Please enter the name of the shoe: ")
    cost = float(input("Please enter the cost of the shoe: "))
    quantity = int(input("Please enter the  shoe quantity: "))
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    print("The shoe has been added successfully.")


def view_all():
    """Allows the user to see data on all shoes."""
    if not shoe_list:
        print("There are no shoes in the inventory. Please select option 1.")
    else:
        table_data = []
        for shoe in shoe_list:
            table_data.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])
        headers = ["Country", "Code", "Product", "Cost", "Quantity"]
        print(tabulate(table_data, headers, tablefmt="fancy_grid"))


def re_stock():
    """Returns shoe with the lowest stock and allows user to choose whether to add more stock."""
    if not shoe_list:
        print("There are no shoes in the inventory. Please select option 1.")
        return

    lowest_quantity_shoe = min(shoe_list, key=lambda x: x.get_quantity())
    print(f"The lowest quantity shoe: {lowest_quantity_shoe}")
    
    restock_option = input("Do you want to restock this shoe? (yes/no): ").lower()
    if restock_option == "yes":
        additional_quantity = int(input("Please enter the quantity that you would like to restock: "))
        lowest_quantity_shoe.quantity += additional_quantity
        print("Restock has been completed.")
    elif restock_option == "no":
        print("No restock was performed.")
    else:
        print("Invalid option. Please enter 'yes' or 'no'.")


def search_shoe():
    """Returns wanted shoe info."""
    code = input("Please enter the shoe code to search: ")
    found_shoe = None
    for shoe in shoe_list:
        if shoe.code == code:
            found_shoe = shoe
            break
    if found_shoe:
        print(found_shoe)
    else:
        print("Shoe was not found. Please try again.")


def value_per_item():
    """Returns the value of shoe stock."""
    if not shoe_list:
        print("There are no shoes in the inventory. Please select option 1.")
    else:
        for shoe in shoe_list:
            value = shoe.get_cost() * shoe.get_quantity()
            print(f"Product: {shoe.product}, Total Value: {value}")


def highest_qty():
    """Returns shoe with highest stock quantity."""
    if not shoe_list:
        print("There are no shoes in the inventory. Please select option 1.")
    else:
        highest_quantity_shoe = max(shoe_list, key=lambda x: x.get_quantity())
        print(f"Highest quantity shoe: {highest_quantity_shoe}")


def save_to_file():
    """Function to save/amend date to inventory.txt."""
    with open("inventory.txt", "w") as file:
        file.write("Country,Code,Product,Cost,Quantity:\n")
        for shoe in shoe_list:
            file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
    print("The inventory data has been saved to 'inventory.txt'.")


read_shoes_data()

# User main Menu
while True:
    print("""
Inventory Management Menu:
1. Read Shoes Data from File
2. Capture Shoes Data
3. View All Shoes
4. View/Restock Lowest Quantity Shoe
5. Search for a Shoe
6. Calculate Value per Shoe Type
7. View Shoe with Highest Quantity
8. Exit""")
    print()

# User input to call a function.
    choice = input("Please select an option by entering it's number: ")
    print()

    if choice == '1':
        pass
    elif choice == '2':
        capture_shoes()
        save_to_file()
    elif choice == '3':
        view_all()
    elif choice == '4':
        re_stock()
        save_to_file()
    elif choice == '5':
        search_shoe()
    elif choice == '6':
        value_per_item()
    elif choice == '7':
        highest_qty()
    elif choice == '8':
        print("The program has been closed.")
        break
    else:
        pass

# Used https://www.datacamp.com/tutorial/docstrings-python to improve/work on my docstring skills.
# Used https://www.w3schools.com/python/python_lambda.asp for lambda function.

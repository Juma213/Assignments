# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:00:05 2024

@author: George Juma
"""
import csv
import os

# File for storing products
PRODUCT_FILE = 'products.csv'

# Header names for the CSV file
CSV_HEADERS = ['Name', 'Price', 'Quantity']


# Function for initializing the product file
def initialize_file():
    # If the file doesn't exist, create it with headers
    if not os.path.exists(PRODUCT_FILE):
        with open(PRODUCT_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(CSV_HEADERS)


# Function for adding a product
def add_product(name, price, quantity):
    try:
        with open(PRODUCT_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, price, quantity])
        print(f'Product "{name}" added successfully!')
    except Exception as e:
        print(f"Error adding product: {e}")


# Function for viewing all the added products
def view_products():
    try:
        with open(PRODUCT_FILE, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            products = list(reader)
            if products:
                print("List of Products:")
                for index, product in enumerate(products, 1):
                    print(f"{index}. Name: {product[0]}, Price: {product[1]}, Quantity: {product[2]}")
            else:
                print("No products available.")
    except FileNotFoundError:
        print("Error: Product file not found.")
    except Exception as e:
        print(f"Error reading product file: {e}")


# Function for updating a product
def update_product(index, name=None, price=None, quantity=None):
    try:
        with open(PRODUCT_FILE, mode='r') as file:
            reader = csv.reader(file)
            products = list(reader)

        if 1 <= index < len(products):
            # Updating product details if provided
            if name:
                products[index][0] = name
            if price:
                products[index][1] = price
            if quantity:
                products[index][2] = quantity

            # Saving the updated product list
            with open(PRODUCT_FILE, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(products)
            print(f"Product at index {index} updated successfully.")
        else:
            print("Invalid product index.")
    except FileNotFoundError:
        print("Error: Product file not found.")
    except Exception as e:
        print(f"Error updating product: {e}")


# Function for deleting a product
def delete_product(index):
    try:
        with open(PRODUCT_FILE, mode='r') as file:
            reader = csv.reader(file)
            products = list(reader)

        if 1 <= index < len(products):
            del products[index]

            with open(PRODUCT_FILE, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(products)
            print(f"Product at index {index} deleted successfully.")
        else:
            print("Invalid product index.")
    except FileNotFoundError:
        print("Error: Product file not found.")
    except Exception as e:
        print(f"Error deleting product: {e}")


# Main program loop
def main():
    initialize_file()
    
    while True:
        print("\nProduct Manager:")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter product name: ")
            price = input("Enter product price: ")
            quantity = input("Enter product quantity: ")
            add_product(name, price, quantity)

        elif choice == '2':
            view_products()

        elif choice == '3':
            view_products()
            index = int(input("Enter the index of the product to update: "))
            name = input("Enter new name (or press Enter to keep the same): ")
            price = input("Enter new price (or press Enter to keep the same): ")
            quantity = input("Enter new quantity (or press Enter to keep the same): ")
            update_product(index, name if name else None, price if price else None, quantity if quantity else None)

        elif choice == '4':
            view_products()
            index = int(input("Enter the index of the product to delete: "))
            delete_product(index)

        elif choice == '5':
            print("Exiting Product Manager.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


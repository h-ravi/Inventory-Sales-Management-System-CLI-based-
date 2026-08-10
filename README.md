# Inventory & Sales Management System (CLI)

A simple command-line based Inventory and Sales Management System built in Python.
This project was made to practice core Python concepts - loops, conditions, file handling (JSON & CSV), and OOP.

## Features

- **Add Product** - add new products with ID, name, price, and quantity
- **Update Product** - update price or quantity of existing products
- **Delete Product** - remove a product permanently
- **View All Products** - see full product list with total amount
- **Sell Product** - sell a product, stock updates automatically
- **Stock Check** - prevents selling if quantity is not available
- **Sales History** - every sale is saved with date, time, price, and quantity
- **Data Storage** - all data is saved in `products.json` and `sales.csv`, so it stays safe even after closing the program

## Tech Used

- Python 3
- Built-in modules: `json`, `csv`, `datetime`

## Project Structure

```
main.py       -> Starts the application, shows main menu
common.py     -> Shared functions (input validation, save/load data)
product.py    -> Product class and product management menu
sales.py      -> Sales class and selling logic
products.json -> Stores product data
sales.csv     -> Stores sales history
```

## How to Run

1. Clone this repository
2. Make sure Python 3 is installed
3. Run the command:
   ```
   python main.py
   ```
4. Follow the on-screen menu to add products, sell products, and view your inventory

## Note

This is a learning project. It is not built for production use, only to practice real Python concepts hands-on.

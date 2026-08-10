import json
import common
import product as pro
import sales as sl

# create json database file (if not created) jds shesh
try:
    with open("products.json", "x") as empty_file:
        json.dump([],empty_file)
    with open("sales.csv", "x"):
        pass
except FileExistsError:
    pass
# Load data in json
all_product_info = common.all_product_info
# report
# Main Application
login = True
while login:
    print("1. Add Product")
    print("2. Sell Product")
    print("3. View All Product")
    print("4. Exit")
    choose = common.choose(1,4)
    if choose == 0:
        continue
    elif choose == 1:
        pro.product_manager()
    elif choose == 2:
        sl.sale_record()
    elif choose == 3:
        print("All Product List in Your Inventry")
        for details in all_product_info:
            try:
                total_profit = details['net_profit']
            except KeyError:
                total_profit = 0
            print("==============================")
            print(f"Product ID : {details['id']}")
            print(f"Product Name : {details['name']}")
            print(f"Product Per Unit Price : {details['price']}")
            print(f"Product Quantity : {details['quantity']}")
            print(f"Product Total Amount : {details['total_amount']}")
            print(f"Product Total Profit : {total_profit}")
            print("==============================")
    elif choose == 4:
        print("Are You Sure Exit and Close Inventry Managment Cli Application?")
        confirm = common.ask()
        if confirm:
            print("Thanks! For Using Our Product Manegmet Application. Your All Data Save in product.json and sales.csv")
            login = False
        else:
            continue
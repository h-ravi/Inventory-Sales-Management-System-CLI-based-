import json

# load frash data
try:
    with open("products.json",'r') as product_file:
        all_product_info = json.load(product_file)
except json.decoder.JSONDecodeError:
    all_product_info = []
# update new data
def update_data():
    with open("products.json","w") as update_file:
        json.dump(all_product_info, update_file, indent=4)
# Confirmation
def ask():
    while True:
        print("1. Yes")
        print("0. No")
        try:
            confi_option = int(input("Enter : "))
        except ValueError:
            print("Invalid Option! Please Enter 1 For Yes or 0 for No.")
            continue
        if confi_option == 0:
            return False
        elif confi_option == 1:
            return True
        else:
            print("Invalid Option! Please Enter 1 For Yes or 0 for No.")
# choose Option
def choose(min_choose,max_choose):
    while True:
        try:
            choose_option = int(input("Choose Your Option : "))
        except ValueError:
            print(f"Invalid Option! Please Choose Right Option Under {min_choose} to {max_choose} or Enter 0 for cancel")
            continue
        if choose_option == 0:
            return choose_option
        elif choose_option < min_choose or choose_option > max_choose:
            print(f"Invalid Option! Please Choose Right Option Under {min_choose} to {max_choose} or Enter 0 for cancel")
            continue
        else:
            return choose_option
# innput Number
def inte(nami):
    while True:
        print("Always Enter Number Grater Then Zero and only Number like 1,2,3,4.........(Enter 0 for Exit)")
        try:
            inputs = int(input(f"Enter Product {nami} : "))
        except ValueError:
            print("Please Type Only number like 1,2,3,4,5......")
            continue
        if inputs < 0:
            print("Please Enter Only Positive And Grater then Zero Number (Enter 0 for Exit)")
            continue
        else:
            return inputs
# duplicate id
def duplicate(id_input):
    for details in all_product_info:
        if details['id'] == id_input:
            return True
    return False
def find(id_input):
    for find_details in all_product_info:
        if find_details['id'] == id_input:
            print("============================")
            print(f"Product ID = {find_details['id']}")
            print(f"Product Name = {find_details['name']}")
            print(f"Product Per Unit Price = {find_details['price']}")
            print(f"Product quantity = {find_details['quantity']}")
            print(f"Product Total Amount = {find_details['total_amount']}")
            print("============================")
            break
if __name__ == "__main__":
    # choose = choose(1,5)
    # print(choose)
    # Ask = ask()
    # print(Ask)
    inputi = int(input("Enter : "))
    status = duplicate(inputi)
    print(status)
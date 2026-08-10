import json
import common

# load Data
all_product_info = common.all_product_info
# main
class Product:
    def __init__(self,id,name,price,quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
    def Add(self):
        new_data = {'id':self.id,'name':self.name,'price':self.price,'quantity':self.quantity,"total_amount":self.price*self.quantity}
        all_product_info.append(new_data)
        print(f"\n{all_product_info}\n")
        common.update_data()
        print("Your Product Data Successful add in Database")
    def update_price(self,new_price):
        self.new_price = new_price
        for details in all_product_info:
            if details['id'] == self.id:
                details['price'] = self.new_price
                details['total_amount'] = self.new_price*details['quantity']
                common.update_data()
                print(f"Successfule Update Product ID {self.id} Price. Now Current Price is : {self.new_price}")
                break
    def update_quantity(self,quantity):
        self.quantity = quantity
        for details in all_product_info:
            if details['id'] == self.id:
                details['quantity'] = self.quantity
                details['total_amount'] = self.quantity*details['price']
                common.update_data()
                print(f"Successfule Update Product ID {self.id} Quantity. Now Current Quantity is : {self.quantity}")
                break
    def delete_data(self):
        for index, details in enumerate(all_product_info):
            if details['id'] == self.id:
                del all_product_info[index]
                common.update_data()
                break
def product_manager():
    while True:
        print("1. Add New Data")
        print("2. Update Data")
        print("3. Delete Data")
        print("4. See All Data")
        print("5. Close Product Manager")
        choose = common.choose(1,5)
        if choose == 0:
            continue
        elif choose == 1:
            while True:
                id_input = common.inte('id')
                duplicate = common.duplicate(id_input)
                if duplicate == True:
                    print("Duplicate Id Detected. Always Enter Uniq id for any products.")
                    common.find(id_input)
                    continue
                else:
                    name_input = input("Enter Product Name : ")
                    price_input = common.inte('price')
                    quantity_input = common.inte('quantity')
                    send_data = Product(id_input,name_input,price_input,quantity_input)
                    send_data.Add()
                    break
        elif choose == 2:
            while True:
                id_input = common.inte('id')
                find_id = common.duplicate(id_input)
                if find_id:
                    common.find(id_input)
                    print("What do you want to update?")
                    print("1. Price")
                    print("2. Quantity")
                    choose = common.choose(1,2)
                    update_data = Product(id_input, None,None,None)
                    if choose == 0:
                        break
                    elif choose == 1:
                        new_price = common.inte('new_price')
                        update_data.update_price(new_price)
                    else:
                        new_quantity = common.inte('New Quantity')
                        update_data.update_quantity(new_quantity)
                    break
        elif choose == 3:
            while True:
                id_input = common.inte('id')
                if id_input == 0:
                    break
                find_id = common.duplicate(id_input)
                print("Are You Sure Delete This ID Data Permanently")
                common.find(id_input)
                confi_input = common.ask()
                if confi_input == 1:
                    delete_data = Product(id_input,None,None,None)
                    delete_data.delete_data()
                else:
                    break
                break
        elif choose == 4:
            print("All Product List in Your Inventry")
            for details in all_product_info:
                print("==============================")
                print(f"Product ID : {details['id']}")
                print(f"Product Name : {details['name']}")
                print(f"Product Per Unit Price : {details['price']}")
                print(f"Product Quantity : {details['quantity']}")
                print(f"Product Total Amount : {details['total_amount']}")
                print("==============================")
        elif choose == 5:
            break
        else:
            print("Please Choose Your Option")
            continue

if __name__ == "__main__":
    product_manager()
    for details in all_product_info:
        print(details)
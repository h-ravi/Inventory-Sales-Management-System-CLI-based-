import csv
import json
import common
from datetime import datetime
# load json data
all_product_info = common.all_product_info
# read csv
def show_data():
    with open("sales.csv",'r') as csv_file:
        all_sales = csv.DictReader(csv_file)
        all_csv_data = list(all_sales)
        for csv_data in all_csv_data:
            print(csv_data)

def update_csv_data(update_selling_data):
    with open("sales.csv","a", newline="") as new_csv_data:
        data_header = ['selling_date','selling_time','prouct_id','product_name','selling_price','current_price','selling_quantity','current_quantity','remaining_quantity','total_selling_price','remaining_total_price','net_profit']
        update_csv = csv.DictWriter(new_csv_data, fieldnames= data_header)
        update_csv.writerow(update_selling_data)
        
class Sales:
    def __init__(self,id,selling_price,selling_quantity):
        self.id=id
        self.selling_price = selling_price
        self.selling_quantity = selling_quantity
    def update_sell(self):
        for details in all_product_info:
            if details['id'] == self.id:
                jsondb_id = details['id']
                jsondb_name = details['name']
                jsondb_current_price = details['price']
                jsondb_quantity = details['quantity']
                jsondb_total_price = details['total_amount']
                selling_date = datetime.now().strftime("%Y-%m-%d")
                selling_time = datetime.now().strftime("%H:%M:%S")
                try:
                    net_profit = details['net_profit']
                except KeyError:
                    net_profit = 0
                if (jsondb_total_price - (self.selling_quantity*self.selling_price)) < 0:
                    net_profit += (self.selling_quantity*self.selling_price) - jsondb_total_price
                else:
                    net_profit += 0
                if details['total_amount']-(self.selling_quantity*self.selling_price) < 0:
                    remaining_total_price = 0
                else:
                    remaining_total_price = details['total_amount']-(self.selling_quantity*self.selling_price)
                if (jsondb_quantity - self.selling_quantity) < 0:
                    print(f"\nThis Sell Not Confirm because Your Current Quanity Not Sufficent. Current Max this product Quanity {jsondb_quantity} in this Product ID {self.id} and name {jsondb_name}\n")
                    break
                else:
                    update_selling_data = {
                        "selling_date": selling_date,
                        "selling_time": selling_time,
                        "prouct_id":self.id,
                        "product_name":jsondb_name,
                        "selling_price":self.selling_price,
                        "current_price":jsondb_current_price,
                        "selling_quantity":self.selling_quantity,
                        "current_quantity":jsondb_quantity,
                        "remaining_quantity": jsondb_quantity-self.selling_quantity,
                        "total_selling_price": self.selling_quantity*self.selling_price,
                        "remaining_total_price" : remaining_total_price,
                        "net_profit":net_profit
                    }
                    for jsondb in all_product_info:
                        if jsondb['id'] == self.id:
                            jsondb['quantity'] = jsondb_quantity-self.selling_quantity
                            jsondb['total_amount'] = remaining_total_price
                            jsondb['net_profit'] = net_profit
                            common.update_data()
                            update_csv_data(update_selling_data)
                            print("Successfully Add Selling History. New Data")
                            common.find(self.id)
                            break

def sale_record():
    while True:
        print("1. Add Selling")
        print("2. Show Selling History")
        print("3. Goto Maine Menu")
        choose = common.choose(1,3)
        if choose == 0:
            break
        elif choose == 1:
            print("\nAttention Please : Please ensure that accurate information is used when entering sales data. Once the data has been added, only the administrator can modify or remove it.\n")
            print("Enter the ID of the product to be sold.")
            id_inputs = common.inte('Product ID')
            if id_inputs == 0:
                break
            else:
                print("Product Info")
                common.find(id_inputs)
                selling_price = common.inte('Selling Price per Unit')
                selling_quantity = common.inte('Total Unit Selling Quantity')
                sales = Sales(id_inputs,selling_price,selling_quantity)
                sales.update_sell()
        elif choose == 2:
            show_data()
            print("\n")
        elif choose == 3:
            break
        else:
            print("Invalid Choosen Option! Please Choose Right option.")
            continue

if __name__ == "__main__":
    sale_record()
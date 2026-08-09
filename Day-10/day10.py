customer_name = input("Enter customer name: ")
parts_price = float(input("Enter parts price: "))
labour_charge = float(input("Enter labour charge: "))
discount = float(input("Enter discount:"))

total_bill = parts_price + labour_charge

after_discount = total_bill - discount

gst = after_discount * 18 / 100

final_bill = after_discount + gst

print("-----GARAGE BILL-----")
print("Customer:", customer_name)
print("Parts:", parts_price)
print("Labour:", labour_charge)
print("Total Bill:", total_bill)
print("after Discount:", discount)
print("GST:", gst)
print("Final bill:", final_bill)

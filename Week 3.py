price=int(input("ENTER PRICE"))
discount_percentage =int(input("Enter discount percentage:"))

def calculate_discount(price,discount_percentage):

    if discount_percentage > 100:
        print("Error: Discount percentage cannot exceed 100%. Using 100% discount.")
        discount_percentage = 100

    if discount_percentage >= 20:
        discount_amount = price * discount_percentage / 100
        final_price = price - discount_amount
        return final_price

    else:
        return price

final_price = calculate_discount(price, discount_percentage)
print(f"The final price is: {final_price:.2f}")




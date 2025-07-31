def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    Apply the discount only if discount_percent is 20 or higher.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for inputs
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))
except ValueError:
    print("Invalid input! Please enter numeric values.")
    exit()

# Calculate the final price
final_price = calculate_discount(original_price, discount)

# Print the result
if discount >= 20:
    print(f"Discount applied! Final price: ${final_price:.2f}")
else:
    print(f"No discount applied. Original price remains: ${original_price:.2f}")

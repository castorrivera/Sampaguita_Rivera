def calculate_payment(quantity):
    if quantity < 3:
        discount = (quantity * 50) - 0
        return discount
    elif quantity < 5:
        discount = (quantity * 50) - (quantity * 50 * 0.10)
        return discount
    elif quantity > 4:
        discount = (quantity * 50) - (quantity * 50 * 0.20)
        return discount



def get_performance(total_sales):
    total = donuts * 50
    if total < 400:
        performance = str("Needs Improvement")
    elif total < 700:
        performance = str("Good Fundraising")
    elif total < 1000:
        performance = str("Very Good Fundraising")
    elif total < 999:
        performance = str("Excellent Fundraising")
    return performance, total

def display_summary(section, total_sales, performance):
    print("================================================")
    print("         JS PROM FUNDRAISING REPORT")
    print("================================================")
    print("Grade 11 Section : ", section)
    print(f"Total Sales : {total}")
    print("Performance : ", performance)
    print("================================================")

print("================================================")
print("           J.CO DONUT FUNDRAISING")
print("         Sweet Treats for a Cause")
print("================================================")
section = str(input("Enter Grade 11 section: "))
donuts = 0
for i in range(1, 6):
    print("---------------- CUSTOMER ", i ," ----------------")
    donut = int(input("Enter Donuts Purchased: "))
    dis = calculate_payment(donut)
    print(f"Total Sales : {dis}")
    tot = donuts - dis
    print(f"Final Payment: {tot:.2f}")


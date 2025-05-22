billAmount = 0
tip = 0
tipRate = 0
total = 0

def get_inputs(message):
    while True:
        try:
            num = eval(input(message))
            if num > 0:
                return num
            else:
                print("Please enter a positive number")
        except NameError:
            print ("Please enter a valid number")


def get_tip(bill_amount, tip_rate):
    return billAmount * (tipRate / 100)


def get_total(bill_amount, tip):
    return billAmount + tip


billAmount = get_inputs("What is the bill amount? ")
tipRate = get_inputs("What is the tip rate? ")

tip = get_tip(billAmount, tipRate)

print(f"Tip: ${tip:.2f}")

total = get_total(billAmount, tip)
print(f"Total: ${total:.2f}")

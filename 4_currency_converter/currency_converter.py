currencies = ("US", "EU", "CA")
exchange_rate = {
    "US":{"EU":.75,"CA":1.5,"US":1},
"EU":{"EU":1,"CA":2,"US":1.5},
"CA":{"EU":.5,"CA":1,"US":.75}
}
def get_amount():
    while True:
        try:
            amount = float(input("Please enter an amount to be exchanged: "))
            if amount <= 0:
                raise ValueError()
            else:
                break
        except ValueError:
            print("This is not a Valid amount to be exchanged")
    return amount
def get_src_currency():
    while True:
        try:
            src_currency = input("What currency do you wish to exchange US, EU, CA?: ")
            if src_currency not in currencies:
                raise ValueError()
            else:
                break
        except ValueError:
            print("Please Enter a Valid Currency... US/EU/ or CA")
    return src_currency
def get_trg_currency():
    while True:
        try:
            trg_currency = input("what is your targegt currency?")
            if trg_currency not in currencies:
                raise ValueError()
            else:
                break
        except ValueError:
            print("Please enter a Valid Target Currency to exchange US, EU, CA?: ")
    return trg_currency
def run(amount, exchange_rate, src_currency, trg_currency):
    converted_amount = amount * exchange_rate[src_currency][trg_currency]
    return converted_amount

amount = get_amount()
src_currency = get_src_currency()
trg_currency = get_trg_currency()
converted_amount = run(amount, exchange_rate, src_currency, trg_currency)
print(f"You will get back {converted_amount} {trg_currency}")

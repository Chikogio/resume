def create_acc():
    username = input("შეიყვანე სახელი: ")
    password = input("შეიყვანე პაროლი: ")
    return {"username": username, "password": password, "balance": 199.99}

def deposit(acc, amount):
    if amount > 0:
        acc["balance"] += amount
        print("შეტანილია $" + str(amount) + ". ბალანსია: $" + str(acc["balance"]))
    else:
        print("შეიყვანეთ სწორი რაოდენობა!")

def withdraw(account, amount):
    if amount > 0:
        if amount <= account["balance"]:
            account["balance"] -= amount
            print("გამოტანილია $" + str(amount) + " ბალანსია: $" + str(account["balance"]))
        else:
            print("გამოტანა გაუქმებულია!")
    else:
        print("შეიყვანეთ სწორი რაოდენობა!")

def get_balance(account):
    return account["balance"]

account = create_acc()

action = input("თანხის შეტანა გინდათ თუ გამოტანა? ")

if action == "შეტანა":
    deposit_amount = float(input("შეიყვანეთ რაოდენობა: "))
    deposit(account, deposit_amount)
elif action == "გამოტანა":
    withdrawal_amount = float(input("შეიყვანეთ რაოდენობა: "))
    withdraw(account, withdrawal_amount)
else:
    print("თანხის შესატანად შეიყვანეთ (შეტანა) ხოლო გამოსატანად შეიყვანეთ (გამოტანა) ")

print("ბალანსია: $" + str(get_balance(account)))
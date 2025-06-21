# demo.py
from banking import BankAccount, SavingsAccount, CheckingAccount, Customer, print_account_summary

# Create accounts
acc1 = BankAccount("Alice", 1000)
acc2 = SavingsAccount("Bob", 2000, 0.05)
acc3 = CheckingAccount("Charlie", 500, 200)

# Perform deposits and withdrawals
acc1.deposit(500)
acc2.withdraw(300)
acc2.apply_interest()
acc3.withdraw(600)  # within overdraft limit

# Merge accounts
merged_acc = acc1 + acc2

# Create customer and manage accounts
cust = Customer("Dana")
cust.add_account(acc1)
cust.add_account(acc2)
cust.add_account(acc3)
cust.add_account(merged_acc)

# Perform transfer
cust.transfer(acc1, acc3, 200)

# Print summaries
print("\n--- Account Summaries ---")
for acc in cust.accounts:
    print_account_summary(acc)
    print(str(acc))
    print(repr(acc))

# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

extra_payment_start_month = int(input('Extra payment start month: '))
extra_payment_end_month = int(input('Extra payment end month: '))
extra_payment = int(input('Extra payment: '))

over_payment = 0

month = 0
while principal > 0:
    month = month + 1
    this_months_payment = payment
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        this_months_payment = payment + extra_payment

    principal = principal * (1 + rate / 12) - this_months_payment
    if principal < 0:
        over_payment = abs(principal)
        principal = 0
    total_paid = total_paid + this_months_payment - over_payment

    print(month, round(total_paid, 2), round(principal, 2))

print('Total paid', round(total_paid, 2))
print('Number of months', month)

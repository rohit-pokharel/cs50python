def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# Strip $ sign
def dollars_to_float(d):
    return float(d.strip('$'))

# Strip % sign
def percent_to_float(p):
    return float(p.strip('%')) / 100

main()

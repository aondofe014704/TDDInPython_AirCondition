email = input("Enter your email address: ").strip()

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")
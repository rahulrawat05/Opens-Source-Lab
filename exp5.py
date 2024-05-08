import random
print("Rahul Singh Rawat")
print("RN : 210410101092")


def generate_otp():
    otp = random.randint(1000, 9999)
    return otp

def send_otp(otp):
    print(f"OTP sent: {otp}")

def verify_otp(otp, user_input):
    if otp == int(user_input):
        print("OTP verification successful!")
    else:
        print("OTP verification failed!")

otp = generate_otp()
send_otp(otp)

user_input = input("Enter the OTP: ")

verify_otp(otp, user_input)


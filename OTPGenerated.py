import random

class OTPGenerated:
    def __init__(self):
        self.generated_otp = None

    def generate_otp(self):
        self.generated_otp = random.randint(1000, 9999)
        return self.generated_otp


class VerifyOTP:
    def verify(self, user_input, generated_otp):
        if user_input == generated_otp:
            return "Login Successful"
        else:
            return "Enter valid OTP"

otp_obj = OTPGenerated()
otp_value = otp_obj.generate_otp()
print("Generated OTP:", otp_value)

user_input = int(input("Enter The OTP: "))

verify_obj = VerifyOTP()
print(verify_obj.verify(user_input, otp_value))

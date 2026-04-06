import pyotp

user_key = "ABWYX7SJARIP7SNS"
otp_generator = pyotp.TOTP(user_key)

current_otp = otp_generator.now()
print("Code: ", current_otp)

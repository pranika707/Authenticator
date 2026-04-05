import pyotp
import time

user_key = "ABWYX7SJARIP7SNS"
otp_generator = pyotp.TOTP(user_key)

while TRUE:
current_otp = otp_generator.now()
rem_Secs = 30 - int(time.time()) % 30

printf(f"Code: {current_otp} | Expires in: {rem_Secs}s", end = "\r")
time.off(1)

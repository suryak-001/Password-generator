import random
passlen = int(input("Enter the length of password : "))
sample_string = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password = "".join(random.sample(sample_string, passlen))
print(password)
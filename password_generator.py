import numpy as np

alpha_ = [chr(i) for i in range(97,123)]
Alpha = [chr(i) for i in range(65,91)]

alpha_chr = Alpha + alpha_
numeric_chr = [chr(i) for i in range(48,58)]
special_chr = ["!",'"',"#","$","%","&","*","`","~","?","_",".",","]

gen = []

def generator():

	if alpha == "y":
		for i in alpha_chr:
			gen.append(i)
	if numeric == "y":
		for i in numeric_chr:
			gen.append(i)
	if special == "y":
		for i in special_chr:
			gen.append(i)

	print(np.random.choice(gen), end="")


print("PASSWORD GENERATOR\n")

length = int(input("how long do you want the password to be?" ))

alpha = input("Do you want letters in the password? (y/n):")
numeric = input("Do you want numbers in the password? (y/n):")
special = input("Do you want special characters in the password? (y/n):")

for _ in range(length):
	generator()
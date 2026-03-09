#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#pylint:disable=W0301
#
#  signature_rsa_demo.py
#
#  Copyright 2018- William Martinez Bas <metfar@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
#import warnings;
#warnings.filterwarnings("ignore", category=UserWarning);

"""
Simple demonstration of digital signature generation using:
1. A toy hash function: h(x) = (x + 3) mod 10;
2. A simplified RSA scheme:
   - private key d = 11;
   - public key e = 5;
   - modulus n = 14;

The message is x = 2.
The signature is computed as:
	s = h(x)^d mod n;

Verification is done by checking that:
	s^e mod n = h(x);
"""

def line(x="="):
	print(x * 70);
def explain_concepts():
	"""
	Prints a simple explanation of the previous concepts.
	"""
	line();
	print("PREVIOUS CONCEPTS");
	line();
	print();
	print("1) What is a message?");
	print("   In cryptography, a message is simply the data that we want");
	print("   to protect, sign, or verify. In this exercise, the message is 2.");
	print();
	print("2) What is a hash function?");
	print("   A hash function transforms some data into another value,");
	print("   usually smaller and easier to handle. Here we use a very");
	print("   simple toy hash function:");
	print("       h(x) = (x + 3) mod 10");
	print("   This is not secure in real life, but it is useful for learning.");
	print();
	print("3) What is RSA?");
	print("   RSA is a cryptographic system that uses two keys:");
	print("   - a public key, which anyone may know;");
	print("   - a private key, which only the owner should know.");
	print();
	print("4) What is a digital signature?");
	print("   A digital signature allows us to prove that a message");
	print("   was signed by the owner of the private key.");
	print();
	print("5) How do we sign in this exercise?");
	print("   First, we compute the hash of the message.");
	print("   Then we raise that hash to the private key modulo n:");
	print("       signature = hash^d mod n");
	print();
	print("6) How do we verify?");
	print("   We take the signature and raise it to the public key modulo n:");
	print("       verification = signature^e mod n");
	print("   If that result matches the original hash, the signature is valid.");
	print();
	print("7) Logical warning:");
	print("   This example uses very small numbers and an invented hash function.");
	print("   It is good for understanding the mechanism, not for real security.");
	print();
	line();
	print();


def toy_hash(x):
	"""
	Computes the toy hash:
		h(x) = (x + 3) mod 10
	"""
	return (x + 3) % 10;


def sign_rsa(hash_value, private_key, modulus):
	"""
	Signs a hash using simplified RSA:
		signature = hash_value^private_key mod modulus
	"""
	return pow(hash_value, private_key, modulus);


def verify_rsa(signature, public_key, modulus):
	"""
	Verifies a simplified RSA signature:
		result = signature^public_key mod modulus
	"""
	return pow(signature, public_key, modulus);


def show_parameters(message, private_key, public_key, modulus):
	"""
	Shows the parameters of the exercise.
	"""
	print("EXERCISE PARAMETERS");
	line("-");
	print(f"Message: {message}");
	print(f"Private key (d): {private_key}");
	print(f"Public key (e): {public_key}");
	print(f"Modulus (n): {modulus}");
	line("-");
	print();


def solve_exercise():
	"""
	Solves the digital signature exercise step by step.
	"""
	message = 2;
	private_key = 11;
	public_key = 5;
	modulus = 14;

	show_parameters(message, private_key, public_key, modulus);

	print("STEP 1: COMPUTE THE HASH OF THE MESSAGE");
	line("-");
	print("We use the function:");
	print("    h(x) = (x + 3) mod 10");
	hash_value = toy_hash(message);
	print("So:");
	print(f"    h({message}) = ({message} + 3) mod 10 = {hash_value}");
	print();

	print("STEP 2: GENERATE THE SIGNATURE WITH RSA");
	line("-");
	print("The signature is computed as:");
	print("    signature = hash^d mod n");
	print(f"    signature = {hash_value}^{private_key} mod {modulus}");
	signature = sign_rsa(hash_value, private_key, modulus);
	print(f"    signature = {signature}");
	print();

	print("STEP 3: VERIFY THE SIGNATURE");
	line("-");
	print("Verification is done as:");
	print("    verification = signature^e mod n");
	print(f"    verification = {signature}^{public_key} mod {modulus}");
	verification = verify_rsa(signature, public_key, modulus);
	print(f"    verification = {verification}");
	print();

	print("STEP 4: COMPARE");
	line("-");
	print(f"Original hash    = {hash_value}");
	print(f"Verified value   = {verification}");
	print();

	if verification == hash_value:
		print("RESULT: The signature is VALID.");
		print(f"The digital signature generated for message {message} is: {signature}");
	else:
		print("RESULT: The signature is INVALID.");
	print();

	print("FINAL INTERPRETATION");
	line("-");
	print("We signed the hash of the message, not the message directly.");
	print("That is precisely the basic idea of a digital signature.");
	print("In this case:");
	print(f"  - message = {message}");
	print(f"  - hash = {hash_value}");
	print(f"  - signature = {signature}");
	print(f"  - verification = {verification}");
	print();


def main():
	"""
	Main function.
	"""
	explain_concepts();
	solve_exercise();


if __name__ == "__main__":
	main();


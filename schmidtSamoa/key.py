#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#

"""
[~] Author: Black Viking
[~] Mail  : blackvkng@yandex.com
"""

import schmidtSamoa.prime as prime

import random

def getPrime(n):
	number = random.getrandbits(n)
	round  = prime.getRound(n)

	while prime.miller_rabin(number, round) != True:
		number = random.getrandbits(n)

	return number

def gcd(a, b):
	while b != 0:
		a, b = b, a % b

	return a

def lcm(a, b):
	return (a * b) / gcd(a, b)

def inverse(a, b):
	i = b
	v = 0
	d = 1

	while a > 0:
		t = i / a
		x = a

		a = i % x
		i = x
		x = d

		d = v - t * x
		v = x

	v = v % b

	if v < 0:
		v = (v + b) % b

	return v 

def generateKey(n):
	p, q = getPrime(n), getPrime(n)

	n = p * q

	pk = pow(p, 2) * q
	sk = inverse(pk, lcm(p - 1, q - 1))

	return(pk, (sk, n))

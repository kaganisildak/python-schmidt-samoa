#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#

"""
[~] Author: Black Viking
[~] Mail  : blackvkng@yandex.com
"""

import random

range = xrange if __import__('sys').version_info[0] == 2 else range

def getRound(n):
    if n >= 1536:
        return 3
    if n >= 1024:
        return 4
    if n >= 512:
        return 7

    return 10

def miller_rabin(n, k):
	if n == 2:
		return True
	if not n & 1:
		return False

	def check(a, s, d, n):
		x = pow(a, d, n)
		if x == 1:
			return True
		for i in range(s - 1):
			if x == n - 1:
				return True
			x = pow(x, 2, n)
		return x == n - 1

	s = 0
	d = n - 1

	while d % 2 == 0:
		d >>= 1
		s += 1

	for i in range(k):
		a = random.randrange(2, n - 1)
		if not check(a, s, d, n):
			return False
	return True
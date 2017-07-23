#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#

"""
[~] Author: Black Viking
[~] Mail  : blackvkng@yandex.com
"""

import base64

def encrypt(message, pk):

    """
    cipher = []

    for char in message.encode():
        newval = str(pow(ord(char), pk, pk)) + " "
        cipher.append(newval)

    return base64.b64decode(''.join(cipher).strip().encode())"""

    return base64.b64encode(''.join([str(int(pow(ord(char), pk, pk))) + " " for char in message]).strip().encode())

def decrypt(cipher, sk, n):

    """
    plain = []

    for num in base64.b64decode(cipher).split(" "):
        newval = str(chr(pow(num, sk, n)))
        plain.append(newval)

    return ''.join(plain)"""

    return ''.join([str(chr(pow(int(num), sk, n))) for num in base64.b64decode(cipher).split(" ")])

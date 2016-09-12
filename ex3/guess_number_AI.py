# -*- coding: utf-8 -*-
"""
:author: lihui
:website: withlihui.com
Let computer guess a number
"""

while True:
    try:
        num = int(raw_input('Enter a number: '))
    except ValueError:
        print "The input must be a integer!"
        continue
    break

guess = num / 2
middle = num / 4
step = 0

while guess != num:
    if num > guess:
        guess += middle
        print "I gusee: ", guess
    elif num < guess:
        guess -= middle
        print "I gusee: ", guess
    middle /= 2
    if middle == 0:
        middle = 1
    step += 1

print "Aha! The answer is: ", guess
print "I totally use %d steps." % step

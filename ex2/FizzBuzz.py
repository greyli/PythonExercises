# -*- coding: utf-8 -*-
"""
:author: lihui
:website: withlihui.com
Let computer guess a number
"""
for i in range(101): print((('Fizz' if i % 3 == 2 else '') + ('Buzz' if i % 5 == 4 else '')) or i+1)

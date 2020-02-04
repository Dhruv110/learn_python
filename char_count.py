__author__ = 'Dhruv Panchal'

str_in = str(input("Please enter a sentence:  "))

str_enter = str_in.lower()

c_count = {}

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for s in str_enter :
    if s in alphabet :
        if s not in c_count :
            c_count[s] = 0
        
        c_count[s] = c_count[s] + 1

c_keys = c_count.keys()
c_keys_order = sorted(c_keys)

for c in c_keys_order :
    print (c, c_count[c])

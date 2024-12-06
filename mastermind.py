import random

#Generates random code based on the six letters available.
code = "".join(random.sample('ABCDEF', 4))

print(code)

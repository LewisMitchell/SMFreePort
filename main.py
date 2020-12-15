import os
import random

x = os.popen('sm --ports').read()
y = []
for line in x.splitlines():
    z = int(line[:5])
    y.append(z)

newPort = random.choice(list(set(range(min(y)+1, max(y)))-set(y)))

print("Port available: %d" % newPort)
print("Assign port and run 'sm --checkports' to validate (returns 1 if not valid).")



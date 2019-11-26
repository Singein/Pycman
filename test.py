from pycman.utils import goto
import os
print(os.getcwd())

with goto('./test'):
    print(os.getcwd())

print(os.getcwd())

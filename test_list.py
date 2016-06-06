import random,string
from time import clock

def random_str(randomlength=8):
    a = list(string.ascii_letters)
    random.shuffle(a)
    return ''.join(a[:randomlength])

test_list = []

for x in range(1,1000):
    test_list.append(random_str(20))

__start = clock()
if "aaaaaaaa" in test_list:
    print("in")
__finish = clock()

print(__finish-__start)

l1 = [1,2,3,4,5,6,7,8,9]
print(l1[len(l1)-5:])
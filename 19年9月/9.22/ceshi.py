import time

t1 = time.time()
n = 10
t2 = time.time()
print('Done processing {0} trees ({1:.20f}sec)'.format(n, t2-t1))
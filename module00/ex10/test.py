from time import sleep
from loading import ft_progress
from tqdm import tqdm

listy = range(1000)
ret = 0
for elem in tqdm(listy):
    ret += (elem + 3) % 5
    # sleep(0.01)
print()
print(ret)

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    # sleep(0.01)
print()
print(ret)

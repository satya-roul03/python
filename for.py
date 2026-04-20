import time
for i in range(3,-1,-1):
    if i>0:
        print(i,end='>>>',flush=True)
        time.sleep(1)
    else:
        print('Start')
import os
import random
def main():
    count = 10
    while count:
        ip = [str(random.randrange(256)) for i in range(4)]
        ip = '.'.join(ip)
        response = os.system("ping " + ip)
        if response == 0:
            print('hellyes\n\n')
            print(f"{ip} is up!")
            count-=1

if __name__ == "__main__":
    main()

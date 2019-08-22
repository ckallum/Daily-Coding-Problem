from time import sleep

def f():
    print('Hello')

def delay(func, delayInMs):
    sleep(delayInMs/1000)
    func()


def main():
    delay(f, 1000)


if __name__ == '__main__':
    main()

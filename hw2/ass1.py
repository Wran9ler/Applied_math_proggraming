def timedelt(x):
    hours = x // 3600
    minutes = (x % 3600) // 60
    sec = (x % 60)
    print(f'{hours}h:{minutes}m:{sec}s')


timedelt(7250)


def work_our(y):
    if y > 40:
        print(int((1.4 * (y - 40) * 2000) + (40 * 2000)))
    else:
        print(y * 2000)


work_our(50)

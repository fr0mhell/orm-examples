from time import sleep


def dummy_progress(seconds: int):
    for i in range(seconds):
        sleep(1)
        print(f'Dummy progress: {i+1} / {seconds} sec')

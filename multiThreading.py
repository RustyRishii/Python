# multithreading = Used to perform multiple tasks concurrently (multitasking)
#                  Good for I/O bound tasks like reading files or fetching data from APIs
#                  threading.Thread(target=my_function)

import threading
import os
import time


def walk_dog(first, last):
    time.sleep(8)
    print(f"then, you take {first} {last} on a walk")


def throw_trash(place):
    time.sleep(4)
    print(f"You first throw the trash from the {place}")


def clean_room(room):
    time.sleep(10)
    print(f"and finally you start cleaning up the {room}")


# def run_defs():
#     walk_dog()
#     throw_trash()
#     clean_room()


# run_defs()

chore1 = threading.Thread(target=walk_dog, args=("Sooby", "Doo"))
# When you are passing only one argument in multitreading, Always pass a tuple with a comma.
chore2 = threading.Thread(target=throw_trash, args=("Kitchen",))
chore3 = threading.Thread(target=clean_room, args=("Garage",))

chore1.start()
chore2.start()
chore3.start()

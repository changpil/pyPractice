# class RefrigeratorRaider:
#     def open(self):
#         print("Open fridge door.")
#
#     def take(self, food):
#         print(f"Finding {food}...")
#         if food == 'deep fried pizza':
#             raise RuntimeError("Health warning!")
#         print(f"Taking {food}")
#
#     def close(self):
#         print("close fridge door.")

from contextlib import closing

class RefrigeratorRaider:
    def open(self):
        print("Open fridge door.")

    def take(self, food):
        print(f"Finding {food}...")
        if food == 'deep fried pizza':
            raise RuntimeError("Health warning!")
        print(f"Taking {food}")

    def close(self):
        print("close fridge door.")

def raid(food):
    with closing(RefrigeratorRaider()) as r:
        r.open()
        r.take(food)

if __name__ == "__main__":
    raid("deep fried pizza") ## It happend fridge to be a opend door
import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.cash = 0
        self.alive = True

    def to_work(self):
        if self.cash <= 2:
            print("time to work")
            self.progress += 0.06
            self.gladness -= 4
            self.cash += 150

    def to_study(self):
        if self.progress <= 1:
            print("time to study")
            self.progress += 0.12
            self.gladness -= 3

    def to_sleep(self):
        if self.gladness <= 1:
            print("time to sleep")
            self.gladness += 3

    def to_chill(self):
        if self.cash >= 50:
            print("time to rest")
            self.gladness += 5
            self.gladness -= 0.1
            self.cash -= 50

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out")
            self.alive = False
        elif self.gladness <= 0:
            print("Depresion...")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False

    def end_of_day(self):
        print(f"gladness = {self.gladness}")
        print(f"progress = {round(self.gladness)}")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1,4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_work()

        self.end_of_day()
        self.is_alive()

nick = Student("Nick")

for day in range(365):
     if nick.alive == False:
         break
     nick.live(day)


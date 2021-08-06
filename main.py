from tkinter import *
from math import *
import time
import math


class MovingCar:
    # Stores current drawing tool used
    drawing_tool = "dot"
    # Tracks whether left mouse is down
    left_but = "down"

    # Tracks x & y when the mouse is clicked and released
    x1_line_pt, y1_line_pt, x2_line_pt, y2_line_pt = None, None, None, None

    # for calculation
    counter, distance, distance_asli, dx, dy, torque = None, None, None, None, None, None
    input_torque = 1
    input_speed = 2

    # Car initial position
    x1_car, y1_car, x1_new_car, y1_new_car = 10, 25, 10, 25
    brake = False

    # ---------- CATCH MOUSE DOWN ----------
    def left_but_down(self, event=None):
        self.left_but = "down"

        # Set x & y when mouse is clicked
        self.x1_line_pt = event.x
        self.y1_line_pt = event.y

    # ---------- CATCH MOUSE UP ----------
    def left_but_up(self, event=None):
        self.left_but = "up"

        self.dot_draw(event)

    # ---------- DRAW DOT ----------

    def dot_draw(self, event=None):

        # Shortcut way to check if none of these values contain None
        if None not in (self.x1_line_pt, self.y1_line_pt):
            event.widget.create_rectangle(self.x1_line_pt, self.y1_line_pt, self.x1_line_pt, self.y1_line_pt, width=3,
                                          tag="gambar")

            self.x1_arr.append(self.x1_line_pt)
            self.y1_arr.append(self.y1_line_pt)
            self.x2_arr.append(self.x1_line_pt)
            self.y2_arr.append(self.y1_line_pt)

        print(self.x1_arr)
        print(self.y1_arr)
        print(self.x2_arr)
        print(self.y2_arr)

    # ---------- RESET ----------
    def clear_canvas(self, event=None):
        self.drawing_area.delete("gambar")

        # To delete all coordinate in array where clear all gambar
        del self.x1_arr[:]
        del self.x2_arr[:]
        del self.y1_arr[:]
        del self.y2_arr[:]

    def move(self, event=None):

        root.update()
        time.sleep(0.0001)
        self.drawing_area.delete("gambar2")

        dx_car = self.x1_new_car - self.x1_car
        dy_car = self.y1_new_car - self.y1_car
        crossproduct = (dx_car * self.dy) - (self.dx * dy_car)
        self.x1_car = self.x1_new_car
        self.y1_car = self.y1_new_car
        if crossproduct < 0:

            self.x1_new_car = self.x1_new_car + (1 + self.a) * math.cos(
                math.atan2(dy_car, dx_car) - math.radians(self.torque * 0.5))
            self.y1_new_car = self.y1_new_car + (1 + self.a) * math.sin(
                math.atan2(dy_car, dx_car) - math.radians(self.torque * 0.5))
            crossproduct = ((self.x1_new_car - self.x1_car) * (self.y1_arr[self.counter] - self.y1_car)) - (
                    (self.x1_arr[self.counter] - self.x1_car) * (self.y1_new_car - self.y1_car))
            if crossproduct >= 0:
                self.x1_car = self.x1_new_car
                self.y1_car = self.y1_new_car
                self.dx = self.x1_arr[self.counter] - self.x1_car
                self.dy = self.y1_arr[self.counter] - self.y1_car
                self.x1_new_car = self.x1_new_car + (1 + self.a) * math.cos(math.atan2(self.dy, self.dx))
                self.y1_new_car = self.y1_new_car + (1 + self.a) * math.sin(math.atan2(self.dy, self.dx))

        elif crossproduct > 0:

            self.x1_new_car = self.x1_new_car + (1 + self.a) * math.cos(
                math.atan2(dy_car, dx_car) + math.radians(self.torque * 0.5))
            self.y1_new_car = self.y1_new_car + (1 + self.a) * math.sin(
                math.atan2(dy_car, dx_car) + math.radians(self.torque * 0.5))
            crossproduct = ((self.x1_new_car - self.x1_car) * (self.y1_arr[self.counter] - self.y1_car)) - (
                    (self.x1_arr[self.counter] - self.x1_car) * (self.y1_new_car - self.y1_car))
            if crossproduct <= 0:
                self.x1_car = self.x1_new_car
                self.y1_car = self.y1_new_car
                self.dx = self.x1_arr[self.counter] - self.x1_car
                self.dy = self.y1_arr[self.counter] - self.y1_car
                self.x1_new_car = self.x1_new_car + (1 + self.a) * math.cos(math.atan2(self.dy, self.dx))
                self.y1_new_car = self.y1_new_car + (1 + self.a) * math.sin(math.atan2(self.dy, self.dx))

        else:
            self.dx = self.x1_arr[self.counter] - self.x1_car
            self.dy = self.y1_arr[self.counter] - self.y1_car
            self.x1_new_car = self.x1_new_car + (1 + self.a) * math.cos(math.atan2(self.dy, self.dx))
            self.y1_new_car = self.y1_new_car + (1 + self.a) * math.sin(math.atan2(self.dy, self.dx))

        self.drawing_area.create_rectangle(self.x1_new_car, self.y1_new_car, self.x1_new_car, self.y1_new_car, width=10,
                                           tag="gambar2")

    def animate(self, event=None):
        self.a = -1
        self.brake = False
        for self.counter in range(len(self.x1_arr)):
            flag = True
            self.torque = self.input_torque
            self.dx = self.x1_arr[self.counter] - self.x1_new_car
            self.dy = self.y1_arr[self.counter] - self.y1_new_car
            self.distance_asli = sqrt(self.dx * self.dx + self.dy * self.dy)
            while flag:
                if abs(int(self.x1_new_car) - self.x1_arr[self.counter]) <= 3 and abs(
                        int(self.y1_new_car) - self.y1_arr[self.counter]) <= 3:
                    break
                else:
                    print(self.a)
                    self.dx = self.x1_arr[self.counter] - self.x1_new_car
                    self.dy = self.y1_arr[self.counter] - self.y1_new_car
                    self.distance = sqrt(self.dx * self.dx + self.dy * self.dy)
                    if self.brake:

                        self.decelerate_brake()
                        if self.a < -0.8:
                            if self.counter > 0:
                                for x in range(self.counter):
                                    print(x)
                                    del self.x1_arr[x]
                                    del self.y1_arr[x]
                                    del self.x2_arr[x]
                                    del self.y2_arr[x]
                            break
                    else:

                        if len(self.x1_arr) - 1 == 0:
                            if self.distance_asli - self.distance <= 80:
                                self.accelerate()

                            elif self.distance < 100:
                                self.decelerate()
                        else:
                            if self.counter == 0:
                                self.accelerate()

                            if self.counter == len(self.x1_arr) - 1:
                                if self.distance < 100:
                                    self.decelerate()
                    self.move()

            if self.brake:
                break

        if self.brake == False:
            self.x1_car, self.y1_car = self.x1_new_car, self.y1_new_car
            self.clear_canvas()

    def brake_button(self, event=None):
        self.brake = True

    def decelerate(self, event=None):
        if self.a > -0.5:
            self.a = self.a - 0.05

    def decelerate_brake(self, event=None):
        if self.a > -1:
            self.a = self.a - 0.005

    def accelerate(self, event=None):
        if self.a <= self.input_speed:
            self.a = self.a + 0.005

    def change_torque(self, event=None):
        newwin = Toplevel(root)

        e = Entry(newwin)
        e.pack()
        e.focus_set()

        def changeIT():
            self.input_torque = int(e.get())
            newwin.destroy()

        button1 = Button(newwin, text="change", command=changeIT)
        button1.pack()

    def change_speed(self, event=None):
        newwin = Toplevel(root)

        e = Entry(newwin)
        e.pack()
        e.focus_set()

        def changeIT():
            self.input_speed = int(e.get())
            newwin.destroy()

        button1 = Button(newwin, text="change", command=changeIT)
        button1.pack()

    def __init__(self, root):
        width = 1000
        height = 600
        self.drawing_area = Canvas(root, width=width, height=height)
        self.drawing_area.pack()
        self.drawing_area.bind("<ButtonPress-1>", self.left_but_down)
        self.drawing_area.bind("<ButtonRelease-1>", self.left_but_up)

        B_car = Button(root, text="Drive", command=self.animate, state=ACTIVE)
        B_car.pack(side=LEFT, padx=10, pady=10, ipadx=5, ipady=5)

        B_stop = Button(root, text="Brake", command=self.brake_button, state=ACTIVE)
        B_stop.pack(side=LEFT, padx=10, pady=10, ipadx=5, ipady=5)

        B_clear = Button(root, text="Clear Canvas", command=self.clear_canvas, state=ACTIVE)
        B_clear.pack(side=LEFT, padx=10, pady=10, ipadx=5, ipady=5)

        B_Torque = Button(root, text="Change Torque", command=self.change_torque, state=ACTIVE)
        B_Torque.pack(side=LEFT, padx=10, pady=10, ipadx=5, ipady=5)

        B_Speed = Button(root, text="Change Speed", command=self.change_speed, state=ACTIVE)
        B_Speed.pack(side=LEFT, padx=10, pady=10, ipadx=5, ipady=5)

        # Save coordinate into array
        self.x1_arr = []
        self.x2_arr = []
        self.y1_arr = []
        self.y2_arr = []

        self.car = self.drawing_area.create_rectangle(self.x1_car, self.y1_car, self.x1_car, self.y1_car, width=10,
                                                      tag="gambar2")


root = Tk()

moving_car = MovingCar(root)

root.mainloop()

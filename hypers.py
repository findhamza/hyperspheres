import tkinter as tk
import numpy as np
import math
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Application(tk.Frame):
    label_text = ['Points', 'Roh', 'Theta', 'Phi']
    g_points = g_roh = g_theta = g_phi = 0

    def __init__(self, master=None):
        super().__init__(master)
        master.title('Hello')
        # master.geometry("500x300")
        self.master = master
        self.create_widgets()

    # noinspection PyAttributeOutsideInit
    def create_widgets(self):
        row_num = 0
        for lable in self.label_text:
            tk.Label(text=lable, relief=tk.RIDGE, width=15).grid(row=row_num, column=0, padx=(20, 5), pady=(5, 15))
            row_num += 1

        self.amount_entry = tk.Entry()
        self.amount_entry.grid(row=0, column=1, padx=(5, 20), pady=(5, 15))
        self.roh_entry = tk.Entry()
        self.roh_entry.grid(row=1, column=1, padx=(5, 20), pady=(5, 15))
        self.theta_entry = tk.Entry()
        self.theta_entry.grid(row=2, column=1, padx=(5, 20), pady=(5, 15))
        self.phi_entry = tk.Entry()
        self.phi_entry.grid(row=3, column=1, padx=(5, 20), pady=(5, 15))
        scatter_2d = tk.Button(text="2D Scatter Plot", command=self.init_2d).grid(row=4, column=1,
                                                                                  padx=(5, 20),
                                                                                  pady=(5, 15))
        scatter_2d = tk.Button(text="3D Scatter Plot", command=self.create_3d).grid(row=5, column=1, padx=(5, 20),
                                                                                    pady=(5, 15))

    def init_2d(self):
        self.g_points = int(self.amount_entry.get())
        self.g_roh = float(self.roh_entry.get())
        self.g_theta = float(self.theta_entry.get())
        self.create_2d()

    def create_2d(self):
        print(self.g_points)
        points = self.g_points
        roh = self.g_roh
        theta = self.g_theta
        plots = Scatter2d(points, roh)
        x_list = plots.get_x()[:points]
        y_list = plots.get_y()[:points]
        graph = ScatterPlot(x_list, y_list)
        graph.draw()
        del plots, graph, x_list, y_list

    def create_3d(self):
        print("2D Scatter")


class ScatterPlot(object):
    def __init__(self, x, y, z=0):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.x = x
        self.y = y
        self.z = z
        self.config_ax()

    def config_ax(self):
        self.ax.scatter(self.x, self.y, self.z, c='r', marker='.')
        self.ax.set_xlim(-2, 2)
        self.ax.set_ylim(-2, 2)
        self.ax.set_zlim(-2, 2)
        self.ax.set_xlabel('X Label')
        self.ax.set_ylabel('Y Label')
        self.ax.set_zlabel('Z Label')

    def draw(self):
        self.fig.show()


class Scatter2d(object):
    x = []
    y = []

    def __init__(self, amount, roh, theta=math.pi * 2):
        self.amount = amount
        self.roh = roh
        self.theta = theta
        self.randroh()
        self.randtheta()
        self.points()

    #    def __init__(self, amount, roh):
    #        self.amount = amount
    #        self.roh = roh

    def randroh(self):
        new_roh = random.uniform(-self.roh, self.roh)
        return new_roh

    def randtheta(self):
        try:
            self.theta
        except NameError:
            new_theta = math.pi * 2 * random.random()
        else:
            new_theta = random.uniform(0, self.theta)
        return new_theta

    def points(self):
        for i in range(self.amount):
            roh_val = self.randroh()
            theta_val = self.randtheta()
            self.x.insert(0, (roh_val * math.cos(theta_val)))
            self.y.insert(0, (roh_val * math.sin(theta_val)))

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def reset(self):
        self.x = []
        self.y = []
        self.amount = 0
        self.roh = 0


root = tk.Tk()
app = Application(master=root)
app.mainloop()

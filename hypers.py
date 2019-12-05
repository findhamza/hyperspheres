"""
Author: Hamza Syed
12/04/2019

Purpose:    This project was made to uniformly sample disk and spheres
"""
import tkinter as tk
import numpy as np
import math
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
Class Application

Purpose:    To establish UI which would allow for the user to modify parameters of of either a disk or a sphere in 
            which points would be randomly distributed. 
"""


class Application(tk.Frame):
    """Establishes labels as well as class global variables to store user inputs"""
    label_text = ['Points', 'Radius / Roh', 'Theta', 'Phi']
    g_points = g_roh = g_theta = g_phi = 0

    """
    Application constructor:
            -Establishes title
            -Defines master
            -Calls on create_widgets() to create GUI
    """

    def __init__(self, master=None):
        super().__init__(master)
        master.title('Hyper Sphere Dist.')
        self.master = master
        self.create_widgets()

    """
    Method create_widgets:
        Purpose: To create GUI
    
        -Utilizes label_text list to create labels in GUI
        -Creates ranged scales to allow user parameters
        -Button scatter_2d calls on init_2d to start uniform disk generation
        -Button scatter_3d calls on init_3d to start uniform sphere generation
    """

    # noinspection PyAttributeOutsideInit
    def create_widgets(self):
        row_num = 0
        for lable in self.label_text:
            tk.Label(text=lable, relief=tk.RIDGE, width=15).grid(row=row_num, column=0, padx=(20, 5), pady=(5, 15))
            row_num += 1

        self.amount_entry = tk.Scale(from_=0, to=9999, orient='horizontal', resolution=100, length=160)
        self.amount_entry.grid(row=0, column=1, padx=(5, 20), pady=(5, 32))
        self.amount_entry.set(4000)
        self.roh_entry = tk.Scale(from_=0, to=10, orient='horizontal', resolution=0.1, length=160)
        self.roh_entry.grid(row=1, column=1, padx=(5, 20), pady=(5, 32))
        self.roh_entry.set(10)
        self.theta_entry = tk.Scale(from_=0, to=(2 * math.pi), orient='horizontal', resolution=0.01, length=160)
        self.theta_entry.grid(row=2, column=1, padx=(5, 20), pady=(5, 32))
        self.theta_entry.set(2 * math.pi)
        self.phi_entry = tk.Scale(from_=0, to=math.pi, orient='horizontal', resolution=0.01, length=160)
        self.phi_entry.grid(row=3, column=1, padx=(5, 20), pady=(5, 32))
        self.phi_entry.set(math.pi)
        scatter_2d = tk.Button(text="2D Scatter Plot", command=self.init_2d).grid(row=4, column=1,
                                                                                  padx=(5, 20),
                                                                                  pady=(5, 15))
        scatter_2d = tk.Button(text="3D Scatter Plot", command=self.init_3d).grid(row=5, column=1, padx=(5, 20),
                                                                                  pady=(5, 15))

    """
    Method init_2d:
        Purpose: To gather user set parameters and save them to global variables, then to actually create uniform disk
    """

    def init_2d(self):
        self.g_points = int(self.amount_entry.get())
        self.g_roh = float(self.roh_entry.get())
        self.g_theta = float(self.theta_entry.get())
        self.create_2d()

    """
    Method init_3d:
        Purpose: To gather user set parameters and save them to global variables, then to actually create uniform sphere
    """

    def init_3d(self):
        self.g_points = int(self.amount_entry.get())
        self.g_roh = float(self.roh_entry.get())
        self.g_theta = float(self.theta_entry.get())
        self.g_phi = float(self.phi_entry.get())
        self.create_3d()

    """
    Method create_2d:
        Purpose: Pass gathered user info to Scatter2d to scatterPlot
        
        -Gathers user set parameters
        -Passes collected parameters to Scatter2d
        -Gathers returned x and y list (coordinates)
        -Passes collected coordinates to be drawn by ScatterPlot
        -Deletes Scatter2d and ScatterPlot and coordinates lists
    """

    def create_2d(self):
        points = self.g_points
        roh = self.g_roh
        theta = self.g_theta
        plots = Scatter2d(points, roh, theta=theta)
        x_list = plots.get_x()[:points]
        y_list = plots.get_y()[:points]
        graph = ScatterPlot(x_list, y_list)
        graph.draw()
        del plots, graph, x_list, y_list

    """
    Method create_3d:
        Purpose: Pass gathered user info to Scatter3d to scatterPlot
        
        -Gathers user set parameters
        -Passes collected parameters to Scatter3d
        -Gathers returned x, y, and z list (coordinates)
        -Passes collected coordinates to be drawn by ScatterPlot
        -Deletes Scatter3d and ScatterPlot and coordinates lists
    """

    def create_3d(self):
        points = self.g_points
        roh = self.g_roh
        theta = self.g_theta
        phi = self.g_phi
        plots = Scatter3d(points, roh, theta=theta, phi=phi)
        x_list = plots.get_x()[:points]
        y_list = plots.get_y()[:points]
        z_list = plots.get_z()[:points]
        graph = ScatterPlot(x_list, y_list, z=z_list)
        graph.draw()
        del plots, graph, x_list, y_list, z_list


"""
Class ScatterPlot

Purpose:    Utilizes Matplotlib to construct scatter plot of passed coordinates 
"""


class ScatterPlot(object):
    """
    ScatterPlot constructor:
            -Establishes figure from Matplotlib on which the coordinates wil be drawn
            -Gathers all the variables passed to it and stores it with its instance
            -If no z is passed, it is assumed that only x and y axis are utilized
                -In case of of no z, z coordinate is set to 0
            -calls on config_ax() to set figure axis range, labels, and coordinates
    """

    def __init__(self, x, y, z=[0]):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.x = x
        self.y = y
        self.z = z
        self.config_ax()

    """
        Method config_ax:
        Purpose: Set figures axis range and labels
        
        -Uses the passed coordinates to create points
        -Sets x, y, and z range from -10 to 10
        -Labels the axis
    """

    def config_ax(self):
        self.ax.scatter(self.x, self.y, self.z, c='r', marker='.', s=1)
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.set_zlim(-10, 10)
        self.ax.set_xlabel('X Axis')
        self.ax.set_ylabel('Y Axis')
        self.ax.set_zlabel('Z Axis')

    """
        Method draw:
        Purpose: Draws the collected coordinates to screen
        
        -Draws the collected coordinates to screen
    """

    def draw(self):
        self.fig.show()


"""
Class Scatter2d

Purpose:    Uses the users defined parameters to create coordinate list which it would return 
"""


class Scatter2d(object):
    """Establishes x and y class global list to store coordinate pairs"""
    x = []
    y = []

    """
    Scatter2d constructor:
            -Gates user set parameters
            -Amount establishes amount of coordinates to be generated
            -Roh defines r, the magnitude from origin (0,0)
            -Theta is 2pi by default unless specified otherwise
            -Calls points() to start generating coordinates
    """

    def __init__(self, amount, roh, theta=math.pi * 2):
        self.amount = amount
        self.roh = roh
        self.theta = theta
        self.points()

    """
        Method randroh:
        Purpose: Return random roh within user defined parameters
    """

    def randroh(self):
        new_roh = self.roh * (random.uniform(0, 1) ** (1 / 2))
        return new_roh

    """
        Method randtheta:
        Purpose: Return random theta within user defined parameters
    """

    def randtheta(self):
        new_theta = self.theta * random.uniform(0, 1)
        return new_theta

    """
        Method points: 
            Purpose:    Using randroh() and randtheta(), adds to coordinates list uniformly distributed 
                        points within user parameters 
            
            -Loops amount of times as many points as user wants
            -Gets random roh and theta within threshold
            -Gets x and y values using trig
            -Inserts to coordinate list the generated coordinates
    """

    def points(self):
        for i in range(self.amount):
            roh_val = self.randroh()
            theta_val = self.randtheta()
            x_val = roh_val * math.cos(theta_val)
            y_val = roh_val * math.sin(theta_val)
            self.x.insert(0, x_val)
            self.y.insert(0, y_val)

    """
        Method get_x: 
            Purpose: Returns list of x coordinates
    """

    def get_x(self):
        return self.x

    """
        Method get_y: 
            Purpose: Returns list of y coordinates
    """

    def get_y(self):
        return self.y

    """
        Method reset: 
            Purpose: resets x and y list as well as amount and roh variables
    """

    def reset(self):
        self.x = []
        self.y = []
        self.amount = 0
        self.roh = 0


"""
Class Scatter3d

Purpose:    Uses the users defined parameters to create coordinate list which it would return 
"""


class Scatter3d(object):
    """Establishes x, y and z class global list to store coordinate pairs"""
    x = []
    y = []
    z = []

    """
    Scatter3d constructor:
            -Gates user set parameters
            -Amount establishes amount of coordinates to be generated
            -Roh defines r, the magnitude from origin (0,0)
            -Theta is 2pi by default unless specified otherwise
            -Phi is pi by default unless specified otherwise
            -Calls points() to start generating coordinates
    """

    def __init__(self, amount, roh, theta=math.pi * 2, phi=math.pi):
        self.amount = amount
        self.roh = roh
        self.theta = theta
        self.phi = phi
        self.points()

    """
        Method randroh:
        Purpose: Return random roh within user defined parameters
    """

    def randroh(self):
        new_roh = self.roh * (random.uniform(0, 1) ** (1 / 3))
        return new_roh

    """
        Method randtheta:
        Purpose: Return random theta within user defined parameters
    """

    def randtheta(self):
        new_theta = self.theta * random.uniform(0, 1)
        return new_theta

    """
        Method randphi:
        Purpose: Return random phi within user defined parameters
    """

    def randphi(self):
        new_phi = math.acos(2 * random.uniform(0, 1) - 1)
        while new_phi > self.phi or new_phi < -self.phi:
            new_phi = math.acos(2 * random.uniform(0, 1) - 1)
        return new_phi

    """
        Method points: 
            Purpose:    Using randroh(), randtheta(), and randphi(), adds to coordinates list uniformly distributed 
                        points within user parameters 
            
            -Loops amount of times as many points as user wants
            -Gets random roh, theta, and phi within threshold
            -Gets x, y, and z values using trig
            -Inserts to coordinate list the generated coordinates
    """

    def points(self):
        for i in range(self.amount):
            roh_val = self.randroh()
            theta_val = self.randtheta()
            phi_val = self.randphi()
            sin_theta = math.sin(theta_val)
            cos_theta = math.cos(theta_val)
            sin_phi = math.sin(phi_val)
            cos_phi = math.cos(phi_val)
            x_val = roh_val * cos_theta * sin_phi
            y_val = roh_val * sin_theta * sin_phi
            z_val = roh_val * cos_phi
            self.x.insert(0, x_val)
            self.y.insert(0, y_val)
            self.z.insert(0, z_val)

    """
        Method get_x: 
            Purpose: Returns list of x coordinates
    """

    def get_x(self):
        return self.x

    """
        Method get_y: 
            Purpose: Returns list of y coordinates
    """

    def get_y(self):
        return self.y

    """
        Method get_z: 
            Purpose: Returns list of z coordinates
    """

    def get_z(self):
        return self.z

    """
        Method reset: 
            Purpose: resets x, y, and z list as well as amount and roh variables
    """

    def reset(self):
        self.x = []
        self.y = []
        self.z = []
        self.amount = 0
        self.roh = 0


"""
Program Start

Purpose:    Creates TKinter object for GUI and starts the TKinter loop to keep it displayed and running
"""

root = tk.Tk()
app = Application(master=root)
app.mainloop()

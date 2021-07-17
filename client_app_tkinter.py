import tkinter as tk
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation


class Test:

    def __init__(self, testt):
        self.a = testt

def get_animated_plot(plot_name, data_filename, root):
    # Create figure for plotting
    fig, ax = plt.subplots()
    xs = []
    ys = []

    def animate(i, xs: list, ys: list):
        with open(data_filename, 'r') as file:
            data = file.read()

        if len(xs) < 10:
            flt = int(data.split("__")[0])
            # Add x and y to lists
            xs.append(dt.datetime.now().strftime('%H:%M:%S'))
            ys.append(flt)
        else:
            xs.append(dt.datetime.now().strftime('%H:%M:%S'))
            xs = xs[-10:]
            yss = data.split('__')
            print(yss)
            yss.reverse()
            try:
                ys = [int(i) for i in yss]
            except:
                print(yss)
        # Draw x and y lists
        ax.clear()
        ax.plot(xs, ys)
        # Format plot
        ax.set_ylim([0, 100])
        # plt.xticks(rotation=45, ha='right')
        # plt.subplots_adjust(bottom=0.20)
        ax.set_title(plot_name)
        ax.set_xlabel('Date Time (hour:minute:second)')
        ax.set_ylabel('Sensor data')

    # Set up plot to call animate() function every 1000 milliseconds
    bar1 = FigureCanvasTkAgg(fig, root)
    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

    return animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)




root = tk.Tk()

ani1 = get_animated_plot('random_1', 'random_1', root)
ani2 = get_animated_plot('random_2', 'random_2', root)
ani3 = get_animated_plot('random_3', 'random_3', root)


root.mainloop()


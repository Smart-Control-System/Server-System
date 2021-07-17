# plot_web_api_realtime.py
"""
A live auto-updating plot of random numbers pulled from a web API
"""

import time
import datetime as dt
import requests
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

import multiprocessing


def plott():
    # Create figure for plotting
    fig, ax = plt.subplots()
    xs = []
    ys = []

    def animate(i, xs: list, ys: list):
        with open('all_queries.json', 'r') as file:
            data = file.read()

        if len(xs) < 10:
            flt = int(data.split("__")[0])
            # Add x and y to lists
            xs.append(dt.datetime.now().strftime('%H:%M:%t'))
            ys.append(flt)
        else:
            xs = xs[-10:]
            yss = data.split('__')
            yss.reverse()
            ys = [int(i) for i in yss]
        # Draw x and y lists
        ax.clear()
        ax.plot(xs, ys)
        # Format plot
        ax.set_ylim([0, 100])
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.20)
        ax.set_title('Plot of random numbers from https://qrng.anu.edu.au')
        ax.set_xlabel('Date Time (hour:minute:second)')
        ax.set_ylabel('Random Number')

    # Set up plot to call animate() function every 1000 milliseconds
    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=500)

    plt.show()

plott()
# if __name__ == "__main__":
#     plot_thread = multiprocessing.Process(target=plott)
#     plot_thread.start()
#     print('plots started')
#
#
#     server_thread = multiprocessing.Process(target=server.main)
#     server_thread.start()
#     print('server started')

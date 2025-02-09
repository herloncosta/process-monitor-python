import psutil
import time
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from collections import deque


def process_monitor(interval=2, max_points=30):
    ctime = deque(maxlen=max_points)
    cpu_data = deque(maxlen=max_points)
    mem_data = deque(maxlen=max_points)

    plt.ion()
    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(10, 8))
    # fig.suptitle('Process Monitor')
    fig.canvas.manager.set_window_title('Process Monitor')
    fig.canvas.toolbar.pack_forget()
    fig.canvas.toolbar = None

    for ax in [ax1, ax2]:
        ax.set_xlabel("Time (s)")
        ax.grid(True)
                    
    ax1.set_ylabel("CPU Usage (%)")
    ax2.set_ylabel("Memory Usage (MB)")

    try:
        time_counter = 0
        while True:
            total_cpu_usage = psutil.cpu_percent(interval=None)
            total_memory_usage = psutil.virtual_memory().used

            ctime.append(time_counter)
            cpu_data.append(total_cpu_usage)
            mem_data.append(total_memory_usage)

            ax1.plot(ctime, cpu_data, label="CPU Usage", color="r")
            ax2.plot(ctime, mem_data, label="Memory Usage", color="b")

            ax1.relim()
            ax1.autoscale_view()
            ax2.relim()
            ax2.autoscale_view()

            fig.canvas.draw()
            fig.canvas.flush_events()

            ax1.clear()
            ax2.clear()

            ax1.set_xlabel("Time (s)")
            ax1.set_ylabel("CPU Usage (%)")
            ax1.grid(True)
            ax2.set_xlabel("Time (s)")
            ax2.set_ylabel("Memory Usage (MB)")
            ax2.grid(True)

            time_counter += interval
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Monitoring stopped")


if __name__ == "__main__":
    process_monitor()

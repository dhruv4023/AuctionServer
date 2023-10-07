
import threading


def set_interval(func, interval=60*60*24*30):
    # Define a wrapper function that schedules the function to run periodically
    def interval_function():
        func()
        # Schedule the next execution after the specified interval
        threading.Timer(interval, interval_function).start()

    func()
    threading.Timer(interval, interval_function).start()

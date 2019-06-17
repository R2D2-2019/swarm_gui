from time import sleep
from sys import platform
import signal

from client.comm import Comm
from modules.template.module.mod import Module

should_stop = False


def main():
    print("Starting application...\n")
    GUI = Module(Comm())
    print("Module created...")

    while not should_stop:
        GUI.process()
        sleep(0.05)

    GUI.stop()


def stop(signal, frame):
    global should_stop
    should_stop = True


signal.signal(signal.SIGINT, stop)
signal.signal(signal.SIGTERM, stop)

if platform != "win32":
    signal.signal(signal.SIGQUIT, stop)

if __name__ == "__main__":
    main()

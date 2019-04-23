import curses
import time

def pbar(window):
	for i in range(10):
		window.addstr(10, 10, "10, 10 [" + ("=" * i) + ">" + (" " * (10 - i)) + "]")
		window.addstr(1, 10, "1, 10[" + ("=" * i) + ">" + (" " * (10 - i)) + "]")
		window.refresh()
		time.sleep(0.5)

curses.wrapper(pbar)

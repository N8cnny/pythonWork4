s = "Results:\n"  # declare s string

# example 1
x = 21
s += str(x) + "\n"  # + concateneates

# example 2
x = 12**2
s += str(x/2) + "\n"

# example 3
y = 4.35
s += str(y*2) + "\n"

# example 4
s += str(5.231 * 6.172 * 29) + "\n"

# example 5
s += str(2 + 6) + "\n"

# example 6
s += str((3 + 1j) * (3 - 1j)) + "\n"

# example 7
s += str(22/  7) + "\n"

###### Message Box Code ######
from tkinter import *
root = Tk()
root.title('Message Box')
Label(root, justify=LEFT, text=s).grid(padx=10, pady=10)

root.mainloop()





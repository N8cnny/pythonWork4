import InputBox
InputBox.ShowDialog("Enter the 1st Fahrenheit value:")
f = InputBox.GetInput()
c1 = (float(f) - 32) * (5/9)

InputBox.ShowDialog("Enter the 2nd Fahrenheit value:")
f = InputBox.GetInput()
c2 = (float(f) - 32) * (5/9)

import MessageBox
MessageBox.Show(str(c1) + "\n" + str(c2))

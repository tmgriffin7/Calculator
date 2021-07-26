from tkinter import Tk, Entry, Label, Button
from tkinter.font import Font

def main():
  wn = Tk()
  wn.title("Calculator")

  fontStyle = Font(family='Courier', size=20)

  entryExp = Entry(master=wn, width=20, font=fontStyle)
  labelEq = Label(master=wn, text=" = ", font=fontStyle)
  labelResult = Label(master=wn, text='0', font=fontStyle)
  buttonCalc = Button(master=wn, text="Calculate", font=fontStyle,
                      command=lambda : calculate(entryExp, labelResult))

  entryExp.grid(row=0, column=0)
  labelEq.grid(row=0, column=1)
  labelResult.grid(row=0, column=2)
  buttonCalc.grid(row=1)

  wn.mainloop()


def calculate(expression, labelResult):
  """Evaluate the expression in the entry widget.
  Update the label with the result on row 0.
  """

  e = expression.get()
  result = eval(e)
  labelResult['text'] = result


if __name__ == '__main__':
  main()

from tkinter import *
from tkinter import ttk
from area import *
from perimeter import *

# num = IntVar()
# num.set(0)

root = Tk()
root.title('Area Or Perimeter')
root.geometry("500x400")

# lists of shapes and options
mathoptions = [
    "Area",
    "Perimeter",
]

Pshapeoptions = [
    "Circle",
    "Square",
    "Rectangle",
    "Triangle"

]

Ashapeoptions = [
    "Circle",
    "Square",
    "Rectangle",
    "Triangle",
    "Trapezoid"
]


# shape selection

def pick_shape(a):
    if my_formula.get() == "Area":
        my_shape.config(value=Ashapeoptions)
        my_shape.current(0)
    #         if my_shape.get() == "Circle":
    #
    #         if my_shape.get() == "Square":
    #         if my_shape.get() == "Rectangle":
    #         if my_shape.get() == "Triangle":
    #         if my_shape.get() == "Trapezoid":
    #         if my_shape.get() == "Curve":

    if my_formula.get() == "Perimeter":
        my_shape.config(value=Pshapeoptions)
        my_shape.current(0)


#         if my_shape.get() == "Circle":
#         if my_shape.get() == "Square":
#         if my_shape.get() == "Rectangle":
#         if my_shape.get() == "Triangle":


# box entries to plug in numbers

# def ans(b):
#     if my_shape.get() == "Circle":
#     if my_shape.get() == "Square":
#     if my_shape.get() == "Rectangle":
#     if my_shape.get() == "Triangle":
#     if my_shape.get() == "Trapezoid":
#     if my_shape.get() == "Curve":


# dropbox for formula

my_formula = ttk.Combobox(root, value=mathoptions)
my_formula.current(0)
my_formula.pack(pady=20)

# dropbox for shape

my_shape = ttk.Combobox(root, value=[" "])
my_shape.current(0)
my_shape.pack(pady=20)

# bind combobox (make sure something happens after clicking)

my_formula.bind("<<ComboboxSelected>>", pick_shape)

# my_shape.bind("<<ComboboxSelected>>", ans)
# number box entries

# self.frame_first = Frame(self.root)
# self.label_first = Label(self.frame_first)
# self.entry_first = Entry(self.frame_first, width=40)
# self.label_first.pack(padx=20, side='left')
# self.entry_first.pack(padx=20, side='left')
# self.frame_first.pack(anchor='w', pady=10)
# self.entry_first.pack_forget()

# frames

my_frame = Frame(root)
my_frame.pack(pady=50)

# compute button

# frame_button = Frame(root)
# button_compute = Button(frame_button, text='COMPUTE', command=compute)
# button_compute.pack(pady=10)
# frame_button.pack()

# def compute():
#     try:
#         first_num = entry_first.get()
#         second_num = entry_second.get()
#         third_num = entry_third.get()
#         shape = num.get()
#         
#         if shape == 1:
#             label_result.config(text=f'Circle area = {area.circle(first_num)}')
#         elif shape == 2:
#             label_result.config(text=f'Square area = {area.square(first_num)}')
#         elif shape == 3:
#             label_result.config(text=f'Rectangle area = {area.rectangle(first_num, second_num)}')
#         elif shape == 4:
#             label_result.config(text=f'Triangle area = {area.triangle(first_num, second_num)}')
#         #Trapezoid and Curve
#         elif shape == 5:
#             label_result.config(text=f'Trapezoid area = {area.trapezoid(first_num, second_num, third_num)}')
#         elif shape == 6:
#             label_result.config(text=f'Area under the curve = {area.curve(first_num, second_num, third_num)}')
#         else:
#             label_result.config(text='No operation selected')
#     except ValueError:
#         label_result.config(text='Enter numeric values')
#     except TypeError:
#         label_result.config(text='Values must be positive')

# results

'''
I tried... I really did...
'''

root.mainloop()
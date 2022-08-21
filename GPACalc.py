from tkinter import *
from course_data import course_list, grade_scale
from kivy.app import App


root = Tk()
root.geometry("500x200")


def GPA_calculator():
    grades_list = []
    total_credits = 0
    for item in course_list:
        grades_list.append(grade_scale[item['grade']] * item['credits'])
        total_credits += item['credits']
    total_grades = sum(grades_list)
    GPA = '{0:.2f}'.format(total_grades/total_credits)
    end_result = Label(
        root, text=f"GPA: {GPA} \n Total Credits: {total_credits}")
    end_result.pack()


my_button = Button(root, text='GPA', command=GPA_calculator)
my_button.pack()

root.mainloop()

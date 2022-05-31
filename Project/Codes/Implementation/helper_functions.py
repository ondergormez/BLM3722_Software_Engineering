import helper_functions
import person
import student
import worker
import teacher
import registrar
import systemAdmin
import information_system
import course
import classroom
import school_branch
import datetime
import getpass


def print_star(num_stars: int):
    for _ in range(num_stars):
        print('*', end="")
    print('\n')


def print_main_menu():
    print(f"{'1) Login as system administrator'} \n2) Login as course registrar")


def print_system_admin_menu():
    print(f"{'1) Create new branch'}")


def print_course_registrar_menu():
    print(f"{'1) Student registration'}")


def print_student_list(student_list: list):
    list_len = len(student_list)
    for list_ind in range(list_len):
        student.Student.display_student(student_list[list_ind])

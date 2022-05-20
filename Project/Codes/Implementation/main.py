import person
import student
import worker
import teacher
import registrar
import course
import classroom
import school_branch
import datetime
import information_system
import create_data


# classroom_name = "A134"
# classroom_capacity = 32
# classroom1 = classroom.Classroom(classroom_name, classroom_capacity)

# name = "Russian"
# capacity = 32
# student_count = 24
# level = "Beginner"
# course_teacher = create_data.teacher1
# course_class1 = classroom_name
# date = ("Monday", "12:00")
# course1 = course.Course(name, capacity, level,
#                         course_teacher, course_class1, date)
# print(course1)
# course1.add_student(create_data.student1)
# course1.add_student(create_data.student2)
# course1.show_students()
# print(course1)
# course1.delete_student(create_data.student1)
# course1.show_students()
# print(course1)
# course1.add_student(create_data.student1)
# course1.show_students()
# print(course1)

# name = "Russian"
# capacity = 32
# student_count = 24
# level = "Advanced"
# course_teacher = create_data.teacher1
# course_class2 = classroom1.name
# date = ("Monday", "14:00")
# course2 = course.Course(name, capacity, level,
#                         course_teacher, course_class2, date)


# print(course2)
# course2.add_student(create_data.student1)
# course2.add_student(create_data.student2)
# course2.show_students()
# print(course2)
# course2.delete_student(create_data.student1)
# course2.show_students()
# print(course2)
# course2.add_student(create_data.student1)
# course2.show_students()
# print(course2)

# classroom1.add_course(course1)
# classroom1.show_courses()
# classroom1.add_course(course2)
# classroom1.show_courses()
# classroom1.delete_course(course1)
# classroom1.show_courses()

# # if (course1.check_course_time(course2)):
# #     print("ÇAKIŞMA")
# # else:
# #     print("ÇAKIŞMA YOK")


# # print(f"course1 id: {id(course1)}")
# # print(f"course2 id: {id(course2)}")
# # print(f"course1.student_list id: {id(course1.student_list)}")
# # print(f"course2.student_list id: {id(course2.student_list)}")

# classroom_name = "A135"
# classroom_capacity = 32
# classroom2 = classroom.Classroom(classroom_name, classroom_capacity)

# branch_name = "Maslak"
# branch_address = "Ayazağa, 34/2"
# id_num = "543463"
# public_transport = "41AT, 500T, 41ST"
# private_transport = ["E6 Otoyolu", "E5 Otoyolu"]
# social_benefits = ["Langırt", "PS5"]
# branch1 = school_branch.SchoolBranch(
#     branch_name, id_num, branch_address, public_transport, private_transport, social_benefits)

# branch1.add_classroom(classroom1)
# branch1.show_classrooms()
# branch1.add_classroom(classroom2)
# branch1.show_classrooms()
# branch1.delete_classroom(classroom2)
# branch1.show_classrooms()


# create_data.registrar1.add_student_to_course(create_data.student1, course1)


# create_data.registrar1.add_student_to_course(create_data.student3, course1)
# course1.show_students()

# create_data.registrar1.register_payment(create_data.student1, "English")
# print(create_data.student1.payment_infos)

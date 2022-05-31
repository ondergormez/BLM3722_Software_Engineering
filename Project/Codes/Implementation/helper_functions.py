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

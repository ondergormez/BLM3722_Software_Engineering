class InformationSystem():

    def __init__(self, total_users: int, total_branches: int):
        self.total_users = total_users
        self.total_branches = total_branches
        self.worker_list = []
        self.teacher_list = []
        self.student_list = []
        self.branch_list = []

    def get_teacher_list(self) -> list:
        return self.teacher_list

    # def find_teacher(self, teacher)

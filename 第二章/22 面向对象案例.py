class Student:
    def __init__(self, name, Chinese, Math, English):
        self.name = name
        self.Chinese = Chinese
        self.Math = Math
        self.English = English

    def __str__(self):
        return f"姓名:{self.name} | 语文:{self.Chinese} | 数学：{self.Math} | 英语：{self.English}"

    # 修改成绩，可以单独传某一科
    def update_score(self, Chinese=None, Math=None, English=None):
        if Chinese is not None:
            self.Chinese = Chinese
        if Math is not None:
            self.Math = Math
        if English is not None:
            self.English = English


# 教务管理系统类
class EduManagement:
    system_version = "1.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = []

    # 添加学生成绩
    def add_student(self):
        name = input("请输入学生姓名：")
        # 判断学生姓名是否存在，如果存在，则添加失败（不能重复添加）
        for s in self.student_list:
            if s.name == name:
                print("该学生已存在，添加失败！")
                return
        Chinese = int(input("请输入学生语文成绩："))
        Math = int(input("请输入学生数学成绩："))
        English = int(input("请输入学生英语成绩："))

        # 判断分数是否在 0-100之间
        if 0 <= Chinese <= 100 and 0 <= Math <= 100 and 0 <= English <= 100:
            stu = Student(name, Chinese, Math, English)
            self.student_list.append(stu)
            print("学生信息添加成功")
        else:
            print("各科成绩必须得在 0-100之间！")

    # 修改学生成绩
    def update_student(self):
        name = input("请输入要修改的学生姓名：")
        # 根据学生姓名找到学生的信息
        for s in self.student_list:
            if s.name == name:
                print(f"当前成绩：{s}")
                Chinese = int(input("请输入学生语文成绩："))
                Math = int(input("请输入学生数学成绩："))
                English = int(input("请输入学生英语成绩："))
                # 判断分数是否在0-100之间
                if 0 <= Chinese <= 100 and 0 <= Math <= 100 and 0 <= English <= 100:
                    s.update_score(Chinese=Chinese, Math=Math, English=English)
                    print("成绩修改成功")
                    print(f"修改后的成绩为：{s}")
                    return
                else:
                    print("各科成绩必须在0-100之间")
                    return
        print("未找到该学生，修改失败！")

    # 删除学生成绩
    def delete_student(self):
        name = input("请输入要删除的学生姓名：")
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("学生信息删除成功")
                return
        print("未找到该学生，删除失败！")

    # 查询学生成绩
    def query_student(self):
        name = input("请输入要查询的学生姓名：")
        for s in self.student_list:
            if s.name == name:
                print(f"学生信息：{s}")
                return
        print("未找到该学生！")

    # 显示全部学生成绩
    def list_student(self):
        for s in self.student_list:
            print(s)

    # 运行系统
    def run(self):
        print(f"欢迎使用教务管理系统 V{EduManagement.system_version}")
        while True:
            print()
            print("#############################################################################")
            print("# 1.添加学生   2.修改学生   3.删除学生   4.查询指定学生   5.查询所有学生   6.退出系统  #")
            print("#############################################################################")
            choice = input("请选择要执行的操作，输入 1-6：")
            match choice:
                case "1":  # 添加学生
                    self.add_student()
                case "2":
                    self.update_student()
                case "3":
                    self.delete_student()
                case "4":
                    self.query_student()
                case "5":
                    self.list_student()
                case "6":
                    print("bye!")
                    return
                case _:
                    print("输入错误，请选择1-6菜单之间的功能")


if __name__ == '__main__':
    # 测试
    manager = EduManagement()
    manager.run()

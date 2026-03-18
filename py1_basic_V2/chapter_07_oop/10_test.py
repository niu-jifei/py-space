"""
学生成绩管理小案例
"""

from datetime import datetime


# 定义Person类
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Student(Person):
    count = 0

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        Student.count += 1
        # 给每个学生添加stu_id属性，格式为：年份-序号，序号靠计数器增长。
        self.id = f"{datetime.now().year}-{Student.count:03d}"
        # 给学生添加成绩，格式为： {'数学':90, '语文':80, '英语':70}
        self.scores = {}

    def add_score(self, course, score):
        self.scores[course] = score
        print(f"{self.name} 成功添加了课程{course}的分数{score}")

    def calc_avg(self):
        if self.scores:
            return sum(self.scores.values()) / len(self.scores)
        return 0

    # 魔法方法
    def __str__(self):
        return f"{self.name}({self.age}-{self.gender}),学号：{self.id}，成绩：{self.scores}，平均分:{self.calc_avg():.1f}"


class Manager:
    def __init__(self):
        self.stu_list = []

    # 添加学生
    def add_student(self):
        name = input("请输入学生姓名：")
        age = int(input("请输入学生年龄："))
        gender = input("请输入学生性别：")
        stu = Student(name, age, gender)
        self.stu_list.append(stu)
        print(f"成功添加学生,学号是{stu.id}")

    # 删除学生
    def del_student(self):
        id = input("请输入要删除学生的学号：")
        target = None
        for stu in self.stu_list:
            if stu.id == id:
                target = stu
                break

        # 如果找到了，就删除
        if target:
            self.stu_list.remove(target)
            print(f"成功删除学生{target.name}")
        else:
            print("学号有误")

    # 显示所有学生
    def show_all(self):
        if self.stu_list:
            for stu in self.stu_list:
                print(stu)
        else:
            print("暂无学生")

    # 给学生设置成绩
    def set_score(self):
        id = input("请输入学生的学号：")
        target = None
        for stu in self.stu_list:
            if stu.id == id:
                target = stu
                break
        if not target:
            print("学号有误")
            return

        # 如果找到了，就设置成绩
        # 输入成绩字符串，格式为：学科-分数，学科-分数
        score_str = input("清输入成绩（学科-分数，学科-分数）")
        # 将输入的多个成绩，按照逗号拆分，形成成绩列表
        score_list = score_str.replace("，", ",").split(",")
        # 循环成绩列表，依次添加成绩
        for score_item in score_list:
            # 将一个成绩字符串，按照减号拆分，形成成绩列表
            score_item_list = score_item.split("-")
            # 获取学科
            course = score_item_list[0].strip()
            # 获取分数
            score = int(score_item_list[1])
            # 调用add_score方法，添加成绩
            target.add_score(course, score)

        print(f"成功为学生{target.name}添加了{len(score_list)}门课程的成绩")

    def run(self):
        while True:
            print("************学生管理************")
            print("1. 添加学生")
            print("2. 删除学生")
            print("3. 查看所有学生")
            print("4. 录入成绩")
            print("5. 退出")

            chocie = input("请输入操作编号：")
            if chocie == "1":
                self.add_student()
            elif chocie == "2":
                self.del_student()
            elif chocie == "3":
                self.show_all()
            elif chocie == "4":
                self.set_score()
            elif chocie == "5":
                print("再见！")
                break
            else:
                print("输入有误！")


m1 = Manager()
m1.run()

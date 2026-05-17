"""
题目: 请设计一个学生管理系统, 包含一下内容:

1. 学生类(Student):
   - 包括属性: 学生姓名(name)、学生年龄(age)、学生成绩(score)
   - 包括功能:
     - 获取学生信息(get_info): 返回该学生的姓名、年龄和成绩。
"""

class Student:
  def __init__(self, name, age, score):
    self.name = name
    self.age = age 
    self.score = score 

  def getinfo(self):
    print(f'学生姓名:{self.name}, 学生年龄:{self.age}, 学生分数:{self.score}')



"""
2. 班级类(ClassRoom):
   - 包括属性: 班级名称(name)、班级学生列表(students)、所有班级列表(classes)
   - 包括功能: 
     - 添加学生(add_student): 将学生对象添加到指定班级的学生列表中, 如果该学生已经在指定班级中则无需重复添加, 如果该学生在其它班则调班。
     - 移除学生(remove_student): 将学生对象从指定班级的学生列表中移除, 如果该学生不在指定班级则无需移除。
     - 获取指定班级的学生信息(get_students_info): 输出指定班级的所有学生信息, 如果没有指定班级, 则默认输出所有班级的所有学生信息。
要求: 
1. 实现上述内容。
2. 编写相关测试代码。
"""

class ClassRoom:
    # 类属性: 所有班级列表
    classes = []
    
    def __init__(self, name):
        self.name = name
        self.students = []  # 班级学生列表
        # 将当前班级添加到所有班级列表中
        ClassRoom.classes.append(self)
    
    @classmethod
    def find_class(cls, class_name):
        """根据班级名称查找班级对象"""
        for classroom in cls.classes:
            if classroom.name == class_name:
                return classroom
        return None
    
    @classmethod
    def find_student_class(cls, student):
        """查找学生所在的班级"""
        for classroom in cls.classes:
            if student in classroom.students:
                return classroom
        return None
    
    def add_student(self, student):
        """
        添加学生到指定班级
        如果该学生已经在指定班级中则无需重复添加
        如果该学生在其它班则调班
        """
        # 检查学生是否已经在这个班级
        if student in self.students:
            print(f"学生 {student.name} 已经在 {self.name} 班级中, 无需重复添加")
            return
        
        # 检查学生是否在其他班级
        existing_class = ClassRoom.find_student_class(student)
        if existing_class:
            # 从原班级移除
            existing_class.remove_student(student)
            print(f"学生 {student.name} 从 {existing_class.name} 班级调班到 {self.name} 班级")
        
        # 添加到当前班级
        self.students.append(student)
        print(f"学生 {student.name} 已成功添加到 {self.name} 班级")
    
    def remove_student(self, student):
        """将学生对象从指定班级的学生列表中移除"""
        if student in self.students:
            self.students.remove(student)
            print(f"学生 {student.name} 已从 {self.name} 班级移除")
        else:
            print(f"学生 {student.name} 不在 {self.name} 班级中, 无需移除")
    
    @classmethod
    def get_students_info(cls, class_name=None):
        """
        获取指定班级的所有学生信息
        如果没有指定班级, 则默认输出所有班级的所有学生信息
        """
        if class_name:
            # 获取指定班级的信息
            classroom = cls.find_class(class_name)
            if classroom:
                print(f"\n=== {classroom.name} 班级的学生信息 ===")
                if not classroom.students:
                    print("该班级暂无学生")
                else:
                    for i, student in enumerate(classroom.students, 1):
                        print(f"{i}. {student.get_info()}")
            else:
                print(f"班级 {class_name} 不存在")
        else:
            # 输出所有班级的所有学生信息
            if not cls.classes:
                print("暂无任何班级")
                return
            
            print("\n=== 所有班级的学生信息 ===")
            for classroom in cls.classes:
                print(f"\n【{classroom.name} 班级】")
                if not classroom.students:
                    print("  暂无学生")
                else:
                    for i, student in enumerate(classroom.students, 1):
                        print(f"  {i}. {student.get_info()}")


# ==================== 测试代码 ====================

def test_student_management_system():
    """测试学生管理系统"""
    print("=" * 50)
    print("学生管理系统测试")
    print("=" * 50)
    
    # 1. 测试学生类的创建
    print("\n1. 创建学生对象:")
    student1 = Student("张三", 18, 95)
    student2 = Student("李四", 19, 87)
    student3 = Student("王五", 18, 92)
    student4 = Student("赵六", 20, 88)
    student5 = Student("小明", 19, 78)
    
    print(f"  {student1.get_info()}")
    print(f"  {student2.get_info()}")
    print(f"  {student3.get_info()}")
    print(f"  {student4.get_info()}")
    print(f"  {student5.get_info()}")
    
    # 2. 测试班级类的创建
    print("\n2. 创建班级对象:")
    class1 = ClassRoom("一年级一班")
    class2 = ClassRoom("一年级二班")
    class3 = ClassRoom("一年级三班")
    print(f"  已创建班级: {class1.name}, {class2.name}, {class3.name}")
    
    # 3. 测试添加学生
    print("\n3. 测试添加学生功能:")
    print("\n--- 向一年级一班添加学生 ---")
    class1.add_student(student1)
    class1.add_student(student2)
    class1.add_student(student3)
    
    print("\n--- 向一年级二班添加学生 ---")
    class2.add_student(student4)
    class2.add_student(student5)
    
    # 4. 测试重复添加学生
    print("\n4. 测试重复添加学生:")
    class1.add_student(student1)  # 应该提示已存在
    
    # 5. 测试调班功能
    print("\n5. 测试调班功能:")
    class2.add_student(student2)  # student2原在class1, 应该调班
    
    # 6. 测试获取学生信息
    print("\n6. 测试获取学生信息功能:")
    ClassRoom.get_students_info()  # 输出所有班级信息
    ClassRoom.get_students_info("一年级一班")  # 输出指定班级信息
    ClassRoom.get_students_info("一年级二班")
    
    # 7. 测试移除学生
    print("\n7. 测试移除学生功能:")
    print("\n--- 从一年级一班移除李四 ---")
    class1.remove_student(student2)  # student2已经在二班, 不应该被移除
    print("\n--- 从一年级二班移除李四 ---")
    class2.remove_student(student2)  # 应该成功移除
    
    # 8. 再次查看班级信息
    print("\n8. 移除后查看班级信息:")
    ClassRoom.get_students_info()
    
    # 9. 测试边界情况
    print("\n9. 测试边界情况:")
    # 移除不存在的学生
    class1.remove_student(student5)  # student5在三班
    # 获取不存在的班级信息
    ClassRoom.get_students_info("不存在的班级")
    
    # 10. 测试向空班级添加学生后查看
    print("\n10. 测试一年级三班:")
    class3.add_student(student5)
    ClassRoom.get_students_info("一年级三班")
    
    print("\n" + "=" * 50)
    print("测试完成!")
    print("=" * 50)


# 运行测试
if __name__ == "__main__":
    test_student_management_system()








def print_info():
    print("1.添加学生信息")
    print("2.删除学生信息 ")
    print("3.修改学生信息")
    print("4.查询单个学生信息")
    print("5.查询所有学生信息")
    print("6.退出系统")

user_info =[   #列表嵌套字典
     {'id':'hm01','name':'李白','phone':'123'},
     {'id':'hm02','name':'李白','phone':'123'},
     {'id':'hm03','name':'李白','phone':'123'}
]
def add_stu():
    new_id=input("请录入要添加的学生的学号：")
    for stu in user_info:
        if new_id==stu['id']:
            print(f'学号{new_id}已存在,请重新录入')
            return

    new_name=input("请输入要添加的学生姓名：")
    new_phone_num=input("请输入要添加的学生的电话号码：")
    new_info=[{'id':new_id,'name':new_name,'phone':new_phone_num}]
    user_info.append(new_info)
    print(f'学生{new_name}已经录入')
def del_stu_by_id():
    del_id=input('请录入要删除的学号：')
    for stu in user_info:
        if stu['id']==del_id:
            user_info.remove(stu)
            print(f'学号为{del_id}的学生信息已删除')
            break
    else:
        print("该学生学号不存在，请重新输入")
        return


def del_stu_by_name():
    flag=False
    del_name=input("请输入你要删除的学生姓名：")
    for i in range(len(user_info)):
        stu=user_info[i]
        if stu['name']==del_name:
           user_info.remove(stu)
           i-=1
           flag=True

    if flag==False:
        print(f"该学生{del_name}不存在，请重新输入")
    else:
        print(f"姓名为：{del_name}的学生信息已经被删除")

def update_stu():
    update_id=input("请输入要修改的学生的id:")
    for stu in user_info:
        if stu['id']==update_id:
            update_name=input("请输入要修改的学生的名字：")
            update_phone_num=input("请输入要修改的学生的电话：")
            stu["name"]=update_name
            stu["phone"]=update_phone_num
            print(f'学号{update_id}学生信息修改成功')
            break
    else:
        print(f"学号{update_id}学号不存在，请重新输入")
        return

def search_stu_by_id():
    search_id=input("请输入要查询的学生id:")
    for stu in user_info:
        if stu['id']==search_id:
            print(f'id:{stu["id"]},name:{stu["name"]},phone:{stu["phone"]}')
            break
    else:
        print(f"学生{search_id}不存在，请重新输入")
        return

def search_stu_by_name():
    flag=False
    search_name = input("请输入你要查询的学生姓名：")
    for i in range(len(user_info)):
        stu = user_info[i]
        if stu['name']==search_name:
            print(f'id:{stu["id"]},name:{stu["name"]},phone:{stu["phone"]}')
            flag=True

    if flag==False:
        print(f"学生{search_name}不存在，请重新输入")
        return

def search_all_stu():
    for stu in user_info:
        print(f'id:{stu["id"]},name:{stu["name"]},phone:{stu["phone"]}')



def student_manager():
    while True:
        print_info()
        input_num=input("请输入您要操作的编号：")
        if input_num == '1':
            add_stu()
        elif input_num == '2':
            del_stu_by_id()
        elif input_num == '3':
            update_stu()
        elif input_num == '4':
            search_stu_by_id()
        elif input_num == '5':
            search_all_stu()
        elif input_num == '6':
            print("退出系统,期待下次再见")
            break
        else:
            print("录入有误，重新输入")
        print()


if __name__ == '__main__':
    student_manager()
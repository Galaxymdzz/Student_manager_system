import os
import json
def load_data():
    global user_info
    if not os.path.exists("./student_info.txt"):
        with open("./student_info.txt","w",encoding="utf-8") as f:
            json.dump([],f,ensure_ascii=False)
        print("未找到studen_info.txt,已为您创建")
    else:
        try:
            with open("./student_info.txt", "r", encoding="utf-8") as f:
                user_info=json.load(f)
        except json.JSONDecodeError:
            user_info = []


def save_data():
    with open("./student_info.txt","w",encoding="utf-8") as f:
        json.dump(user_info,f,ensure_ascii=False,indent=2)

def SM_info():
    print("1.添加学生信息")
    print("2.删除学生信息 ")
    print("3.修改学生信息")
    print("4.查询单个学生信息")
    print("5.查询所有学生信息")
    print("6.退出系统")




user_info =[

]

def add_stu():
    add_stu_id=input("请输入您要添加的学生id:")
    for stu in user_info:
        if stu['id']==add_stu_id:
            print(f"学生系统中已经录入{add_stu_id}的信息，请重新输入")
            break
    else:
        add_stu_name=input("请输入您要录入的学生的姓名：")
        add_stu_tel =input("请输入您要录入的学生的电话：")
        user_info.append({"id":add_stu_id,"name":add_stu_name,"tel":add_stu_tel})

def del_stu_by_id():
    del_stu_id=input("请输入您要删除的学生id:")
    for stu in user_info:
        if stu['id']==del_stu_id:
            user_info.remove(stu)
            break
    else:
        print(f"该学生系统中没有id为:{del_stu_id}的学生，请重新输入")
        return

def del_stu_by_name():
    flag=False
    del_stu_name = input("请输入您要删除的学生姓名:")

    i=0
    while i <len(user_info):
        stu=user_info[i]
        if stu['name']==del_stu_name:
            user_info.remove(stu)
            i-=1
            flag=True
        i+=1

    if flag:
        print(f"学生{del_stu_name}信息已经删除")
    else:
        print(f"该学生系统中没有name为:{del_stu_name}的学生，请重新输入")
        return

def update_stu_info():
    update_stu_id = input("请输入您要修改的学生id:")
    for stu in user_info:
        if stu['id']==update_stu_id:
            update_stu_name=input("请输入您要修改的学生名字：")
            update_stu_tel=input("请输入你要修改的学生电话：")
            stu['name']=update_stu_name
            stu['tel']=update_stu_tel
            break
    else:
        print(f"该学生系统中没有id为:{update_stu_id}的学生，请重新输入")
        return

"""def update_stu_info_by_name():
    flag=False
    update_stu_name = input("请输入您要修改的学生name:")
    for stu in user_info:
        if stu['name'] ==update_stu_name:
            
"""

def search_single_by_id():
    search_stu_id = input("请输入您要查询的学生id:")
    for stu in user_info:
        if stu['id']==search_stu_id:
            print(f"id:{stu['id']},name:{stu['name']},tel:{stu['tel']}")
            break
    else:
        print(f"该学生系统中没有id为:{search_stu_id}的学生，请重新输入")
        return

def search_single_by_name():
    flag=False
    search_stu_name = input("请输入您要查询的学生name:")

    for stu in user_info:
        if stu['name']==search_stu_name:
            print(f"id:{stu['id']},name:{stu['name']},tel:{stu['tel']}")
            flag=True

    if flag==False:
        print(f"该学生管理系统中没有学生姓名为{search_stu_name}的信息")
        return

def search_all_stu():
    if len(user_info)==0:
        print("暂无学生信息，请添加后重新查询")
    else:
        for stu in user_info:
            print(f"id:{stu['id']},name:{stu['name']},tel:{stu['tel']}")





def stu_manager():
    load_data()

    while True:
        SM_info()
        sel_num=input("请输入您要操作的编号：")
        if sel_num=='1':
            add_stu()
            save_data()
        elif sel_num=='2':
            #del_stu_by_id()
            del_stu_by_name()
            save_data()
        elif sel_num=='3':
            update_stu_info()
            save_data()
        elif sel_num=='4':
            #search_single_by_id()
            search_single_by_name()
        elif sel_num=='5':
            search_all_stu()
        elif sel_num=='6':
            print("退出系统，欢迎下次再见")
            save_data()
            break
        else:
            print("输入错误，请重新输入")

        print()

if __name__ == '__main__':
    #启动学生管理系统
    stu_manager()

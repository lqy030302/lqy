#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�2021/12/02
"""
import random
# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����
# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��
def name_to_number(name):
    if name=="ʯͷ":
        return 0
    elif name=="ʷ����":
        return 1
    elif name=="��":
        return 2
    elif name=="����":
        return 3
    elif name=="����":
        return 4
    else:
        return 5
    print("Error: No Correct NameError: No Correct Name")
def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��
    if number==0:
        return "ʯͷ"
    if number==1:
        return "ʷ����"
    if number==2:
        return "��"
    if number==3:
        return "����"
    if number==4:
        return "����"
def rpsls(player_choice):


    print("----------------")
    print("player chooses",(player_choice))
    x=name_to_number(choice_name)
    comp_numb=random.randrange(0,5)
    y=number_to_name(comp_numb)
    print("���Ե�ѡ����",y)
    if x==5:
     print("error: No Correct Name")
    elif comp_numb==x:
        print("��͵���һ��")
    elif comp_numb==0:#���1
        if x == 5:
            print("error: No Correct Name")
        elif x==3 or x==4:
            print("����Ӯ��")
        else:
            print("��Ӯ��")
    elif comp_numb==1:#���2
       if x == 5:
            print("error: No Correct Name")
       elif x==4 or x==0:
           print("����Ӯ��")
       else:
           print("��Ӯ��")
    elif comp_numb==2:#���3
        if x==5:
          print("error: No Correct Name")
        elif x==0 or x==1:
            print("����Ӯ��")
        else:
            print("��Ӯ��")
    elif comp_numb==3:#���4
        if x == 5:
            print("error: No Correct Name")
        elif x==1 or x==2:
            print("����Ӯ��")
        else:
            print("��Ӯ��")
    elif comp_numb==4:#���5
        if x == 5:
            print("error: No Correct Name")
        elif x==2 or x==3:
            print("����Ӯ��")
        else:
            print("��Ӯ��")

    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    """


    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�



# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)
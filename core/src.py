# - 从settings.py中获取所需路径
# - 从common.py中获取公用方法
from conf import settings
from lib import common
import random


# - 猜大小：用户选择大或小，然后开奖，中奖与否都记录竞猜记录，中奖则记录中奖记录
def guess_big_or_small():
    winner = ""
    choice = input("请输入大或小：").strip()

    if not choice or choice != "大" or choice != "小":
        print("输入有误")
        return

    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    num3 = random.randint(1, 6)
    sum_num = sum([num1, num2, num3])

    if sum_num == 3 or sum_num == 18:
        winner = "庄家"
    elif (choice == "小" and 3 < sum_num < 11) or (choice == "大" and 10 < sum_num < 18):
        winner = "用户"

    if winner or winner == "庄家":
        common.save_record("guess", "点数分别为 %s %s %s ，总计点数：%s  %s 赢" % (num1, num2, num3, sum_num, winner))
        print("点数分别为 %s %s %s ，总计点数：%s  %s 赢" % (num1, num2, num3, sum_num, winner))
        common.save_win(winner, "猜大小中奖")
    else:
        common.save_record("guess", "点数分别为 %s %s %s ，总计点数：%s  输" % (num1, num2, num3, sum_num))
        print("点数分别为 %s %s %s ，总计点数：%s  输" % (num1, num2, num3, sum_num))


# - 匹配三：三个数字匹配，不要求顺序匹配，全对一等奖，对二二等奖，对一三等奖，记录规则同时
def tiger_machine_three():
    pass


# - 匹配五：三个数字匹配，设置五个奖项，规则同上
def tiger_machine_five():
    pass


func_map = {
    "1": guess_big_or_small,
    "2": tiger_machine_three,
    "3": tiger_machine_five,
}


# - 提示用户选择玩法：0退出 1猜大小 2匹配三 3匹配五 其他输入错误，重输
def run():
    while 1:
        choice = input("""
        0:退出
        1:猜大小
        2:匹配三
        3:匹配五
        
选项：""").strip()
        if choice == "0":
            print("退出")
            break
        if choice not in func_map:
            print("输入错误，请重输")
            continue
        func_map[choice]()

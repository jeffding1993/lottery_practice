# - 从settings.py中获取所需路径
# - 从common.py中获取公用方法
from conf import settings
from lib import common
import random


# - 猜大小：用户选择大或小，然后开奖，中奖与否都记录竞猜记录，中奖则记录中奖记录
def guess_big_or_small():
    while True:
        winner = ""
        choice = input("请输入大或小(输入q退出)：").strip()

        if choice == "q":
            print("退出")
            break

        flag, msg = common.check_input(choice, 1)
        if not flag:
            print(msg)
            break

        num_list = [random.randint(1, 6) for i in range(3)]
        sum_num = sum(num_list)

        if sum_num == 3 or sum_num == 18:
            winner = "庄家"
        elif (choice == "小" and 3 < sum_num < 11) or (choice == "大" and 10 < sum_num < 18):
            winner = "用户"

        if winner or winner == "庄家":
            common.save_record("guess", "点数分别为 %s %s %s ，总计点数：%s  %s 赢" % (num_list[0], num_list[1], \
                                                                           num_list[2], sum_num, winner))
            print("点数分别为 %s %s %s ，总计点数：%s  %s 赢" % (num_list[0], num_list[1], num_list[2], sum_num, winner))
            common.save_win(winner, "猜大小中奖")
        else:
            common.save_record("guess", "点数分别为 %s %s %s ，总计点数：%s  输" % (num_list[0], num_list[1], \
                                                                        num_list[2], sum_num))
            print("点数分别为 %s %s %s ，总计点数：%s  输" % (num_list[0], num_list[1], num_list[2], sum_num))


# - 匹配三：三个数字匹配，不要求顺序匹配，全对一等奖，对二二等奖，对一三等奖，记录规则同时
def tiger_machine_three():
    while True:
        winner = ""
        choice = input("请输入1-8的三个数字(输入q退出)：").strip()

        if choice == "q":
            print("退出")
            break

        # 转换为列表
        fan_wei = list(range(1, 9))
        choice_list = [int(i) if int(i) in fan_wei else 0 for i in choice]
        flag, msg = common.check_input(choice_list, 3)  # 检查输入

        if not flag:
            print(msg)
            break

        print("输入：")
        print(choice_list)

        # 几等奖
        result = 0
        # 假设8个数
        num_list = [random.randint(1, 8) for i in range(3)]

        num_dic = {}
        for i in num_list:
            if i not in num_dic:
                num_dic[i] = 1
            else:
                num_dic[i] += 1

        for i in choice_list:
            if i in num_dic and num_dic[i] > 0:  # 对应中奖的数量
                result += 1
                num_dic[i] -= 1

        print("结果：")
        print(num_list)

        if result:  # 中奖的话
            winner = "用户"
            reward = ""
            if result == 3:
                reward = "一"
            elif result == 2:
                reward = "二"
            elif result == 1:
                reward = "三"
            print("%s, 中 %s 等奖。" % (winner, reward))
            common.save_record("guess", "%s, 中 %s 等奖。" % (winner, reward))
            common.save_win(winner, "%s, 中 %s 等奖。" % (winner, reward))
        else:
            winner = "用户"
            print("%s,未中奖" % winner)
            common.save_record("guess", "%s,未中奖" % winner)


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

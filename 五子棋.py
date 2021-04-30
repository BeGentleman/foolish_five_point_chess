# 创建棋盘
# 用类：以方便创建子类进行改写
# 用字典：key为坐标，value为棋子
class QiPan(object):
    # 棋盘属性
    def __init__(self):
        self.qipan = []
        global input_weidu
        # self.weidu = input_weidu

    # 生成任意大小棋盘
    def generate_qipan(self):
        self.qipan = []
        for i in range(1, input_weidu+1):
            for j in range(1, input_weidu+1):
                self.qipan.append({str(i)+str(j): '+'})
        return self.qipan

    # 显示棋盘
    def print_qipan(self):
        self.qipan = self.generate_qipan()
        #qipan此时不是空的了
        # 将列表中每一个字典中的value遍历出来，并以指定的行列数展示
        hang = []
        for element in self.qipan:
            for value in element.values():
                hang.append(value)

        for i in range(0, len(hang), input_weidu):
            print(hang[i: i+input_weidu])


# 输入坐标
def luozi():
    white_heng = input("请输入白棋横坐标")
    white_zong = input("请输入白棋纵坐标")
    white_finally = white_heng + white_zong

    black_heng = input("请输入黑棋横坐标")
    black_zong = input("请输入黑棋纵坐标")
    black_finally = black_heng + black_zong

    return white_finally, black_finally


# 继承棋盘
class New_QiPan(QiPan):
    # 创建棋盘
    def __init__(self):
        self.new_qipan = self.generate_qipan()
        # global input_weidu
        # self.weidu = input_weidu

    # TODO:保留上一次棋盘用闭包
    # 更新棋盘
    def update_old_qipan(self):
        # 解包
        a, b = luozi()
        print("白棋在", a, "黑棋在", b)

        # 一旦落子点在棋盘内，找到对应坐标组成的key，将value的白棋变成🏳，黑棋变成🏴
        # 首先遍历棋盘，然后将luozi()中返回值找到
        for element in self.new_qipan:
            for jian in element.keys():
                if a == jian:
                    element[a] = '🏳'
                    break
                elif b == jian:
                    element[b] = '🏴'
                    break
        return self.new_qipan

    def print_qipan(self):
        self.qipan = self.new_qipan
        #qipan此时不是空的了
        # 将列表中每一个字典中的value遍历出来，并以指定的行列数展示
        hang = []
        for element in self.qipan:
            for value in element.values():
                hang.append(value)

        for i in range(0, len(hang), input_weidu):
            print(hang[i: i+input_weidu])


# 主函数
if __name__ == "__main__":
    input_weidu = int(input("请输入棋盘的维度"))

    qipan_1 = QiPan()
    qipan_1.print_qipan()

    count = 0
    while count < 11:
        qipan_22222 = New_QiPan()
        qipan_22222.update_old_qipan()
        qipan_22222.print_qipan()
        count += 1

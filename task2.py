# -*- coding: utf-8 -*-

"""
@author: hsowan <hsowan.me@gmail.com>
@date: 2019/10/17

"""
import random
import sys
import time

"""
    Fight Landlord Version 0.0.1
    
    Support: 一张/ 一对/ 三张/ 四张, 不能带, 没有炸弹, 没有顺子, 没有飞机, Just A Simple Game! Try it !!!
    
    Todo:
        - 炸弹
        - 三张可以带
        - 顺子
        - ✈️
        - More...
    
    - 共54张牌
    - 花色
    - 黑桃`'\u2660'` - 梅花`'\u2663'` - 方块`'\u2665'` - 红桃`'\u2666'`
    -牌
    - 大小王
    - 数字 `A2~10JQK`
    - 要求
    - 1.生成大小王+各种花色分别13张牌,装在列表中
    - 2.将顺序打乱,也就是洗牌
    - 3.发给3个人,没人17张,底牌留三张
    - 4.将三个人分别是什么牌装在字典中
    - 5.抢地主,分别打印三个人的名字,让其确认是否当地主
    - 6.如果有人地主,则将三张牌追加到他的牌中
    - 7.如果没有人地址,则默认将牌发给第一个人
    
"""


class Base(object):
    """基础类"""

    def __init__(self):
        """初始化方法"""

        # 定义列表，用来保存当前角色手中的牌。初始牌为空。
        self.cards = []

    def show_cards(self, show_cards=None):
        """
        1. 向控制台打印手中所有的牌。
        2. 对手中的牌进行整理

        :param show_cards: 需要打印的牌
        """

        if show_cards is None:
            show_cards = self.cards
            # 牌数
            card_count = len(show_cards)
            # 对牌进行整理
            for k in range(card_count):
                for j in range(k + 1, card_count):
                    if self.cards[k].card_value < self.cards[j].card_value:
                        temp = self.cards[k]
                        self.cards[k] = self.cards[j]
                        self.cards[j] = temp
        else:
            card_count = len(show_cards)
        for index, card in enumerate(show_cards):
            end = '\n' if index + 1 == card_count else ' '
            if card.card_text != u'大王' and card.card_text != u'小王':
                print(card.card_type, card.card_text, sep='', end=end)
            else:
                print(card.card_text, end=end)


class Card(object):
    """定义扑克牌类。每个对象代表一张扑克牌。

    """

    def __init__(self, card_type=None, card_text=None, card_value=None):
        """初始化方法。

        Parameters
        -----
        card_type : str
            牌的类型。（红桃，黑桃，梅花，方片）
        card_text : str
            牌面显示的文本。（A，K，Q，J）
        card_value : int
            牌面大小。（如A > K）

        """
        self.card_type = card_type
        self.card_text = card_text
        self.card_value = card_value


class Role(Base):
    """定义角色类，用来表示电脑（庄家）与我们用户（玩家）。"""

    def __init__(self, name):
        """初始化方法"""
        super().__init__()
        self.name = name

    def push_cards(self, cards_index):
        """玩家出牌, 根据牌的序号选择出牌

        :param cards_index: 牌的序号, 从1开始
        :return: list
        """
        # 需要打印的牌
        ret_cards = []
        # 将下标减一
        cards_index = list(map(lambda x: x - 1, cards_index))
        for index, card_index in enumerate(cards_index):
            card_index -= index
            ret_cards.append(self.cards[card_index])
            self.cards.pop(card_index)

        return ret_cards


class CardManager(Base):
    """扑克牌管理类。管理一整副扑克牌，并且能够进行发牌。"""

    def __init__(self, file):
        """初始化方法"""

        # 定义列表，用来保存一整副扑克牌（54张）
        super().__init__()
        self.file = file
        self.last_push_cards = None
        # 定义所有牌的类型。
        all_card_type = u"♥♠♣♦"
        # 定义所有牌面显示的文本
        all_card_text = ["2", "A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3"]
        # 定义牌面文本对应的大小
        all_card_value = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3]
        # 对牌面类型与牌面文本进行嵌套循环。
        for card_type in all_card_type:
            for index, card_text in enumerate(all_card_text):
                # 创建Card类型的对象。（一张扑克牌）
                card = Card(card_type, card_text, all_card_value[index])
                # 将创建好的card对象加入到整副扑克牌当中。
                self.cards.append(card)
        # 添加大小王
        self.cards.append(Card(card_text=u'大王', card_value=17))
        self.cards.append(Card(card_text=u'小王', card_value=16))
        # 洗牌操作
        random.shuffle(self.cards)

    def send_card(self, role, num=1):
        """给电脑或者玩家发牌。

        Parameters
        -----
        role: Role
            电脑或玩家对象。
        num: int
            发牌的张数。默认为1。
        """

        count = 0
        while count < num:
            card = self.cards.pop()
            role.cards.append(card)
            count += 1

    def save_push_cards(self, push_cards):
        """保存玩家的出牌到文本

        :param push_cards: str, 玩家的出牌
        :param file: 保存的文件
        :return:
        """
        push_cards_str = ''
        card_count = len(push_cards)
        for index, card in enumerate(push_cards):
            end = '\n' if index + 1 == card_count else ' '
            if card.card_text != u'大王' and card.card_text != u'小王':
                push_cards_str += card.card_type + card.card_text + end
            else:
                push_cards_str += card.card_text + end

        with open(self.file, 'a',encoding="utf-8") as f:
            f.write(push_cards_str)

    def reload_push_cards(self):
        """重载玩家的出牌

        :return:
        """
        with open(self.file, 'r') as f:
            print(f.read())

    def remember_last_push_cards(self, push_cards):
        """记录上一个玩家的出牌

        :param push_cards: Card list
        :return:
        """
        self.last_push_cards = push_cards

    def compare(self, push_cards):
        """前后两次出牌的比较

        :param push_cards: Card list
        :return: bool
        """
        if len(push_cards) != len(self.last_push_cards):
            return False
        else:
            return push_cards[0].card_value > self.last_push_cards[0].card_value

    @staticmethod
    def is_game_over(current_role):
        """判断游戏是否结束

        :param current_role: Role 出牌的玩家
        :return:
        """
        if len(current_role.cards) == 0:
            return True
        return False

    @staticmethod
    def is_push_cards_valid(push_cards):
        """判断出牌的合法性, 一张/ 一对/ 三张/ 四张

        :param push_cards: Card list
        :return:
        """

        card_values = []
        for push_card in push_cards:
            card_values.append(push_card.card_value)
        if len(push_cards) == card_values.count(card_values[0]):
            return True
        else:
            return False


if __name__ == '__main__':
    # 创建扑克牌管理器类
    save_file = str(int(time.time())) + '.txt'
    card_manager = CardManager(save_file)

    print('**************** Fight Landlord Version 0.0.1 ****************')
    print(u'请自觉遵守游戏规则哦')
    print(u'请自觉遵守游戏规则哦')
    print(u'请自觉遵守游戏规则哦')
    print(u'重要的事情都是说三遍的！！！')
    print(u'我们马上就要开始了')
    for i in range(3, 0, -1):
        time.sleep(1)
        print(i)

    roles = []
    # 创建三个玩家
    # 玩家悟空
    wukong = Role(u'悟空')
    # 添加玩家到玩家列表
    roles.append(wukong)
    print(u'悟空准备好了...')
    time.sleep(1)

    # 玩家沙僧
    shaseng = Role(u'沙僧')
    # 添加玩家到玩家列表
    roles.append(shaseng)
    print(u'沙僧准备好了...')
    time.sleep(1)

    # 玩家八戒
    bajie = Role(u'八戒')
    # 添加玩家到玩家列表
    roles.append(bajie)
    print(u'八戒准备好了...')
    time.sleep(1)

    print(u'都准备好了呀, 那我们开始吧👀')
    time.sleep(1)

    # 打乱玩家顺序
    random.shuffle(roles)

    print(u'************** 开始发牌 **************')
    time.sleep(0.5)
    print(u'************** 正在发牌 **************')
    for i in range(17):
        for j in range(3):
            card_manager.send_card(roles[j])
            time.sleep(0.1)
    print(u'************** 发牌完成 **************')

    # 顺序看牌
    for i in range(3):
        while 1:
            is_ready = input(u'请' + roles[i].name + u'看牌, 其他玩家请回避哦, 准备好否? (y/n)')
            if is_ready == 'y':
                roles[i].show_cards()
                break
            else:
                print(u'输入有误, 请输入y/n')

        while 1:
            read_over = input(u'看完否? (y/n)')
            if read_over == 'y':
                for j in range(100):
                    print(u'不准往上看哦')
                break

    # 地主
    landlord = None
    # 是否抢地主
    for i in range(3):
        want_rob = input(u'抢地主吗, ' + roles[i].name + u'? (y/n)')
        if want_rob == 'y':
            landlord = roles[i]
            roles.pop(i)
            break

    if landlord is None:
        print(u'开始随机选择地主...')
        time.sleep(1)
        random_index = random.choice((0, 1, 2))
        landlord = roles[random_index]
        roles.pop(random_index)

    # 给所有玩家展示底牌
    print(u'************** 这是底牌 **************')
    card_manager.show_cards()
    print(u'************** 这是底牌 **************')

    # 将底牌追加到地主手中
    landlord.cards.extend(card_manager.cards)
    card_manager.cards.clear()

    # 重新调整玩家列表的位置
    temp = [landlord]
    temp.extend(roles)
    roles = temp
    del temp

    # 不要的次数
    pass_count = 0
    # 是否属于第一次出牌
    first_fight = True
    # 从地主开始出牌
    while True:
        for index, role in enumerate(roles):
            current_role_name = u'农民(' + role.name + ')' if index != 0 else u'地主(' + role.name + ')'
            if pass_count == 2:
                card_manager.last_push_cards = None
                first_fight = True
                pass_count = 0
            while True:
                is_ready = input(u'轮到' + current_role_name + u'出牌, 其他人回避了吗? (y/n)')
                if is_ready == 'y':
                    for j in range(100):
                        print(u'不准往上看哦')
                    if card_manager.last_push_cards:
                        print(u'************** 这是上一个玩家出的牌 **************')
                        card_manager.show_cards(card_manager.last_push_cards)
                        print(u'************** 这是上一个玩家出的牌 **************')

                    role.show_cards()
                    while True:
                        push_cards_index = input(u'请输入需要出的牌的序号, 以英文逗号分割, 序号从1开始: (输入n表示不要)')

                        if push_cards_index == 'n':
                            if first_fight:
                                print(u'地主第一次出牌不能不要哦, 请选择出牌')
                                continue
                            else:
                                print(u'过过过')
                                pass_count += 1
                                break
                        # 获取玩家所出牌的列表
                        push_cards_index_list = push_cards_index.replace(' ', '').split(',')
                        if len(push_cards_index_list) == 0:
                            print(u'至少出一张牌哦, 请重新出牌')
                            continue
                        # 将列表中的字符转为数字
                        try:
                            push_cards_index_list = list(map(lambda x: int(x), push_cards_index_list))
                        except ValueError:
                            print(u'非法输入, 请重新选择出牌')
                            continue
                        # 设置标志: 是否出牌合法
                        is_push_cards_valid = True
                        # 判断所出牌的合法性
                        for push_card_index in push_cards_index_list:
                            if 1 <= push_card_index <= len(role.cards):
                                # 所出牌序号重复
                                if push_cards_index_list.count(push_card_index) > 1:
                                    print(u'所出牌序号重复, 请重新出牌')
                                    is_push_cards_valid = False
                                    break
                            # 所出牌序号不存在
                            else:
                                print(u'所出牌序号不存在, 请重新出牌')
                                is_push_cards_valid = False
                                break

                        if is_push_cards_valid:
                            # 玩家出牌
                            push_cards = role.push_cards(push_cards_index_list)
                            # 再次判断出牌是否有效
                            if card_manager.is_push_cards_valid(push_cards):
                                # 不是第一次出牌的话，需要和上一次出牌进行比较
                                if card_manager.last_push_cards:
                                    if not card_manager.compare(push_cards):
                                        # 出牌无效时, 将牌还给玩家
                                        role.cards.extend(push_cards)
                                        print(u'所出牌不够大哦, 请重新出牌')
                                        continue

                                if card_manager.is_game_over(role):
                                    if index != 0:
                                        print(u'革命胜利了！！！')
                                    else:
                                        print(u'地主太厉害了。。。')
                                    print(u'************** 这是出牌记录 **************')
                                    card_manager.reload_push_cards()
                                    print(u'************** 这是出牌记录 **************')
                                    sys.exit()
                                else:
                                    print(u'您打的牌真棒👍👍👍')
                                    card_manager.remember_last_push_cards(push_cards)
                                    card_manager.save_push_cards(push_cards)
                                    break
                            else:
                                # 出牌无效时, 将牌还给玩家
                                role.cards.extend(push_cards)
                                print(u'该版本仅支持: 一张/ 一对/ 三张/ 四张, 不能带, 没有王炸, 没有顺子, 没有飞机, Simple Game It is! 请重新出牌')
                                continue
                        else:
                            continue
                    if first_fight:
                        first_fight = False
                    break



# 呵呵


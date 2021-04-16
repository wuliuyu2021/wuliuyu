#!/usr/bin/python
# -*- coding: utf-8 -*-


class Player(object):

	def __init__(self, name, score=0):
		self.name=name
		self.score=score

	def __str__(self):
		rep=self.name + ":\t" + str(self.score)
		return rep

	def ask_yes_no(question):
		response=None
		while response not in ("y", "no"):
			response=input(question).lower()
		return response

	def ask_number(question, low, high):
		response=None
		while response not in range(low, high):
			response=int(input(question))
		return response

	if __name__ == '__main__':
		print("You ran this module directly (and did not 'import' it).")
		input("\n\nPress the Enter key to exit.")

class Card(object):
	RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
	SUITS = ["c", "d", "h", "s"]

	def __init__(self, rank, suit, face_up = True):
		self.rank = rank
		self.suit = suit
		self.is_face_up = face_up

	def __str__(self):
		if self.is_face_up:
			rep = self.rank + self.suit
		else:
			rep = "XX"return rep

	def flip(self):
		self.is_face_up = not self.is_face_up

class Hand(object):     # 手牌类

    """A hand of playing cards."""
	def __init__(self):
		self.cards = []

 	def __str__(self):
 		if self.cards:
 			rep = ""
 			for card in self.cards:
 				rep += str(card) + "\t"
 			else:
 				rep = "<empty>"
 		return rep

	def clear(self):
		self.cards = []

 
 	def add(self, card):
 		self.cards.append(card)

	def give(self, card, other_hand):
		self.cards.remove(card)
		other_hand.add(card)

class Deck(Hand):    # 副牌类， 继承Hand类

    """A deck of palying cards"""
	def populate(self):   # 创建一副牌
		for suit in Card.SUITS:
			for rank in Card.RANKS:
				self.add(Card(rank, suit))
	
	def shuffle(self):
		import random
		random.shuffle(self.cards)

	def deal(self, hands, per_hand = 1):   # 发牌  per_hand(玩家应得牌数)，hands(玩家列表)
		for rounds in range(per_hand):
			for hand in hands:
				if self.cards:
					top_card = self.cards[0]
					self.give(top_card, hand)
				else:
					print("Can't continue deal. Out of cards!")

 	if __name__ == "__main__":
 		print("This is a module with classes for playing cards!")
 		input("\n\nPress the enter key to exit.")


import Games, Cards_Module

class BJ_Card(Cards_Module.Card):    # 卡牌类， 继承Card类

    """A Blackjack Card."""
	ACE_VALUE = 1          # "A"的值，默认为1
	
	@property
	
	def value(self):     # 获取牌所对应的值
		if self.is_face_up:
			v = BJ_Card.RANKS.index(self.rank) + 1
			if v > 10:
				v = 10
			else:
				v = None
		return v


class BJ_Deck(Cards_Module.Deck):   # 副牌类， 继承Deck类

    """A Blackjack Deck."""

	def populate(self):     # 重写populate方法，允许BJ_Deck对象填入BJ_Card对象

		for suit in BJ_Card.SUITS:

			for rank in BJ_Card.RANKS:

				self.cards.append(BJ_Card(rank, suit))
				
				
class BJ_Hand(Cards_Module.Hand):  # 手牌类  ， 继承Hand类

""" A Blackjack Hand."""

	def __init__(self, name):   # 重写构造器，添加一个表示拥有者的name特性

		super(BJ_Hand, self).__init__()   # super(BJ_Hand,self)用于找到BJ_Hand的父类，也可以直接调用父类名

		self.name = name

	def __str__(self):   # 重写该方法，使其可以显示这手牌的总点数

		rep = self.name + ":\t" + super(BJ_Hand,self).__str__()

		if self.total:

			rep += "(" + str(self.total) + ")"

		return rep
	
	@property

	def total(self):

# 如果当前这手牌中有一张牌的value为None,则total为None

		for card in self.cards:

			if not card.value:

			return None

# 把牌的点数加起来，A的点数记为1

			t = 0

			for card in self.cards:

				t += card.value


        # 判断当前这手牌中有没有A

			contains_ace = False

        for card in self.cards:

            if card.value == BJ_Card.ACE_VALUE:

                contains_ace = True

 

        # 如果有A且total够小，则将A记为11

        if contains_ace and t <= 11:

            # 因为已经为这张A加了1，所有这里只加10

            t += 10

 

        return t

 

    def is_busted(self):  # 判断是否爆掉

        return self.total > 21

 

 

class BJ_Player(BJ_Hand):   # 玩家类  继承BJ_Hand类

    """A Blackjack Player."""

    def is_hitting(self):   # 是否再次叫牌

        response = Games.Player.ask_yes_no("\n" + self.name +", do you want a hit?(Y/N):")

        return response == "y"

 

    def bust(self):   # 声明该玩家爆掉

        print(self.name, "busts.")

        self.lose()

 

    def lose(self):   # 声明玩家输了

        print(self.name, "loses.")

 

    def win(self):    # 声明玩家赢了

        print(self.name, "wins.")

 

    def push(self):   # 声明玩家平手

        print(self.name, "pushes.")

 

 

class BJ_Dealer(BJ_Hand):   # 庄家类   继承BJ_Hand类

    """A Blackjack Dealer."""

    def is_hitting(self):   # 总点数不足17必须叫牌

        return self.total < 17

 

    def bust(self):    # 声明庄家爆掉

        print(self.name, "busts.")

 

    def flip_first_card(self):   # 翻开庄家的第一张牌

        first_card = self.cards[0]

        first_card.flip()

 

 

class BJ_Game(object):   # 21点游戏 类，用于创建一局游戏

    """A Blackjack Game."""

    def __init__(self, names):

        self.players = []

        for name in names:   # 玩家加入游戏

            player = BJ_Player(name)

            self.players.append(player)

 

        self.dealer = BJ_Dealer("Dealer")   # 创建庄家

 

        self.deck = BJ_Deck()   # 定义一副牌

        self.deck.populate()    # 构造一副牌

        self.deck.shuffle()     # 洗牌

 

    @property

    def still_playing(self):   # 存活玩家列表

        sp = []

        for player in self.players:

            if not player.is_busted():

                sp.append(player)

        return sp

 

    def __additional_cards(self, player):   # 向玩家或庄家加发一张牌

        while not player.is_busted() and player.is_hitting():

            self.deck.deal([player])

            print(player)

            if player.is_busted():

                player.bust()

 

    def play(self):

        # 给每个人发两张牌

        self.deck.deal(self.players + [self.dealer], per_hand=2)

        self.dealer.flip_first_card()  # 隐藏庄家的第一张牌

        for player in self.players:

            print(player)

        print(self.dealer)

 

        # 给所有玩家加牌

        for player in self.players:

            self.__additional_cards(player)

 

        self.dealer.flip_first_card()  # 翻开庄家的第一张牌

        if not self.still_playing:

            # 由于所有玩家都爆掉了，因此直接亮出庄家手中的牌即可

            print(self.dealer)

        else:

            # 给庄家加牌

            print(self.dealer)

            self.__additional_cards(self.dealer)

 

            if self.dealer.is_busted():

                # 所有还在玩的玩家都获胜

                for player in self.still_playing:

                    player.win()

            else:

                # 每位还在玩的玩家分别跟庄家比点数

                for player in self.still_playing:

                    if player.total > self.dealer.total:

                        player.win()

                    elif player.total < self.dealer.total:

                        player.lose()

                    else:

                        player.push()

 

        # 清空所有人手中的牌

        for player in self.players:

            player.clear()

        self.players.clear()

 

 

def main():

    print("\t\tWelcome to Blackjack!\n")

    names = []     # 玩家列表

    number = Games.Player.ask_number("How many players? (1-7):", low = 1, high = 8)

    for i in range(number):     # 添加玩家

        name = input("Enter player name:")

        names.append(name)

    print()

 

    game = BJ_Game(names)    # 创建游戏

 

    again = None

    while again != "n":

        game.play()      # 开始游戏

        again = Games.Player.ask_yes_no("\nDO you want to play again?:(Y/N)")   # 再来一局？

 

# 程序主体

main()

input("\n\nPress the enter key to exit.")
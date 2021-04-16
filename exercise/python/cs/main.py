#!/usr/bin/env python
# -*- coding: utf-8 -*-

from grenade import Grenade
from gun import Gun
from bulletbox import Bulletbox
from gengster import Gengster
from profector import Profector

def main():

	bulletbox = Bulletbox(10)
	gun = Gun(bulletbox)
	grenade = Grenade(20)
	good1 = Profector(gun,grenade)
	good2 = Profector(gun,grenade)
	bad1 = Gengster(gun,grenade)
	bad2 = Gengster(gun,grenade)

	print("阿宝开枪打坏人1和2")
	good1.fire(bad1)
	good1.fire(bad2)

	print("阿爷开枪打坏人1和2")
	good2.fire(bad1)
	good2.fire(bad2)

	print("坏人1炸阿宝和阿爷")
	bad1.fire2(good1)
	bad1.fire2(good2)

	print("坏人2炸阿宝和阿爷")
	bad2.fire2(good1)
	bad2.fire2(good2)

	print("阿宝、阿爷补血100")
	good1.fillblood(100)
	good2.fillblood(100)
	print('Congratulations, Full Blood!!!')

if __name__ == '__main__':
	main()
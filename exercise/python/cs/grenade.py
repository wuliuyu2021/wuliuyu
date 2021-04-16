#!/usr/bin/env python
# -*- coding: utf-8 -*-

from person import Person

class Grenade(object):

	def __init__(self,grenadecount):
		self.grenadecount = grenadecount

	def damage(self):
		if self.grenadecount == 0:
			print('手雷没有了')
		else:
			self.grenadecount -= 1
			print("轰他一炮，手雷还剩%d颗" % (self.grenadecount))
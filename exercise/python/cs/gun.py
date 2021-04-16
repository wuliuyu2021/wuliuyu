#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Gun(object):

	def __init__(self,bulletbox):
		self.bulletbox = bulletbox

	def shoot(self):
		if self.bulletbox.bulletcount == 0:
			print('没子弹了')
		else:
			self.bulletbox.bulletcount -= 1
			print('开一枪，还剩%d颗子弹' % (self.bulletbox.bulletcount))
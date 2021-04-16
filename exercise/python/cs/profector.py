#!/usr/bin/env python
# -*- coding: utf-8 -*-

from person import Person

class Profector(Person):
	
	def __init__(self, gun, grenade, blood=100):
		super(Profector,self).__init__(gun, grenade, blood)
		'''self.gun = gun
		self.grenade = grenade
		self.blood = blood

	def fire(self, person):
		person.blood -= 5
		self.gun.shoot()
		print(str(person) + "血量减少5，剩余" + str(person.blood))

	def fire2(self,person):
		person.blood -= 10
		self.grenade.damage()

	def fillbullet(self):
		self.gun.bulletbox.bulletcount += 10

	def fillblood(self,num):
		self.blood += num
		if self.blood > 100:
			self.blood = 100
			print("补血后血量：" + str(self.blood))'''
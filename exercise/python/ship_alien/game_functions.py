#-*- coding:utf-8 -*-
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from bullet import Bullet

def check_events(ai_settings,screen,ship,bullets):
	# 监视键盘和鼠标事件
	for event in pygame.event.get():

		if event.type == pygame.QUIT:  # 关闭窗口退出
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)

def update_screen(ai_settings,screen,ship,bullets):
	'''更新屏幕上的图片，并切换到新屏幕'''
	screen.fill(ai_settings.bg_color)  # 设置背景颜色
	ship.blitme()  # 绘制飞船

	# 循环子弹组里面的元素，进行绘制 为空时不执行
	for bullet in bullets.sprites():
		bullet.draw_bullet()	# 绘制子弹

	# 显示最新屏幕，擦拭旧屏幕
	pygame.display.flip()
	# print('1')

def check_keydown_events(event,ai_settings,screen,ship,bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)

def check_keyup_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def update_bullets(bullets):
	'''更新子弹位置，删除子弹'''
	bullets.update()	 # 子弹组每个成员执行self.update()操作
	for bullet in bullets.sprites():
		if bullet.rect.bottom <= 0:  # 子弹出界 删除
			bullets.remove(bullet)

def update_ship(ship):
	ship.update()

def fire_bullet(ai_settings,screen,ship,bullets):
	# 创建一个子弹对象 加入到子弹组
	if len(bullets) < ai_settings.bullet_allowed:  # 子弹少于允许值时再生成
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)
#!/usr/bin/env python
#-*- coding: utf-8 -*-
#上記の文を書けば日本語で注釈が書ける
import rospy
from std_msgs.msg import Int32　　#送信方法を数字で行うという意味
#msgという枠組みで送受信を行う 文でやるなら inport String

n = 0

def cb(message): # cdという関数を作成
	//rospy.loginfo(message.data*2)
	global n
	n = message.data*2　#受け取ったcountの数字を二倍にしている

if __name__ == '__main__':  #C言語でのメイン文
	rospy.init_node('twice') :ROSのノードを初期化している
	sub = rospy.Subscriber('count_up', Int32, cb)#受け取ったcount_upを
#cbに付けている
	//rospy.spin()
	pub = rospy.Publisher('twice', Int32, queue_size=1)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown(): #ROSが終了するまで実行を繰り返す
		pub.publish(n)#nの値をCUIに記述
		rate.sleep()
	

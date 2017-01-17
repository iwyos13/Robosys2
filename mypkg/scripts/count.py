#!/usr/bin/env python
#-*- coding: utf-8 -*-
#上記の文を書けば日本語で注釈が書ける

import rospy  #Cでいうinclude 
from std_msgs.msg import Int32 #msgという枠組みで送受信 Int32は数字でやり取り

if __name__ == '__main__': #main文
	rospy.init_node('count')#ノードの初期化
	pub = rospy.Publisher('count_up', Int32, queue_size=1)
	#キューサイズは送る数字,1にカウントアップという名前を付ける
	#Int32 は送る形式, これだと数字で送る
	rate = rospy.Rate(10) #一回につき10回カウント
	n = 0
	while not rospy.is_shutdown():
		n += 1
		pub.publish(n)
		rate.sleep()


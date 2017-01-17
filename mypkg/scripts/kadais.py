#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Int32 #送信方法を数字で行うという意味
#msgという枠組みで送受信を行う 文でやるなら inport String

n = 0

def ABC(message): # cdという関数を作成
       
        global n
        n = message.data+1 #受け取ったcountの数字+1

if __name__ == '__main__': #C言語でのメイン文
        rospy.init_node('kadais')  #ROSのノードを初期化している
        sub = rospy.Subscriber('count_up', Int32, ABC)#受け取ったcount_upを
#ABCに付けている
       
        pub = rospy.Publisher('kadais', Int32, queue_size=1)
        rate = rospy.Rate(30)
        while not rospy.is_shutdown(): #ROSが終了するまで実行を繰り返す
                pub.publish(n*3)#nの値をCUIに記述
                rate.sleep()

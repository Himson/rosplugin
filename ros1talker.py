import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    pub2 = rospy.Publisher('chatter_2', String, queue_size=10)

    rospy.init_node('talker', anonymous=True, xmlrpc_port=45100, tcpros_port=45101)
    rate = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        hello_str2 = "hello world again! %s" % rospy.get_time()
        # rospy.loginfo(hello_str)
        pub.publish(hello_str)
        pub2.publish(hello_str2)

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
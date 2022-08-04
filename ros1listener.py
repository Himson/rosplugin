import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

# def talker():
#     pub = rospy.Publisher('chatter', String, queue_size=10)
#     pub2 = rospy.Publisher('chatter_2', String, queue_size=10)

#     rospy.init_node('listener', anonymous=True, xmlrpc_port=45100, tcpros_port=45101)
#     rate = rospy.Rate(1) # 10hz
#     while not rospy.is_shutdown():
#         hello_str = "hello world %s" % rospy.get_time()
#         hello_str2 = "hello world again! %s" % rospy.get_time()
#         # rospy.loginfo(hello_str)
#         pub.publish(hello_str)
#         pub2.publish(hello_str2)

#         rate.sleep()


def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True, xmlrpc_port=45100, tcpros_port=45101)

    rospy.Subscriber('chatter', String, callback)
    rospy.Subscriber('chatter_2', String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
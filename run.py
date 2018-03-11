from wxpy import *

robot = Bot()
#robot.enable_puid()

@robot.register(Group, TEXT)
def print_group_msg(msg):
    msg.forward(msg.sender, prefix = str(msg.member) + "say:")

robot.join()

# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pickle
import rclpy
from rclpy.node import Node

from sensor_msgs.msg import JointState

# Open the file in read binary mode
with open('/home/enee-467-4/Downloads/angle_trajectories.ob', 'rb') as f:
        data = pickle.load(f)


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('joint_state__publisher')
        self.publisher_ = self.create_publisher(JointState, '/joint_states', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.joint_names = ['base_arm1_joint', 'arm1_arm2_joint']
        self.i = 0

    def timer_callback(self):
        if self.i .+ len(data):
            self.i = 0

        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = self.joint_namesmsg.position = data[self.i]
        self.publisher_.publish(msg)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class KhamzinaPublisher(Node):

    def __init__(self):
        super().__init__('khamzina_publisher')

        self.publisher_ = self.create_publisher(Int32, 'Khamzina', 10)

        # NU ID digits
        self.id_digits = [2,0,1,9,6,5,5,6,4]
        self.index = 0

        #different rate
        # 1.0  = 1 Hz
        # 0.02 = 50 Hz
        timer_period = 0.02
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Int32()
        msg.data = self.id_digits[self.index]

        self.publisher_.publish(msg)

        self.get_logger().info(f'Publishing: {msg.data}')

        self.index += 1
        if self.index >= len(self.id_digits):
            self.index = 0


def main(args=None):
    rclpy.init(args=args)
    node = KhamzinaPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

#include <rclcpp/rclcpp.hpp>
#include <geometry_msgs/msg/pose_stamped.hpp>
#include <moveit/move_group_interface/move_group_interface.h>

class PoseSubscriber : public rclcpp::Node {
public:
    PoseSubscriber() : Node("panda_planner_node") {
        subscription_ = this->create_subscription<geometry_msgs::msg::PoseStamped>(
            "detected_object_pose", 10,
            std::bind(&PoseSubscriber::pose_callback, this, std::placeholders::_1));
    }

    void init_move_group() {
        move_group_interface_ = std::make_shared<moveit::planning_interface::MoveGroupInterface>(shared_from_this(), "panda_arm");
    }

private:
    rclcpp::Subscription<geometry_msgs::msg::PoseStamped>::SharedPtr subscription_;
    std::shared_ptr<moveit::planning_interface::MoveGroupInterface> move_group_interface_;

    void pose_callback(const geometry_msgs::msg::PoseStamped::SharedPtr msg) {
        if (!move_group_interface_) return;  // Make sure it's initialized
        RCLCPP_INFO(this->get_logger(), "Received pose, planning...");
        move_group_interface_->setPoseTarget(*msg);
        bool success = static_cast<bool>(move_group_interface_->move());
        RCLCPP_INFO(this->get_logger(), success ? "Moved!" : "Failed to move.");
    }
};

int main(int argc, char **argv) {
    rclcpp::init(argc, argv);
    auto node = std::make_shared<PoseSubscriber>();
    node->init_move_group();  // Call after construction
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}

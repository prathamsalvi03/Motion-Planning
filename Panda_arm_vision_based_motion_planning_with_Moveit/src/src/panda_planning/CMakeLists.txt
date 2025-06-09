cmake_minimum_required(VERSION 3.8)
project(panda_planning)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(moveit_ros_planning_interface REQUIRED)

add_executable(move_to_pose src/move_to_pose.cpp)

ament_target_dependencies(move_to_pose
  rclcpp
  geometry_msgs
  moveit_ros_planning_interface
)

install(TARGETS
  move_to_pose
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()

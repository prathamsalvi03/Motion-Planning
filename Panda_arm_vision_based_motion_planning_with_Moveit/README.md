Project: Vision-Based Object Detection and Motion Planning using MoveIt2
Overview
This project uses a vision system (OpenCV) to detect a red circle object using a USB camera and publishes its position as a geometry_msgs::msg::PoseStamped. A motion planning node (written in C++) listens to this pose and commands a robotic arm (e.g., Panda or UR5) to move to that location using MoveIt2.






[PANDA_VISION_PROJECT_MOVEIT2.webm](https://github.com/user-attachments/assets/1cda7dc0-b25b-46c4-9ec7-3d0000e6ec5f)

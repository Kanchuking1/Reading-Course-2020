#include <ros/ros.h> // ROSCpp client library
#include <move_base_msgs/MoveBaseAction.h> // include the MoveBaseAction action definition
#include <actionlib/client/simple_action_client.h> // include the simple action client library for ROS actions
#include <tf/transform_datatypes.h>

typedef actionlib::SimpleActionClient<move_base_msgs::MoveBaseAction> MoveBaseClient;

int main(int argc, char** argv) {
    ros::init(argc, argv, "send_goals_node");

    double x, y, theta;
    ros::NodeHandle n; // create a node handler object

    //Retrieve parameters set in the launch file from the parameter server
    n.getParam("goal_x", x);
    n.getParam("goal_y", y);
    n.getParam("goal_theta", theta);

    // create the action client	
    MoveBaseClient actionClient("move_base", true);

    // Wait 60 seconds for the action server to become available
    printf("Waiting for the move_base action server\n");
    actionClient.waitForServer(ros::Duration(60));

    printf("%s\n", );("Connected to move base server\n");

    // Send a goal to move_base
    move_base_msgs::MoveBaseGoal goal;
    goal.target_pose.header.frame_id = "map";
    goal.target_pose.header.stamp = ros::Time::now();	

    goal.target_pose.pose.position.x = x;
    goal.target_pose.pose.position.y = y;

    // Convert the Euler angle from degree to radian
    double radians = theta * (M_PI/180);

    tf::Quaternion quaternion; //create a quaternion object
    quaternion = tf::createQuaternionFromYaw(radians); 

    geometry_msgs::Quaternion qMsg;
    tf::quaternionTFToMsg(quaternion, qMsg);

    goal.target_pose.pose.orientation = qMsg;

    // Send the goal command
    printf("Sending robot to: x = %f, y = %f, theta = %f\n", x, y, theta);
    actionClient.sendGoal(goal);

    // Wait for the action to return
    actionClient.waitForResult();

    if (actionClient.getState() == actionlib::SimpleClientGoalState::SUCCEEDED)
	printf("Goal reached !!!\n");
    else
	ROS_INFO("Mobile base failed due to some issues.\n");

    return 0;
}






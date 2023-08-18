
# ROS2: MAX30102 heart_rate_sensor

ROS2 Foxy on Ubuntu 20.04. Publish heart rate to a ROS topic via pyserial. Running on Intel AMR Scuttle Kit


## Setting up Arduino

- Install Arduino 1.18.19 from https://www.arduino.cc/en/software
- To install the library navigate to the Sketch > Include Library > Manage Libraries…
- Filter your search by typing MAX3010x. Look for SparkFun MAX3010x Pulse and Proximity Sensor Library. Click on that entry, and then select Install.
- To access the example sketches, navigate to the File > Examples > SparkFun MAX3010x Pulse and Proximity Sensor Library, select Example5


Credit: https://lastminuteengineers.com/max30102-pulse-oximeter-heart-rate-sensor-arduino-tutorial/


## Building ROS2 package

To build this project, run:

```bash
  cd ros2_workspace/src
  git clone https://github.com/CharlesTay25/heart_rate_ROSduino.git
  cd ..
  colcon build --symlink-install --packages-select heart_rate_monitor
```
After building, source the environment
```bash
source install/setup.bash
```

## To run

To launch the basic heart rate monitoring:
```bash
ros2 launch heart_rate_monitor basic.launch.py
```
To launch heart rate monitoring with auto stopping of robot
```bash
ros2 launch heart_rate_monitor with_finger.launch.py
```
## Features

- Stop and Go of Scuttle via finger detection
- Real-time heart rate monitoring




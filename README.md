# tickle-me-slow
  Primary attempts to build a Self-driving car, to gloat about on www.medium.com :)
  ## Neural Network
  Train a Network to detect lanes and provide basic steering commands such as forward, left, right or idle.
  Hopefully should be able to work with data, obtained from Mobile camera mounted on vehicle.
  However, I need to code the data extraction code, to work on the Rasberry-Pi 3
  
  Later stages may include:
  1. A separate detection for **stop** signs, Signals, and other Disciplinary actions
  2. Obstacle detection and evasion to avoid humans, other cars and foreign objects on road
  3. Smart Gesture sensing to navigate the vehicle superficially
  
  ## ROS
  Handle the NN-Prediction and achieve real-time steering without mess
  Nodes expected to be running:
  + Image Capture and transfer
  + Neural Network Prediction
  + Steering Command Relay to Arduino Interface
  + GUI on Phone/PC to communicate with Vehicle
  
  ## sources 
  + https://github.com/hamuchiwa/AutoRCCar.git
  + https://www.raspberrypi.org/magpi/self-driving-rc-car/
  + https://hackernoon.com/iarrc2018-b93a2b63c1a6
  + https://medium.com/@rodrigocava/i-built-my-own-self-driving-rc-car-1b269fc02e6c
  + NVIDIA CNN :  https://devblogs.nvidia.com/deep-learning-self-driving-cars/
  + https://github.com/rodrigocava/mrrobot


  # Current-Status
  Pushed car_train.ipynb for training and testing dataset
  ## Instructions for use:
  + Download jupyter Notebook
  + Collect Training and testing data
  + Organize the data in folders in following manner:
    1. `./forward/ *.jpg`
    2. `./left/ *.jpg`
    3. `./right/ *.jpg`
    4. `./idle/ *.jpg`
    1. `./forward_test/ *.jpg`
    2. `./left_test/ *.jpg`
    3. `./right_test/ *.jpg`
    4. `./idle_test/ *.jpg`
  + Run the Notebook to train the data Set and present accuracy
  

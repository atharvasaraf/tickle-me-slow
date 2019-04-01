# tickle-me-slow
  Exploration of self-driving car
  ## Neural Network
  used to train the image from rpi-cam
  this will help in detection of orientation and provide desired heading
  ## opencv
  for image capture
  ## ros 
  to implement control on car
  sources 
  https://github.com/hamuchiwa/AutoRCCar.git
  https://www.raspberrypi.org/magpi/self-driving-rc-car/
  https://hackernoon.com/iarrc2018-b93a2b63c1a6
  https://medium.com/@rodrigocava/i-built-my-own-self-driving-rc-car-1b269fc02e6c
  NVIDIA CNN :  https://devblogs.nvidia.com/deep-learning-self-driving-cars/
  https://github.com/rodrigocava/mrrobot


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
  

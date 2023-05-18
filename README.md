# Team Numeric

Members:
Atish Patange (coach)
Vishwanath Suresh Kumar
Sai Chintakula 
Jayasiamman Prabakaran
         
         
# Robot Details
## Hardware Specifications Descriptions
- Fischertechnik Robotics TXT 4.0 Base Set & Robotics Add On: Autonomus Driving.
- Coding Software: ROBO Pro Coding Software
## Driving mechanism
 -  Steering mechanism with 4 wheels
 -  Two wheels at the back connect with one Encoder motor (for forwards and backwards)
  -  Two wheels at the front connect with the servo motor from Steering mechanism (for left and right turn)
  
## Sensors used
- Camera sensor
- Sonar sensor

## Camera and Image Processing
- Camera sensing the red and green signals using Computer Vision.
- We substracted the RGB values from the treshold to check for the color we want
- If we wanted to sense red --> R_Value-(G_Value+B_Value)>Treshold
- If we wanted to sense green --> G_Value-(R_Value+B_Value)>Treshold

Problem:
- The robot could not detect any color

Solution:
- We reduced the ratio of the selecting box to specify the color and not the background.

## Sonar sensor
- A sonar sensor is a device that uses soundwaves to detect objects and measure distances.
- It emits ultrasonic waves and detects echoes.
- It can be used to map or locate objects in the ocean or surrounding environment.
- We used it to avoid hitting the wall.

Problem:
- We were confused because of our lack of experience.

Solution: 
- We figured out that the new RoboPro Update changed the some codeblocks, so the example code from Fishertechnik was not to be trusted. We figured out out own code after a while by replacing and removing some blocks.

## Algorithm progress
- For learning purpose we programmed Tachometer,Taximeter and Odometer
1.Odometer:Odometer will simply display the Di
         

## Topics learned in Robotics
- Computer Vision
- Sensor Fusion
- Path Planning

## Build Process
ToDo: Compile and Upload, what is the difference
- How it works with Fischer Technik


## Team management
- Sai Chintakula: Coding, building the Robo and editing the videos and photos
- Jayasimman Prabakaran: Coding, helped Vishwa build the Robo
- Vishwanath Suresh Kumar: Coding, wiki,build the Robo



## YouTube account details
- https://www.youtube.com/@TeamNumeric

## Timeline
- 11-03-23: Vishwanath and Jayasimman were building the robo.
- 18-03-23: Sai and Jayasimman were doind the code for the qualification round
- 25-03-23: Everyone was working on the movement code and finshed it.
- 01-04-23: Sai was working on the camera.
- 15-04-23: Vishwa was working on the sonar senser code.
- 22-04-23: All were working on the source code for qualification round and finshed the sonar senser code.
- 29-04-23: All were working on the source code for qualification round.
- 06-05-2023: 
- Sai created the youtube channel and created the videos and photos
- Jayasimman corrected source code for qualification round.
-  Vishwanath wrote the wiki
              
              
- 13-05-2023: Vishwa changed the source code for qualification round.
- 18-05-2023: Vishwa updating the wiki. 
              Sai correcting the qualification code and build the traffic signals.
              Jayasimman starting the final round.
              
              
              
 
 
 
 
# Our Plans

## Qualification Round

We saw that the wall will come till a patikular point so we programmed the robo to move at the boader of the mat.It works but the after for every round the angles 
differs. 
So we used the sonar sensor to detect the wall and to get precise angles.
            
              


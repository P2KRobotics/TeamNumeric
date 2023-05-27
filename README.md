# Team Numeric

Members:
Atish Patange (Coach)
; Vishwanath Suresh Kumar
; Sai Chintakula 
; Jayasimman Prabakaran
         
         
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
 Compiling refers to the process of converting source code into object code. On the other hand, uploading refers to transferring the compiled code (instruction set) to a processor and triggering the execution of the instructions.


## Team management
- Sai Chintakula: Coding, building the Robo and editing the videos and photos
- Jayasimman Prabakaran: Coding, helped Vishwa build the Robo
- Vishwanath Suresh Kumar: Coding, wrote the wiki,build the Robo



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
- 06-05-2023: Sai created the youtube channel and created the videos and photos 
              Jayasimman corrected source code for qualification round.
              Vishwanath wrote the wiki
              
              
- 13-05-2023: Vishwa changed the source code for qualification round.
- 18-05-2023: Vishwa updating the wiki. 
              Sai correcting the qualification code and build the traffic signals.
              Jayasimman starting the final round.
              
 - 20-05-2023: Vishwanath updating the wiki,works on qualification round.
                Jayasimman works on the qualification round. 
                Sai updating the wiki,works on qualification round.
                
 - 20-05-2023: Vishwanath updating the wiki,works on qualification round.
                Jayasimman works on the qualification round. 
                Sai updating the wiki, works on qualification round.
                All tried to solve the problem on qualification round
              
              
 
 
 
 
# Our Plans

## Qualification Round

We tried multiple codes for the qualification round. We knew that there were 6 options where the robot can start from and 6 for the other direction. 

- Version1 : Here we tried a code where the we measured the distances of the walls accurately. The robot just followed the code. We used a single block to go forward and increased the distance by putting it in the repeat block. But it was very inaccurate, because the values became way too high. For turning we just put the servo motor to an angle and continued using the repeat block. The code started to become very big´in length and it was very hard to correct. It was a failure so started with Version2

- Version2 : We started working with variales so it's easier to correct. We stopped using the repeat block and started using Step size for the distance. With that block the code became way less. We succesfully completed 1 round, but there were a lot problems. With each turn the angle became more innacurate so we had a different angle for every turn. We knew we couldn't work like this and it would be very hard to complete 3 rounds.

- Version3 : We completly delted the whole code and started new. This time, we neither did depend on the repeat block or the Step size, but we used the time. We were using functions. For each function (example for going straight or turning) we created a definition. The code became 70% less longer than before. Though the distances were percfect, we faced a new problem with angles. The same code with giving a different output. Sometimes, the angles were completly off eventhough it was the same code. So we had to start a new version.

- Version4 : We are only depending on the sonar sensor to measure the distance to the wall. So if the robot comes to a specific distance, it turns 90 degrees and continues. We created a code that when the robot detects the wall is under 60cm, it turns. But when not detected, it normally continues to go straight. But the code was a complete disaster. Because without detecting the wall itself it turned left.
            
              


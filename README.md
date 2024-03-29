# Team Numeric

Members:

 Swapnil Rudrawar and Atish Patange (Coach)
 
 Sai Charan Chintakula
 
 Vishwanath Suresh Kumar
 
 Jayasimman Prabakaran Sowmiya 
         
         
# Robot Details
## Hardware Specifications Descriptions
- Fischertechnik Robotics TXT 4.0 Base Set & Robotics Add On: Autonomus Driving.
- Coding Software: ROBO Pro Coding Software. We can program the robot both in logical blocks and python. Below image is the sample code written to detect red color ball.

## Driving mechanism
 -  Steering mechanism with 4 wheels
 -  Two wheels at the back connect with one Encoder motor (for forwards and backwards)
  -  Two wheels at the front connect with the servo motor from Steering mechanism (for left and right turn)
  
## Algorithm progress
- For learning purpose we programmed Tachometer,Taximeter and Odometer
1.Odometer:Odometer will simply display the Di
         

## Topics learned in Robotics
- Computer Vision:
  Computer vision uses machine learning and neural insights to teach computers to see problems and problems before they affect operations.
  Computer vision can also help computers recognize objects, track movements, reconstruct scenes and restore images.

- Sensor Fusion: 
  Sensor Fusion is a combination of Sensors. We may use the combination of camera and sonar sensor.

  Sensor Fusion is a combination of Sensors. We may use the combination of camera and sonar sensor.

## Build Process
 Compiling refers to the process of converting source code into object code. On the other hand, uploading refers to transferring the compiled code (instruction set) to a processor and triggering the execution of the instructions.


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
              
 - 23-05-2023: Vishwanath worked on red color signal detecting logic for final round. 
               The code is working and commited to github
               
 - 25-05-2023: Vishwanath,Sai Charan and Jayasimman rebuilt the robot.
              Vishwanath and Jayasimman worked on the Final match code.
              
 - 27-05-2023: Jayasimman worked on green color signal detecting logic for final round. The code is working and commited to github.
               Jayasimman and Viswanath created the schematic Diagram.And wiki.
               Sai Charan worked on the Qualification round. 
	       
 - 29-05-2023: Our Encoder motor gear mechanism used to transfer power to rear wheels broke down. The rear wheels were not rotating properly. 
               We rebuilt the whole robot again, opened the gear mechanism, and fixed the issue. So far robot is moving properly in forward and backward
               direction. Jayasimman, Vishwanath worked on rear wheel gear mechanism. Sai is continue to work on Qualifying round code.
	       
  - 30-05-2023: All were working on the Final Match.
   
  -  31-05-2023: All went through the rules, made final changes for the regional competion in Rüsselsheim.
 
 - 01-06-2023: After facing problems with Fishertechnik TXT4.0 in the regional competition in Rüsselsheim, we decided to change our robot. Last year we worked with Spike Prime at Robosports, so that was our best option.
 - 02-06-2023:
We assembled our Spike Prime robot. We faces an issue: Because we are only allowed to use one encoder motor, the robot was very unstable. The whole day we tried to figure a stable structure
- 03-06-2023:
We started coding with Spike Prime Legacy. We realised that the code for the qualification round is much shorter than it was with RoboProCoding. We finished our code, but we had a problem we never had before: The robot was so unstable that the wheels broke off in the middle of the match, multiple times. Eventhough the code was stable, the robot wasn't. So we gad no other option than to revert back to our Fishertechnik TXT4.0. 
-04-06-2023:
Today something happened that never happened before: The robot didnt crack. Suddenly the robot was very stable. We came back to our old codes and started working on the qualification rounds for clockwise and anti-clockwise
  -  05-06-2023: We worked on the final round. We changed the code completly. The reason was that the code that we wrote before didnt work at Rüsslesheim was because we had specific RGB values. In Rüsslesheim the temperature was different. So now we created a very simple and new logic. If R>G & R>B then do the positions. 
  -  08-06-2023: 
Abd it worked! So we continued fir every other position. But because the positons were different now we needed to do new positions for every condition. This process is the most time consuming. 
  - 9-06-2023:
We continued doinf the positions.
 - 10-06-2023:
Today was the last day we could work, because our school starts from next week. We tried to finish as much as possible and stopped for today.       
	       
# Our Plans

## Qualification Round

We tried multiple codes for the qualification round. We knew that there were 6 options where the robot can start from and 6 for the other direction. 

- Version1 : Here we tried a code where the we measured the distances of the walls accurately. The robot just followed the code. We used a single block to go forward and increased the distance by putting it in the repeat block. But it was very inaccurate, because the values became way too high. For turning we just put the servo motor to an angle and continued using the repeat block. The code started to become very big´in length and it was very hard to correct. It was a failure so started with Version2

- Version2 : We started working with variales so it's easier to correct. We stopped using the repeat block and started using Step size for the distance. With that block the code became way less. We succesfully completed 1 round, but there were a lot problems. With each turn the angle became more innacurate so we had a different angle for every turn. We knew we couldn't work like this and it would be very hard to complete 3 rounds.

- Version3 : We completly delted the whole code and started new. This time, we neither did depend on the repeat block or the Step size, but we used the time. We were using functions. For each function (example for going straight or turning) we created a definition. The code became 70% less longer than before. Though the distances were percfect, we faced a new problem with angles. The same code with giving a different output. Sometimes, the angles were completly off eventhough it was the same code. So we had to start a new version.

- Version4 : We are only depending on the sonar sensor to measure the distance to the wall. So if the robot comes to a specific distance, it turns 90 degrees and continues. We created a code that when the robot detects the wall is under 60cm, it turns. But when not detected, it normally continues to go straight. But the code was a complete disaster. Because without detecting the wall itself it turned left.

## Final Round 
            
## Designed Solution

### Qualifying Round
#### Encoder motor
For qualifying round we are using Fischer technik robot with one encoder motor and one servo. The python or fischer technik block controls the encoder motor to move clock wise
or anticlockwise. We use speed functionality, step size to control the encoder motor. We also use timing function to stop the encoder motor. For example in qualifying round, if we want to move straight
for particular distance we set the speed (for encoder motor) and use it in combination with time functionality to achieve that distance.

#### Servo motor
Servo motor. Servo motor is used for steering mechanism. We use three different angles for steering. 160 degree for straight, 250 degree for left and 60 degree for riight. But servo motor is not precise or
may be due to mechaniscs limitations and surface inclinations our turning angle changes. We use servo blocks from fischer technik/python to turn our servo motor left, right and center. Using that we can turn the robot. E.g. When we detect Red signal, we try to turn around.

In below image, configuration windows for Fischertechnik robot is shown. Here we connected Sevo and encoder motors.


### Final Round
#### Encoder motor
Same working as qualifying round

#### Servo motor
Same working as qualifying round

#### Camera
We are using camera to detect signals. Our detection algorithm uses color information from signals. We used Fischer Technik's camera configuration block to get the RGB Pixels values. The RGB pixesl
values are then meaned over rectangle box. The rectangle box is also called as region of interest. In Fischer technik it is called as color_detector box. 

We later used RGB values in our if blocks (python as well as fischer technik software) to compare whether they are greater or smaller than threshold. And there is combination of threshold and if logic
to detect green and red signals. 

Then upon detecting green color using above logic, later we wrote codes to turn our servo motor to right side, straight and then left. We did this so that robot can keep the green signal to left.

Then upon detecting red, we did the same above logic but in opposite direction. We also use encoder motor to move robot forward and backward direction.

For examle in below image we are using color detection algorithm from Fischertechnik. We are considering RGB values to detect possible red color blob in image. 



### Final Match Idea :

We used the camera to sense the color of the signal Red and green. And used the sonar sensor to turn precisly and to avoid the walls.  We use two colordetector for the two different positions where the signal could be. The detector are placed in the middle of the mat. So that the other signals can also be detected. And blocked the gaps so the camera will not give wrong readings. After the first color, we could have programmed the robot so that it directly goes to the next block. But we insisted, because if we use the sonar sensor the code will be much shorter. We have multiple color detectors, one for green and one for red.   

### Spontaneous change of Hardware
After finishing the WRO on a regional level, we came to the decision to switch our robot to Spike Prime. Because we already worked woth Spike Prime last year in Robosports, we thought it would be easier. We did our own design with one encoder motor, servo motor and 3 sonar sensors. We completly tried 3 combinations.
- Try1 (5th June): We first used one sonar sensor in the front. Because now the software changed, other blocks need to be used. We used the blocks •when• for detecting the wall and then turning.  But we faced the same problems as with TXT 4.0: the robot was gradually increasing the angles. We only wanted to concentrate on the qualification rounds first. One thing we noticed was that Spike Prime took less rotations to reach the same position as with TXT 4.0.
- Try2: We used two sonar sensors: an additional one on the left. We programmed so that when the side sensor detects something closer than 5 cm, it should gradually turn to the right. The first round was fine, but entering the second round the robot crashed the right wall. 
-  Try3: Now we had 3 sonar sensors. Just so that the right sensor when detected gradually moves left. We thought eventually it will just move in the middle, but we were wrong. In spike prime 3 we had the problem that the code was getting finished to the end. So if the side sensors detected something and short after the wall in the front was closer, the robot finished the code of the side sensors, so it crashed to the wall. And it kept on getting disoriented. Because we only had one encoder motor, the robot was overall unstable. The pieces of the robot randomly kept falling apart in the middle of the round. 
So why face problems we never faced?  We decided to revert back to TXT 4.0!

![_MG_9568 00_00_07_21 Still002(1)](https://github.com/P2KRobotics/TeamNumeric/assets/118617386/40d2d9da-7a62-4583-b3c3-b0020799171e)
![schematic diagram Spike Prime](https://github.com/P2KRobotics/TeamNumeric/assets/118617386/e3bfa46a-e829-427a-97a3-934ee4d67bb8)

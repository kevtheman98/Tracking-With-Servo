Object Tracking using OpenCv with python and Elagoo super started kit

This is my first somewhat major project with the Elagoo super starter kit, the main things I learned with how to use the microcontroller and the various functionns from the arduino ide and OpenCv for object tracking with python. 

Objective-
The camera tracks the top half of the frame and measures the angle between the center/motor and the object this is shown by the red line. The python file sends the angle that it calculated to the microcontroller and that tells the motor where to go. This also updates the LCD display with the angle it is currently at and the distance the object is from the motor.

Materials-
LCD display
Elagoo Uno r3
Power distrubuter module
Servo motor
Potienmeter
Ultrasonic Sensor
Two Pens

Learned-
I used Paul Mchorters youtube tutorials for the hardware side and then used opencv docs and other youtube videos for the software side. I spent a lot of time trying to make it work with the stepper motor but without knowing the position of the motor I realized that the servo was a much easier and better option for this project. I also was at first overwhelmed with the amount of diffrent things you can do with opencv, eventually figured out the drawing the countours and using .moments to find the centroid was the key for this project.


<video src="https://github.com/user-attachments/assets/2b3aa77e-80a5-498f-8e86-c220a2965edc" width=100 length=100></video>


![image2](https://github.com/user-attachments/assets/4b349cc0-2533-46bf-b540-2f07b63e6be7)
![image1](https://github.com/user-attachments/assets/79342086-a339-42c6-a9ba-39071275adf0)
![image0](https://github.com/user-attachments/assets/970c8874-f13f-4138-a666-564c6dc920d2)
![image3](https://github.com/user-attachments/assets/4cdaeae0-90a7-4b03-8486-99599405f210)



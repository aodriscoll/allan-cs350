# CS-350 Emerging System Architecture & Technology

```
 _____ _   _  _   _ _   _   _____  _____       _____ _____  _____ 
/  ___| \ | || | | | | | | /  __ \/  ___|     |____ |  ___||  _  |
\ `--.|  \| || |_| | | | | | /  \/\ `--. ______   / /___ \ | |/' |
 `--. \ . ` ||  _  | | | | | |     `--. \______|  \ \   \ \|  /| |
/\__/ / |\  || | | | |_| | | \__/\/\__/ /     .___/ /\__/ /\ |_/ /
\____/\_| \_/\_| |_/\___/   \____/\____/      \____/\____/  \___/ 
```                                                               

## Course Information

|              |                                                                                                                                                                            |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Institution  | Southern New Hampshire University                                                                                                                                          |
| Course       | [CS-350-14554-M01 Emerging Sys Arch & Tech 2025 C-2 (Mar - Apr)](https://learn.snhu.edu/d2l/home/1860290 "CS-350-14554-M01 Emerging Sys Arch & Tech 2025 C-2 (Mar - Apr)") |
| Instructor   | **Roland Morales, M.S.** r.morales3@snhu.edu                                                                                                                               |
| GitHub       | @rmorales3snhuedu                                                                                                                                                          |
| Linked In    |                                                                                                                                                                            |
| Course Dates | 3/03/2025 - 4/27/2025                                                                                                                                                      |
| Status       | Active/Online                                                                                                                                                              |


## Artifacts

| Description                                           | Link                                                                                                                                                                         |
| :---------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Milestone Three Input With Buttons Lab Reflection     | [Allan_ODriscoll_CS350_5_1_Milestone_Three_Input_With_Buttons_Lab_20250405.docx](artifacts/Allan_ODriscoll_CS350_5_1_Milestone_Three_Input_With_Buttons_Lab_20250405.docx)             |
| Milestone Three Input With Buttons Lab Diagram        | [Allan_ODriscoll_CS350_5_1_Milestone_Three_Input_With_Buttons_Lab_20250405.drawio.pdf](artifacts/Allan_ODriscoll_CS350_5_1_Milestone_Three_Input_With_Buttons_Lab_20250405.drawio.pdf) |
| Milestone Three Input With Buttons Lab Python Script  | [Allan_ODriscoll_Milestone3.py](artifacts/Allan_ODriscoll_Milestone3.py)                                                                                                               |
| Final Project Thermostat Lab Report                   | [Allan_ODriscoll_CS350_7_2_Final_Project_Thermostat_20250419.docx](artifacts/Allan_ODriscoll_CS350_7_2_Final_Project_Thermostat_20250419.docx)                                         |
| Final Project Thermostat Lab Diagram                  | [Allan_ODriscoll_CS350_7_2_Final_Project_Thermostat_20250419.drawio.pdf](artifacts/Allan_ODriscoll_CS350_7_2_Final_Project_Thermostat_20250419.drawio.pdf)                             |
| Final Project Thermostat Lab Python Script            | [Allan_ODriscoll_Thermostat.py](artifacts/Allan_ODriscoll_Thermostat.py)                                                                                                               |

## Summarize the project and what problem it was solving.

This course explored various aspects of embedded systems including microcontrollers and single board computers like the Raspberry Pi. The final project involved the creatioin of a thermostat similar to one that you might find in your home. The thermostat consisted of a Raspberry Pi, a temperature sensor, several buttons, an LCD display, and several light indicators. The idea was to simulate the functionality of a thermostat to head and cool the environment based on an active temperature reading and a temperature set point. The requirements for this project included the following:

- The device must have a mechanism to set the mode to either OFF, HEAT, or COOL. This is accomplished with a button (green) that cycles through the three possible modes. This button is connected to the system through GPIO pin 24. The software implements an interrupt-driven state machine that handles the transition between the various modes.
- The device must have a mechanism to define a temperature set point. This is accomplished with two buttons connected to GPIO pins 12 and 25. The first button (red) increases the set point by one degree. The second button (blue) decreases the set point by one degree. When the unit starts, the set point should be initialized to 72 degrees Fahrenheit, but it may be adjusted to the user’s desired temperature using the buttons. Button presses generate interrupt signals that allow the system to react.
- The device must be capable of sensing the ambient temperature in the room. This is accomplished through the use of an AHT20 temperature sensor that communicates using the I2C protocol.
- The device must have a visual indication of the current mode of operation. This is accomplished through the use of two light-emitting diodes. When the system is OFF, both lights will also be off. When the system is in HEAT mode, a red light will be on and will pulse when the system is actively heating. When the system is in COOL mode, a blue light will be on and will pulse when the system is actively cooling.
- The device must have an LCD display that displays the current date and time on one line and alternates between the current temperature reading and the mode plus temperature set point on the second line. The thermostat will use a 1602A LCD for this purpose, along with several additional GPIO pins for communication.
- The device must communicate the mode, temperature reading, and set point with the systems servers. In the prototype, this activity is simulated using several serial ports (i.e., the UART).

The project was delivered as a prototype on a breadboard along with a video demonstration and a report. Here is an image of the result:

![Image of Final Project](images/IMG_7729_2.png)

## What did you do particularly well?

## Where could you improve?

## What tools and/or resources are you adding to your support network?

## What skills from this project will be particularly transferable to other projects and/or course work?

## How did you make this project maintainable, readable, and adaptable?
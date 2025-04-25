FRAMEWORK USED
- I used Flask as the main web framework for this project.

HOW TO RUN THE PROJECT
1. I started by installing VirtualBox and Ubuntu Linux on my device.
2. I created a virtual machine in VirtualBox and set the network to NAT so I could access the internet inside the VM.
3. After that, I updated and upgraded all the necessary packages inside the VM.
4. I installed Python3 and created a virtual environment for the project.
5. I activated the virtual environment and installed Flask using pip.
6. I created a folder that contained my app.py and other necessary files like my HTML templates.
7. I configured the firewall (if needed) to allow access on port 5000.
8. I launched the Flask server using host="0.0.0.0" and port=5000.
9. I was then able to access the application using http://192.168.1.17:5000 on both the VM and my host machine.

ISSUE I ENCOUNTERED AND HOW I FIXED IT

Issue:
When I tried to run the app using python3 main.py, I got an error saying:
"Address already in use. Port 5000 is in use by another program. Either identify and stop that program, or start the server with a different port."

Solution:
To fix it, I typed the command lsof -i :5000 in the terminal. It showed the PID of the process using port 5000 — in my case, it was 75399. I stopped the process by running kill 75399, and after that, the Flask server started successfully.

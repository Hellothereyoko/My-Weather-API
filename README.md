#Author: Yoko Parks
#Class:  CSCD 330 EWU Tony Espinoza
#Date:   16th April 2025


#About The Program:
This program takes a domain passed into the terminal and plots the 
weather forecast by hour on a graph. (With a maxima of 160hrs)
The program utilizes modular design where the functions are predefined, then called in main.
The program will display the API call, Coordinates, and temps. This is to have some user feedback
that the program is functioning.


#See below:
Step 1: Resolves Domain to IP
Step 2a: Resolves IP to Physical Address
Step 2b: Parses Returned Address in Human Readable Fields
Step 3: Resolves Physical Address into Coordinates
Step 4: Fetches Weather @ Coordinates
Step 5: Plots Temps Over 160hrs


#Syntax:
python3 lab2.py <domain>


#Example:
python3 lab2.py google.com



##################################################
#             Laboratory Questions:              #
##################################################

# 1) What is an API?
APIs(Application Programming Interface) are a set of rules &
specifications that allow software to communicate with each other.

# 2) What is a RESTful API? Were the APIs we used RESTful?
A RESTful API is stateless client/server communication that manipulates data in 
some way. By that definition, I would say that they were.

# 3) What is a JSON? Did these APIs use JSON?
A Java Script based text format, used to store & exchange data.
These APIs used JSON to store weather and location data such as temps 
& coordinates.

# 4) What is Bash? Have you ever used Bash?
Bash(Born Again SHell) is a terminal interpreter for Linux to enable control
of system operations. I have used BASH a lot in Linux Programs like my Minecraft Server.






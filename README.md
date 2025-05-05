
<div align="center">
  
# $${\color{red}About} {} {\color{red}The} {} {\color{red}Program:}$$

</div>


<div align="left">
This program takes a domain passed into the Ubuntu terminal and plots the 
weather forecast by hour on a graph. (With a maxima of 160hrs)
The program utilizes modular design where the functions are predefined, then called in main.
The program will display the API call, Coordinates, and temps. This is to have some user feedback to ensure
that the program is functioning.

Check out my implementation of this API in a Python FLASK server at: 

</div>
<br>


<div align="center">
  
# $${\color{red}Program} {}  {\color{red}Outline:}$$

</div>


<div align="left">
  
- ### $${\color{red}Step} {} {\color{red}1:}$$  Resolves Domain to IP
- ### $${\color{red}Step} {} {\color{red}2a:}$$ Resolves IP to Physical Address
- ### $${\color{red}Step} {} {\color{red}2b:}$$ Parses Returned Address in Human Readable Fields
- ### $${\color{red}Step} {} {\color{red}1:}$$  Resolves Physical Address into Coordinates
- ### $${\color{red}Step} {} {\color{red}4:}$$  Fetches Weather @ Coordinates
- ###  $${\color{red}Step} {} {\color{red}5:}$$ Plots Temps Over 160hrs

</div>

<div align="center">
  
# $${\color{red}Syntax:}$$

    python3 lab2.py DOMAIN_HERE

</div>



<div align="center">

## $${\color{red}Example:}$$

    python3 lab2.py google.com

</div>

<br>


  

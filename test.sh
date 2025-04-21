#!/bin/bash

# Author: Yoko Parks
# Class:  CSCD 330 EWU Tony Espinoza 
# Date:   16 April 2025 


test_num=3
dmn1=google.com
dmn2=bsideportfolio.com
dmn3=poptropica.com


echo -ne "This Program moves onto cases after closing the plotter.\n"
echo -ne "Close the plotter to move onto the next test automatically. (will close in 5sec.)\n"
sleep 5

for((i = 1; i < test_num + 1; i++));

do

  domain_var="dmn$i"
  domain="${!domain_var}"

  echo "Starting Test $i: $domain"
  python3 lab2.py "$domain"

done


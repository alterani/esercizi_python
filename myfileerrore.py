#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 19:22:21 2018

@author: enricoalterani
"""

mylist = [1,2,3,4,5,6]
while True:
    try:
        data = input('Digita un numero che sia compresso tra -%d e %d oppure 9  per uscire\nDigita un numero......   ' 
                 %(len(mylist), len(mylist) -1))
        num = int(data)
        if(num == 9):
            break
        print(mylist[num])       
    except(ValueError, IndexError):       
        print("\n\n\n\nATTENZIONE: Numero non valido")
    
print('\n\n\n\n\ Programma terminato!!')
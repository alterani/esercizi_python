#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 14:44:55 2018

@author: enricoalterani
"""
#######################  OPERAZIONI SU FILE #######################

# Aperura file
f = open('enrico.txt')
print("Il nome del file  è: " + f.name)
print("L'encoding del file e: "  + f.encoding)

f.close()


#chiusura file
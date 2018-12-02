#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 14:44:55 2018

@author: enricoalterani
"""
#######################  OPERAZIONI SU FILE #######################

# Creazione file file
#f = open('enrico.txt', 'w')

#Aprtura file
f = open('enrico.txt')

print("Il nome del file  è: " + f.name)
print("L'encoding del file e: "  + f.encoding)

#legge tutto il file

testoFile = f.read()
print(testoFile)
    
f = open('enrico.txt')
#legge una riga del file
rigaFile = f.readlines()

print(rigaFile)


#SALVA FILE
f.close()

"""  NOTA
La funzione read si comporta come un cursore. Quando la chiami il cursore si trova alla
fine del file. Quindi per riposizionare il cursore in alto bisogna chiamare di nuovo
la fuzzione Open

"""

"""
SCRIVERE SUI FILE
"""

f = open('enrico.txt', 'w')

print('testo del file \naltra riga fiel\nterza riga del testo del fiel', file = f, flush= True)
f= open('enrico.txt')
testoFile = f.read()
print(testoFile)




############## FUNZIONI DI INTERPOSIZIONE #########################

type('stringa') # Se si passa unggetto restituisce il tipo di oggetto

hasattr('stringa', 'real') #booleana: restituisce true se l'oggetto contiene l'attributo

dir('oggetto') # restituisce l'elenco deglli attributi 

isinstance(3,int) #ci dice se l'oggetto è un'istanza di della classe


# is: ci dice se due oggetti sono identici
a=2
b=2

a is b  #True

c = 3
d = 4

c is d #False


############ DIR() & HELP()

# DIR = Principali attributi di un oggetto 
# Help = Descrive l'attributo


dir('stringa')

help('lower'.lower)























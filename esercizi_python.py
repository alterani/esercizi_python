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


################################
# list comprehension esercizio
##############################

"""
Data la stringa '33;91;77;15' generare la somma di tutti i numeri in esse contenuti
divisi dal carattere ;
Per farlo usiamo la sintassi List comprehension
"""

'33;91;77;15'

sum([int(item) for item in '33;91;77;15'.split(';')])

# funziona anche scrivendo il tutto senza parentesi perchè in questo
#caso sarebbe un 'generator expression' 

sum(int(item) for item in '33;91;77;15'.split(';'))


###############################################
###### ESPRESSIONI CONDIZIONALI
#
#<ESPRESSIONE 1> IF <TEST> ELSE <ESPRESSIONE2>
################################################

x = 'a' if 4 ==  2 + 2 else 'b'  # x è uguale a 
x = 'a' if 4 ==  3 + 2 else 'b'  # x è uguale b


######## CREARE UNO SWITCH CASE ###########

def switch(codice):
    d = {0: len, 1: min, 2: max }
    return d.get(codice, sum)  # la funzione get ristorna il valore associato alla key "primo parametro"
                              #oppure il valore di default "secondo parametro"
switch(0)([1,2,3])  # len = 3
switch(1)([5,9,1])  # min = 1
switch(2)([5,9,1])  # max = 9
switch(9)([5,9,1])  # sum = 15  (parametro di default)



################# FOR CON ELSE ################
# L'else viene eseguito se il ciclo è stato 
# interrotto senza l'interruzione break.

# NOTA: L'istruione else esiste anche per il ciclo while
###########################################

# Esempio con else eseguito

for i in range(5):
    print(i+1)
    if i == 6:
        break
else:
    print('else eseguito')

# Esempio con else non eseguito perchè il
#ciclo è interrotto da un break

for i in range(10):
    print(i+1)
    if i+1 == 6:
        break
else:
    print('else eseguito')


#####################################################    
#################### WHILE - break e continue #######
#####################################################

while True:
    dati_utente = input('Digita qualcosa:  ')
    if dati_utente == 'esci':
        print('interrompo il ciclo')
        break
    elif (dati_utente == 'qqq'):
        print('interrompo il blocco e continuo il ciclo')
        continue
    print(dati_utente)                
    

################ COMIPILAZIONE DEI FILE ##############
# Per questo esercizio ho creato un modulo da importare che si chiama
# m.py
######################################################
    
# quando un modulo viene importato pytho lo compila in automatio
# e crea una sotto cartella __pycache__ ed all'interano di esse genera
#il un file conestensone <nome_modulo>.cpython-<versione>.pyc che sarebbe il modilo 
#compilato in binario. 
# nel nostro caso ha creato la cartella __pycache__ ed all'interno il file m.cpython-37.pyc
# è possibile eseguire direttamente il binario es: python __pycache__/m.cpython-37.pyc
'''
L'attributo magico __file__ contiene il nime ed il percorso del file del modulo importato
L'attibito __cached__ è come __file__ ma si riferisce al file compilato
'''    

################## ATTRIBUTI MAGICI ###########
'''

__class__   Restituische il tipo di oggetto stessa info si ottiene con type(<oggetto>) 
__file__    L'attributo magico __file__ contiene il nime ed il percorso del file del modulo importato
__cached__ L'attibito __cached__ è come __file__ ma si riferisce al file compilato
    
''''
    












































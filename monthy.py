#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 17:57:14 2020

@author: walberto

Problema de Monty Hall

Las puertas son 0,1,2

"""
import random

# Variables importantes

n = int # Numero de juegos
Gana_p = int # Numero de juegos ganados al presistir
Gana_c = int # Numero de juegos ganados al cambiar
puerta = int # Numero de la puerta ganadora
Elec = int # Puerta escogida por el concursante
Elec2 = int # Puerta cambiada
cabra = int # Puerta que abre monty y tiene cabra

random.seed = 27122003

def Concurso():
    """ Esta fucnión simula el concurso de mounty """
    p = (random.random()*3)//1
    return(p)
    
def Eleccion():
    """ Esta función elige una puerta por el concursante """
    E = (random.random()*3//1)
    return(E)
    
def Abrir():
    """ Esta función abre una puerta que no es la premiada"""
    puertas = {0,1,2}
    if Elec != puerta:
        puertas.remove(Elec)
        puertas.remove(puerta)
        Abierta = puertas.pop()
        
    else:
        puertas.remove(Elec)
        Abierta = puertas.pop()
        
    return(Abierta)

def Cambio():
    """ Esta funcion cambia la eleccion hecha originalmente"""
    puertas = {0,1,2}
    puertas.remove(Elec)
    puertas.remove(cabra)
    N_Elec = puertas.pop()
    return(N_Elec)
    
# Configuramos el numero de corridas
    
n = 10000
Gana_p = 0
Gana_c = 0

for i in range(n):
    puerta = Concurso()
    Elec = Eleccion()
    cabra = Abrir()
    Elec2 = Cambio()
    
    # Si el jugador persiste con la desision
    if puerta == Elec:
        Gana_p += 1
        
    # Si el jugador cambia de puerta 
    if puerta == Elec2:
        Gana_c += 1
        
#Resultados:
prob_p = Gana_p/ n
prob_c = Gana_c/ n
print("Probabilidad de ganar al no hacer cambio: "+str(prob_p))
print("Probabilidad de ganar al cambiar: "+str(prob_c))
    
    

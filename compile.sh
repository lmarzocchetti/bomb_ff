#!/bin/bash

cython --embed -o tmp.c main.py

gcc -Os -I /usr/include/python3.8/ -o bomb_ff tmp.c -lpython3.8 -lpthread -lm -lutil -ldl

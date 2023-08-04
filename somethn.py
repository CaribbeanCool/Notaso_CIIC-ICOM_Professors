"""
A module to clear the screen.
"""
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return ("   ")
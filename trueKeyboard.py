import click
from os import system

prsian_alphbet = "ضصثقفغعهخحجچپشسیبلاتنمکگظطزرذدئو./ " 
english_alphabet = "qwertyuiop[]\\asdfghjkl;'zxcvbnm,./ "
answer = ''
x = ''

while x != '-':
    system('cls')
    print(answer)
    x = click.getchar()
    indexNumber = english_alphabet.find(x)
    answer += prsian_alphbet[indexNumber]


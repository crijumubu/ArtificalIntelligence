#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

#regex = r"[\w|áéíóú|\`\!\@\¿\?]+"
regex = r"[\d\.\d]+|[\w|áéíóú]+|[\!\¡\.\?\(\)\=\>\<']"

print('TEST 1:\n')

text = 'El dólar en Colombia cerró la semana del 26 al 30 de septiembre y el noveno mes del 2022, con un comportamiento muy fuerte al alza y a menos de 7 pesos de los ¡4.600! pesos.'

print('\tOriginal text:', text, '\n')
print('\tTokenization:' , re.findall(regex, text))

print('\n\nTEST 2:\n')

text = 'url_match(\'<a href=\"test\">\', \'test\')'

print('\tOriginal text:', text, '\n')
print('\tTokenization:' , re.findall(regex, text))
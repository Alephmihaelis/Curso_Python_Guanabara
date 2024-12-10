
'''
Crie um código em Python que teste se um site está acessível no computador usado.
'''

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com')

except urllib.error.URLError:
    print('O site não está acessível no momento.')

else:
    print('Tudo certo! ;D')

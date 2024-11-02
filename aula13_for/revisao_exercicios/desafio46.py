
# Importa a biblioteca `emoji`
import emoji

# Importa a função `sleep` da biblioteca `emoji`
from time import sleep

# Faz o `loop` que conta de 10 a 0
for second in range(10, -1, -1):
    # Mostra na tela cada segundo
    print(second)

    # Faz o computador esperar 1 segundo antes de mostrar o próximo `print` dentro do laço
    sleep(1)

# Mostra na tela `emojis` de fogos de artifício
print(emoji.emojize(':fireworks:'*100))

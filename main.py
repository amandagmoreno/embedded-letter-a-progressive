from machine import Pin
import neopixel
import time

# ===============================
# CONFIGURAÇÕES
# ===============================
BOTAO_A = Pin(5, Pin.IN, Pin.PULL_UP)
LED_PIN = 7
NUM_LEDS = 25

BRILHO = 0.08
DEBOUNCE_MS = 300

leds = neopixel.NeoPixel(Pin(LED_PIN), NUM_LEDS)

# ===============================
# MAPEAMENTO CORRETO DA MATRIZ
# ===============================
def idx(linha, coluna):
    linha = 4 - linha
    coluna = 4 - coluna
    return linha * 5 + coluna

# ===============================
# LETRA A (ORDEM DE FORMAÇÃO)
# ===============================
letra_A = [
    (0,1),(0,2),(0,3),
    (1,0),(1,4),
    (2,0),(2,1),(2,2),(2,3),(2,4),
    (3,0),(3,4),
    (4,0),(4,4)
]

# ===============================
# ESTADO
# ===============================
indice = 0
ultimo_tempo = 0

# ===============================
# FUNÇÕES AUXILIARES
# ===============================
def limpar():
    for i in range(NUM_LEDS):
        leds[i] = (0, 0, 0)
    leds.write()

def atualizar_A(qtd):
    limpar()
    for i in range(qtd):
        l, c = letra_A[i]
        leds[idx(l, c)] = (int(255 * BRILHO), 0, 0)
    leds.write()

# ===============================
# INÍCIO
# ===============================
print("Projeto: Letra A Progressiva")
limpar()

# ===============================
# LOOP PRINCIPAL
# ===============================
while True:
    if BOTAO_A.value() == 0:
        agora = time.ticks_ms()

        if time.ticks_diff(agora, ultimo_tempo) > DEBOUNCE_MS:
            ultimo_tempo = agora

            indice += 1

            if indice > len(letra_A):
                indice = 0
                limpar()
            else:
                atualizar_A(indice)

    time.sleep(0.05)

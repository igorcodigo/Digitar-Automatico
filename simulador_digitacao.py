import pyautogui
import time
import keyboard
import sys
import threading

# Coloque seu texto aqui - fácil de modificar
# Basta substituir todo o conteúdo entre as aspas triplas
TEXT_TO_TYPE = """cole seu texto aqui"""

# Variável global para controlar a execução
running = True

def check_mouse_position():
    """Monitora a posição do mouse e para o programa se estiver em um canto"""
    global running
    
    # Obtém o tamanho da tela
    screen_width, screen_height = pyautogui.size()
    
    # Define a área de sensibilidade para os cantos (em pixels)
    corner_sensitivity = 10
    
    while running:
        # Obtém a posição atual do mouse
        x, y = pyautogui.position()
        
        # Verifica se o mouse está em algum dos cantos
        in_top_left = x <= corner_sensitivity and y <= corner_sensitivity
        in_top_right = x >= (screen_width - corner_sensitivity) and y <= corner_sensitivity
        in_bottom_left = x <= corner_sensitivity and y >= (screen_height - corner_sensitivity)
        in_bottom_right = x >= (screen_width - corner_sensitivity) and y >= (screen_height - corner_sensitivity)
        
        # Se o mouse estiver em qualquer canto, interrompe o programa
        if in_top_left or in_top_right or in_bottom_left or in_bottom_right:
            print("Mouse detectado em um canto da tela. Parando o programa...")
            running = False
            break
            
        # Pequena pausa para não sobrecarregar o CPU
        time.sleep(0.02)

def type_text(text=TEXT_TO_TYPE, delay=0.1):
    global running
    for char in text:
        # Verifica se o programa deve continuar
        if not running:
            print("Digitação interrompida!")
            return
            
        if char == '\n':
            keyboard.press_and_release('enter')
        else:
            # Usa o método write do keyboard que suporta caracteres Unicode
            keyboard.write(char)
        time.sleep(delay)  # Pausa entre as teclas para parecer mais humano
    
    print("Digitação concluída com sucesso!")

if __name__ == "__main__":
    # Inicia o thread para monitorar a posição do mouse
    mouse_monitor = threading.Thread(target=check_mouse_position)
    mouse_monitor.daemon = True  # O thread terminará quando o programa principal terminar
    mouse_monitor.start()
    
    print("Aguardando 5 segundos antes de iniciar...")
    time.sleep(5)
    
    print("Para interromper o programa, mova o mouse para qualquer canto da tela.")
    if running:
        type_text()
    
    # Encerra o programa após a conclusão da digitação
    running = False
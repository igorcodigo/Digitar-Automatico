# Projeto de Digitador para Acessibilidade e Inclusão

## Visão Geral
Este projeto tem como objetivo promover a inclusão digital e a acessibilidade para pessoas com deficiência motora. A ferramenta desenvolvida automatiza a digitação de textos, possibilitando que usuários com dificuldades motoras possam interagir de maneira mais eficiente com dispositivos eletrônicos.

## Funcionalidades
- **Automatiza a digitação de textos**: O sistema escreve automaticamente um texto predefinido, facilitando a interação de pessoas com limitações motoras.
- **Interrupção fácil**: O programa pode ser interrompido ao mover o mouse para qualquer canto da tela, permitindo um controle rápido e intuitivo.
- **Simulação de digitação humana**: Insere pausas entre as teclas para imitar a digitação natural, proporcionando uma experiência mais realista.

## Tecnologias Utilizadas
- **Python**
- **Bibliotecas**:
  - `pyautogui` para controle do mouse e teclado.
  - `keyboard` para a entrada de texto.
  - `threading` para monitoramento simultâneo da posição do mouse.

## Como Usar
1. Instale as dependências necessárias:
   ```sh
   pip install pyautogui keyboard

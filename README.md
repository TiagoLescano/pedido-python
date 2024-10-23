# 🐍 SAIDINHA MAIS CEDO em Python

Este projeto é uma aplicação gráfica divertida e interativa desenvolvida em Python com a biblioteca Tkinter. Ele simula um pedido de "saidinha mais cedo" em uma interface que tem dois botões com comportamentos diferentes: um que foge do mouse e outro que exibe uma mensagem engraçada ao ser clicado.

## 📜 Descrição do Projeto

A aplicação apresenta um **pedido de autorização** com uma pergunta descontraída: **"Posso sair mais cedo, libera aí?"**. O usuário tem duas opções para responder:

- **Botão "Sim"**: Quando clicado, exibe uma mensagem humorística.
- **Botão "Não"**: Tenta fugir do cursor do mouse, tornando difícil clicá-lo. Se o usuário conseguir, o botão é removido da interface.

O comportamento imprevisível do botão "Não" proporciona uma experiência divertida e interativa para o usuário.

## ⚙️ Funcionalidades

- 🔒 **Movimento Dinâmico do Botão "Não"**: O botão "Não" se move aleatoriamente quando o mouse se aproxima.
- 📩 **Exibição de Mensagem**: O botão "Sim" exibe uma caixa de diálogo com uma mensagem engraçada.
- 🎨 **Estilização Personalizada**: Uso de cores e fontes modernas para criar uma interface visualmente agradável.

## 🛠️ Tecnologias Utilizadas

- 🐍 **Python**: Linguagem de programação usada para desenvolver a aplicação.
- 🖼️ **Tkinter**: Biblioteca para criação da interface gráfica.
- 🎲 **Random**: Utilizada para gerar coordenadas aleatórias para o botão "Não".

## 📋 Estrutura do Projeto

1. **Janela Principal**: Janela de 600x600 pixels com fundo cor de rosa claro (`#EE82EE`).
2. **Texto Principal**: Exibe a frase "Posso sair mais cedo, libera aí?" com fonte `Montserrat`, em tom vinho.
3. **Botão "Sim"**: Fixo e fácil de clicar, exibe uma mensagem de humor quando pressionado.
4. **Botão "Não"**: Móvel e escorregadio, se reposiciona ao se aproximar do mouse e é removido quando clicado.
5. **Caixa de Diálogo**: Ao clicar em "Sim", é exibida uma mensagem popup.

## 🚀 Como Executar o Projeto

1. Certifique-se de ter o Python instalado.
2. Execute o comando abaixo no terminal para rodar o projeto:

   ```bash
   python seu_arquivo.py

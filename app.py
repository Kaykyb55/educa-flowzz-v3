import streamlit as st
import time
import random
import datetime

# Configuração da página
st.set_page_config(
    page_title="Educa.Flowzz AI - Como ChatGPT",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Ultra Avançado
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }
    
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .stApp {
        background: transparent;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .stButton>button {
        background: linear-gradient(45deg, #ff6b6b, #ee5a24);
        color: white;
        border: none;
        padding: 15px 30px;
        border-radius: 25px;
        font-weight: bold;
        font-size: 16px;
        transition: all 0.3s ease;
        box-shadow: 0 5px 20px rgba(255, 107, 107, 0.4);
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(255, 107, 107, 0.6);
    }
    
    .chat-container {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border-radius: 25px;
        padding: 30px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.3);
        min-height: 500px;
    }
    
    .user-message {
        background: linear-gradient(45deg, #00b894, #00a085);
        color: white;
        padding: 18px 24px;
        border-radius: 25px 25px 8px 25px;
        margin: 15px 0;
        max-width: 75%;
        margin-left: auto;
        box-shadow: 0 8px 20px rgba(0, 184, 148, 0.4);
        animation: slideInRight 0.4s ease;
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    .bot-message {
        background: linear-gradient(45deg, #6c5ce7, #a29bfe);
        color: white;
        padding: 20px 25px;
        border-radius: 25px 25px 25px 8px;
        margin: 15px 0;
        max-width: 75%;
        margin-right: auto;
        box-shadow: 0 8px 20px rgba(108, 92, 231, 0.4);
        animation: slideInLeft 0.4s ease;
        border: 1px solid rgba(255, 255, 255, 0.3);
        line-height: 1.6;
    }
    
    @keyframes slideInLeft {
        from { transform: translateX(-30px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideInRight {
        from { transform: translateX(30px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    .header-premium {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(15px);
        padding: 30px;
        border-radius: 30px;
        text-align: center;
        margin-bottom: 30px;
        border: 2px solid rgba(255, 255, 255, 0.3);
        animation: glow 3s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from { box-shadow: 0 0 25px rgba(255, 255, 255, 0.3); }
        to { box-shadow: 0 0 35px rgba(255, 255, 255, 0.5); }
    }
    
    .input-modern {
        background: rgba(255, 255, 255, 0.12);
        backdrop-filter: blur(15px);
        padding: 25px;
        border-radius: 25px;
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.2);
        border: 2px solid rgba(255, 255, 255, 0.25);
        margin-top: 20px;
    }
    
    .typing-animation {
        overflow: hidden;
        border-right: 3px solid #fff;
        white-space: nowrap;
        animation: typing 3.5s steps(50, end), blink-caret 0.75s step-end infinite;
    }
    
    @keyframes typing {
        from { width: 0; }
        to { width: 100%; }
    }
    
    @keyframes blink-caret {
        from, to { border-color: transparent; }
        50% { border-color: #fff; }
    }
    
    .glowing-text {
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.8);
        animation: text-glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes text-glow {
        from { text-shadow: 0 0 10px rgba(255, 255, 255, 0.8); }
        to { text-shadow: 0 0 20px rgba(255, 255, 255, 1); }
    }
</style>
""", unsafe_allow_html=True)

# Base de conhecimento INFINITA
CONHECIMENTO_INFINITO = {
    "matematica": {
        "algebra": """🧮 **ÁLGEBRA AVANÇADA** 

A álgebra é a linguagem universal da matemática! 

🔹 **O que é?**
- Estudo de símbolos e regras para manipular esses símbolos
- Resolução de equações e inequações
- Trabalho com variáveis (x, y, z) e constantes

🔹 **Exemplos práticos:**
```python
# Equação do 1º grau
2x + 5 = 15
2x = 10
x = 5

# Sistema de equações
x + y = 10
x - y = 2
Solução: x=6, y=4


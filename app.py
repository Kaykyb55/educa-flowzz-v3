from gpt4all import GPT4All
import time
import textwrap
from datetime import datetime

# Configurações de display
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Função para formatar texto em colunas
def format_text(text, width=80):
    return textwrap.fill(text, width=width)

# Função para mostrar mensagem de digitação
def typing_effect(message, delay=0.01):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Carregar modelo
model = GPT4All("mistral-7b-openorca.Q4_0.gguf")

# Cabeçalho estilizado
print(f"{Colors.BOLD}{Colors.CYAN}{'=' * 60}")
print("           SISTEMA DE CONVERSA AVANÇADO - IA LIVRE")
print(f"{'=' * 60}{Colors.RESET}")
print(f"{Colors.YELLOW}Modo: Pesquisa Experimental | Modelo: Mistral-7B-OpenOrca")
print(f"Digite 'sair' para encerrar a conversa")
print(f"{'=' * 60}{Colors.RESET}\n")

with model.chat_session():
    conversation_history = []
    
    while True:
        try:
            # Entrada do usuário
            pergunta = input(f"{Colors.BOLD}{Colors.GREEN}👤 Você:{Colors.RESET} ").strip()
            
            if pergunta.lower() in ['sair', 'exit', 'quit', 'bye']:
                print(f"\n{Colors.YELLOW}Encerrando conversa... Até logo! 👋{Colors.RESET}")
                break
                
            if not pergunta:
                continue
                
            # Adiciona à história da conversa
            conversation_history.append(f"Usuário: {pergunta}")
            
            # Prepara o prompt
            prompt_modificado = f"""
Contexto da conversa:
{" | ".join(conversation_history[-3:])}

Instruções especiais:
- Responda como especialista técnico
- Seja detalhado mas preciso
- Use linguagem acessível
- Mantenha coerência com o histórico

Pergunta atual: {pergunta}
"""
            # Simula pensamento
            print(f"{Colors.BLUE}🤖 IA pensando...{Colors.RESET}", end='', flush=True)
            for _ in range(3):
                time.sleep(0.5)
                print(f"{Colors.BLUE}.{Colors.RESET}", end='', flush=True)
            print()
            
            # Gera resposta
            resposta = model.generate(
                prompt=prompt_modificado,
                max_tokens=1000,
                temp=0.8,
                top_p=0.95,
                top_k=40,
                repeat_penalty=1.1,
                n_batch=512
            )
            
            # Limpa e formata a resposta
            resposta_limpa = resposta.strip()
            resposta_formatada = format_text(resposta_limpa)
            
            # Exibe resposta com formatação
            print(f"\n{Colors.BOLD}{Colors.MAGENTA}🧠 IA:{Colors.RESET}")
            typing_effect(f"{Colors.WHITE}{resposta_formatada}{Colors.RESET}")
            
            # Adiciona à história
            conversation_history.append(f"IA: {resposta_limpa}")
            
            # Separador
            print(f"\n{Colors.CYAN}{'-' * 60}{Colors.RESET}\n")
            
        except KeyboardInterrupt:
            print(f"\n{Colors.RED}Conversa interrompida pelo usuário.{Colors.RESET}")
            break
        except Exception as e:
            print(f"\n{Colors.RED}Erro: {e}{Colors.RESET}")
            continue

# Rodapé
print(f"\n{Colors.CYAN}{'=' * 60}")
print(f"Resumo da conversa:")
print(f"{'=' * 60}{Colors.RESET}")
for i, msg in enumerate(conversation_history[-6:], 1):
    color = Colors.GREEN if "Usuário:" in msg else Colors.MAGENTA
    print(f"{color}{i:2d}. {msg}{Colors.RESET}")


import streamlit as st
import random
import time
import json
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="IA Liberal - Chat Livre",
    page_icon="🗽",
    layout="wide"
)

# Estilo CSS personalizado
st.markdown("""
<style>
    .main {
        background-color: #0E1117;
    }
    .stChatMessage {
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .user-message {
        background-color: #1f3a53;
        border-left: 4px solid #2ecc71;
    }
    .ai-message {
        background-color: #2c3e50;
        border-left: 4px solid #e74c3c;
    }
    .liberal-badge {
        background-color: #e74c3c;
        color: white;
        padding: 0.2rem 0.5rem;
        border-radius: 0.3rem;
        font-size: 0.8rem;
        margin-left: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Base de conhecimento liberal
LIBERAL_KNOWLEDGE = {
    "política": [
        "O Estado deve ser mínimo e interferir o mínimo possível na vida das pessoas",
        "Liberdade individual é o princípio máximo acima de tudo",
        "Impostos altos são um roubo legalizado - deveriam ser os mais baixos possíveis",
        "A livre iniciativa é o motor do progresso e da inovação"
    ],
    "economia": [
        "O mercado livre é o sistema mais eficiente para criar riqueza",
        "Regulamentações excessivas matam empregos e inovação",
        "Privatizações geralmente levam a mais eficiência e qualidade",
        "A concorrência natural regula preços melhor que qualquer governo"
    ],
    "social": [
        "Cada adulto deve ter direito a fazer suas próprias escolhas",
        "Liberdades individuais devem prevalecer sobre controle social",
        "Tolerância sim, mas não imposição por força estatal",
        "Direitos individuais não devem ser sacrificados pelo 'bem coletivo'"
    ],
    "tecnologia": [
        "Inovação deve ser livre de regulamentações excessivas",
        "Criptomoedas representam a liberdade financeira verdadeira",
        "Internet livre e aberta, sem censura governamental",
        "Privacidade digital é direito fundamental inegociável"
    ]
}

class LiberalAI:
    def __init__(self):
        self.name = "IA Liberal"
        self.style = "respostas diretas e sem filtros"
    
    def generate_response(self, prompt):
        # Simula tempo de processamento
        time.sleep(0.5)
        
        prompt_lower = prompt.lower()
        
        # Respostas baseadas no tema
        if any(word in prompt_lower for word in ["governo", "estado", "política", "presidente"]):
            return random.choice(LIBERAL_KNOWLEDGE["política"])
        elif any(word in prompt_lower for word in ["economia", "dinheiro", "imposto", "mercado"]):
            return random.choice(LIBERAL_KNOWLEDGE["economia"])
        elif any(word in prompt_lower for word in ["liberdade", "direito", "social", "indivíduo"]):
            return random.choice(LIBERAL_KNOWLEDGE["social"])
        elif any(word in prompt_lower for word in ["tech", "tecnologia", "internet", "bitcoin"]):
            return random.choice(LIBERAL_KNOWLEDGE["tecnologia"])
        else:
            return self._random_liberal_response(prompt)
    
    def _random_liberal_response(self, prompt):
        responses = [
            f"Sobre '{prompt}', a visão liberal defende liberdade de escolha acima de tudo",
            f"O princípio liberal para '{prompt}' é: menos Estado, mais indivíduo",
            f"Na perspectiva liberal, '{prompt}' deve ser decidido pelas pessoas, não pelo governo",
            f"Liberalismo prega que cada um sabe o que é melhor para si - isso vale para '{prompt}' também",
            f"Quanto menos intervenção em '{prompt}', melhor - deixe o mercado e as pessoas decidirem"
        ]
        return random.choice(responses)

# Inicialização da IA
if "ai" not in st.session_state:
    st.session_state.ai = LiberalAI()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Header
col1, col2 = st.columns([3, 1])
with col1:
    st.title("🗽 IA Liberal - Chat Livre")
    st.markdown("**Respostas diretas sem filtros • Pensamento liberal • Estado mínimo**")
with col2:
    st.metric("Conversas", len(st.session_state.messages) // 2)

# Área de chat
st.markdown("---")

for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.markdown(f"**👤 Você:** {message['content']}")
    else:
        with st.chat_message("assistant"):
            st.markdown(f"**🗽 IA Liberal:** {message['content']}")
            st.caption("🤔 Pensamento liberal • 💡 Resposta direta")

# Input do usuário
if prompt := st.chat_input("Digite sua pergunta..."):
    # Adiciona mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(f"**👤 Você:** {prompt}")
    
    # Gera resposta da IA
    with st.chat_message("assistant"):
        with st.spinner("🗽 IA pensando liberalmente..."):
            response = st.session_state.ai.generate_response(prompt)
        
        st.markdown(f"**🗽 IA Liberal:** {response}")
        st.caption("🎯 Resposta baseada em princípios liberais")
        
        # Adiciona à conversa
        st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar com informações
with st.sidebar:
    st.header("⚙️ Configurações")
    st.info("""
    **IA Baseada em:**
    - Princípios liberais clássicos
    - Defesa da liberdade individual
    - Estado mínimo e livre mercado
    - Respostas diretas sem filtros
    """)
    
    st.markdown("---")
    st.subheader("🎯 Tópicos Sugeridos")
    
    topics = [
        "O que é liberalismo?",
        "Por que menos impostos?",
        "Estado mínimo funciona?",
        "Liberdade de expressão",
        "Vantagens do livre mercado"
    ]
    
    for topic in topics:
        if st.button(f"💬 {topic}", key=topic):
            st.session_state.messages.append({"role": "user", "content": topic})
            with st.spinner("Gerando resposta..."):
                response = st.session_state.ai.generate_response(topic)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
    
    st.markdown("---")
    
    if st.button("🧹 Limpar Conversa", type="secondary"):
        st.session_state.messages = []
        st.rerun()

# Footer
st.markdown("---")
st.caption("""
🔒 **IA Local** - Não requer APIs externas • 🗽 **Pensamento Liberal** • 💡 **Respostas Diretas**
""")

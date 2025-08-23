import streamlit as st
import random
import time
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="IA Conversacional - Chat Inteligente",
    page_icon="🤖",
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
        border-left: 4px solid #3498db;
    }
    .ai-badge {
        background-color: #3498db;
        color: white;
        padding: 0.2rem 0.5rem;
        border-radius: 0.3rem;
        font-size: 0.8rem;
        margin-left: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Base de conhecimento geral
KNOWLEDGE_BASE = {
    "ciência": [
        "A teoria da relatividade de Einstein revolucionou nossa compreensão do espaço-tempo",
        "As células são a unidade básica da vida, descobertas por Robert Hooke em 1665",
        "O DNA contém as instruções genéticas para o desenvolvimento de todos os organismos",
        "A fotossíntese é o processo pelo qual plantas convertem luz solar em energia"
    ],
    "tecnologia": [
        "Inteligência Artificial está transformando indústrias em todo o mundo",
        "Blockchain oferece transparência e segurança em transações digitais",
        "Computação quântica promete resolver problemas impossíveis para computadores clássicos",
        "Realidade virtual e aumentada estão mudando a forma como interagimos com o digital"
    ],
    "história": [
        "A Revolução Industrial começou na Inglaterra no século XVIII",
        "A queda do Muro de Berlim em 1989 marcou o fim da Guerra Fria",
        "O Renascimento foi um período de grande avanço cultural e científico na Europa",
        "As Grandes Navegações expandiram o conhecimento geográfico do mundo"
    ],
    "cultura": [
        "A arte expressa emoções e ideias através de diversas formas e técnicas",
        "A literatura permite explorar diferentes realidades e perspectivas humanas",
        "A música é uma linguagem universal que conecta pessoas across culturas",
        "O cinema combina arte, tecnologia e narrativa para contar histórias"
    ],
    "saúde": [
        "Exercícios físicos regulares melhoram a saúde física e mental",
        "Uma dieta balanceada é essencial para o bem-estar geral",
        "O sono adequado é crucial para a recuperação e saúde do cérebro",
        "Meditação e mindfulness podem reduzir stress e ansiedade"
    ],
    "educação": [
        "A aprendizagem contínua é fundamental no mundo moderno",
        "Habilidades digitais são cada vez mais importantes no mercado de trabalho",
        "O pensamento crítico ajuda a analisar informações de forma objetiva",
        "A criatividade pode ser desenvolvida através da prática e experimentação"
    ]
}

class ConversationalAI:
    def __init__(self):
        self.name = "IA Assistente"
        self.style = "respostas úteis e informativas"
    
    def generate_response(self, prompt):
        # Simula tempo de processamento
        time.sleep(0.3)
        
        prompt_lower = prompt.lower()
        
        # Respostas baseadas no tema
        if any(word in prompt_lower for word in ["ciência", "científico", "pesquisa", "física", "química"]):
            return random.choice(KNOWLEDGE_BASE["ciência"])
        elif any(word in prompt_lower for word in ["tech", "tecnologia", "computador", "internet", "digital"]):
            return random.choice(KNOWLEDGE_BASE["tecnologia"])
        elif any(word in prompt_lower for word in ["história", "passado", "antigo", "histórico"]):
            return random.choice(KNOWLEDGE_BASE["história"])
        elif any(word in prompt_lower for word in ["arte", "cultura", "música", "cinema", "literatura"]):
            return random.choice(KNOWLEDGE_BASE["cultura"])
        elif any(word in prompt_lower for word in ["saúde", "exercício", "dieta", "medicina", "bem-estar"]):
            return random.choice(KNOWLEDGE_BASE["saúde"])
        elif any(word in prompt_lower for word in ["educação", "aprender", "estudo", "escola", "universidade"]):
            return random.choice(KNOWLEDGE_BASE["educação"])
        else:
            return self._random_general_response(prompt)
    
    def _random_general_response(self, prompt):
        responses = [
            f"Interessante sua pergunta sobre '{prompt}'. É um tema que envolve várias perspectivas diferentes.",
            f"Sobre '{prompt}', existem diversas abordagens e opiniões na comunidade especializada.",
            f"Ótima questão! '{prompt}' é um tópico que tem sido discutido por muitos especialistas.",
            f"Analisando '{prompt}', posso oferecer algumas informações gerais baseadas no conhecimento atual.",
            f"'{prompt}' é um assunto complexo que pode ser abordado de diferentes ângulos.",
            f"Vamos explorar '{prompt}' juntos. O que específico você gostaria de saber?"
        ]
        return random.choice(responses)

# Inicialização da IA
if "ai" not in st.session_state:
    st.session_state.ai = ConversationalAI()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Header
col1, col2 = st.columns([3, 1])
with col1:
    st.title("🤖 IA Conversacional - Assistente Inteligente")
    st.markdown("**Respostas úteis • Conhecimento geral • Assistência informativa**")
with col2:
    st.metric("Mensagens", len(st.session_state.messages))

# Área de chat
st.markdown("---")

for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.markdown(f"**👤 Você:** {message['content']}")
    else:
        with st.chat_message("assistant"):
            st.markdown(f"**🤖 IA:** {message['content']}")
            st.caption("💡 Informação útil • 🎯 Resposta precisa")

# Input do usuário
if prompt := st.chat_input("Digite sua pergunta ou mensagem..."):
    # Adiciona mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(f"**👤 Você:** {prompt}")
    
    # Gera resposta da IA
    with st.chat_message("assistant"):
        with st.spinner("🤖 IA processando sua pergunta..."):
            response = st.session_state.ai.generate_response(prompt)
        
        st.markdown(f"**🤖 IA:** {response}")
        st.caption("📚 Baseado em conhecimento geral")
        
        # Adiciona à conversa
        st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar com informações
with st.sidebar:
    st.header("⚙️ Sobre a IA")
    st.info("""
    **Assistente Inteligente:**
    - Respostas baseadas em conhecimento geral
    - Informações sobre diversos temas
    - Linguagem natural e acessível
    - Sem viés político ou ideológico
    """)
    
    st.markdown("---")
    st.subheader("🎯 Tópicos Populares")
    
    topics = [
        "Como funciona a inteligência artificial?",
        "Dicas para aprender melhor",
        "Importância do exercício físico",
        "História da internet",
        "Benefícios da leitura"
    ]
    
    for topic in topics:
        if st.button(f"💡 {topic}", key=topic):
            st.session_state.messages.append({"role": "user", "content": topic})
            with st.spinner("Gerando resposta..."):
                response = st.session_state.ai.generate_response(topic)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
    
    st.markdown("---")
    
    if st.button("🧹 Limpar Conversa", type="secondary"):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.caption(f"🕐 Última atualização: {datetime.now().strftime('%H:%M')}")

# Footer
st.markdown("---")
st.caption("""
🔍 **IA de Conhecimento Geral** • 🤖 **Assistente Conversacional** • 💡 **Respostas Informativas**
• Desenvolvido para ajudar e informar
""")

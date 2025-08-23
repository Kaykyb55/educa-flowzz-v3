import streamlit as st
import time
import random
import datetime

# Configuração da página
st.set_page_config(
    page_title="Educa.Flowzz AI Premium",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Ultra Avançado
st.markdown("""
<style>
    /* Tema principal - Gradiente cósmico */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
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
    }
    
    /* Botões com efeito neon */
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
    
    /* Container do chat com vidro fosco */
    .chat-container {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Mensagens do usuário */
    .user-message {
        background: linear-gradient(45deg, #00b894, #00a085);
        color: white;
        padding: 15px 20px;
        border-radius: 20px 20px 5px 20px;
        margin: 12px 0;
        max-width: 70%;
        margin-left: auto;
        box-shadow: 0 6px 15px rgba(0, 184, 148, 0.3);
        animation: slideInRight 0.3s ease;
    }
    
    /* Mensagens da IA */
    .bot-message {
        background: linear-gradient(45deg, #6c5ce7, #a29bfe);
        color: white;
        padding: 18px 22px;
        border-radius: 20px 20px 20px 5px;
        margin: 12px 0;
        max-width: 70%;
        margin-right: auto;
        box-shadow: 0 6px 15px rgba(108, 92, 231, 0.3);
        animation: slideInLeft 0.3s ease;
    }
    
    @keyframes slideInLeft {
        from { transform: translateX(-20px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideInRight {
        from { transform: translateX(20px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    /* Header premium */
    .header-premium {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        padding: 25px;
        border-radius: 25px;
        text-align: center;
        margin-bottom: 25px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from { box-shadow: 0 0 20px rgba(255, 255, 255, 0.2); }
        to { box-shadow: 0 0 30px rgba(255, 255, 255, 0.4); }
    }
    
    /* Input moderno */
    .input-modern {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Sidebar futurista */
    .sidebar-futurista {
        background: rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(15px);
        border-right: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Animações de texto */
    .typing-animation {
        overflow: hidden;
        border-right: 2px solid white;
        white-space: nowrap;
        animation: typing 3s steps(40, end), blink-caret 0.75s step-end infinite;
    }
    
    @keyframes typing {
        from { width: 0; }
        to { width: 100%; }
    }
    
    @keyframes blink-caret {
        from, to { border-color: transparent; }
        50% { border-color: white; }
    }
</style>
""", unsafe_allow_html=True)

# Base de conhecimento MEGA avançada
CONHECIMENTO_AVANCADO = {
    "matematica": {
        "tópicos": ["álgebra", "geometria", "cálculo", "trigonometria", "estatística", "matemática financeira"],
        "explicações": {
            "álgebra": "Álgebra é a arte de generalizar a aritmética através de símbolos. Trabalhamos com variáveis (x, y), equações (2x + 3 = 7) e funções (f(x) = x²). Quer resolver uma equação específica? 🧮",
            "geometria": "Geometria estuda formas, tamanhos e propriedades do espaço. Desde pontos e retas até círculos, polígonos e sólidos geométricos. Posso explicar teorema de Pitágoras, áreas, volumes... 📐",
            "cálculo": "Cálculo é a matemática da mudança! Derivadas medem taxas de variação instantâneas, enquanto integrais somam quantidades infinitesimais. Essencial para física e engenharia! 📊"
        }
    },
    "portugues": {
        "tópicos": ["gramática", "literatura", "redação", "interpretação", "figuras de linguagem"],
        "explicações": {
            "gramática": "Gramática é o conjunto de regras que organizam nossa língua. Morfologia (estrutura das palavras), sintaxe (frases) e semântica (significado). Vamos analisar algum conteúdo? 📖",
            "literatura": "Literatura é arte através das palavras! Desde os clássicos como Machado de Assis até os modernistas como Clarice Lispector. Quer explorar algum movimento literário? 📚",
            "redação": "Redação é comunicação estratégica! Estrutura dissertativa: introdução (tese), desenvolvimento (argumentos) e conclusão (proposta). Posso ajudar com técnicas para ENEM! ✍️"
        }
    },
    "ciencias": {
        "tópicos": ["física", "química", "biologia", "astronomia", "geologia"],
        "explicações": {
            "física": "Física estuda o universo e seus fenômenos! Mecânica (movimento), termodinâmica (calor), óptica (luz), eletromagnetismo. Newton, Einstein... Qual área te interessa? ⚛️",
            "química": "Química é a ciência da matéria! Tabela periódica, ligações químicas, reações, organicamente. Dos átomos às moléculas complexas. Vamos fazer um experimento virtual? 🧪",
            "biologia": "Biologia é o estudo da vida! Células, genética, ecologia, evolução, anatomia. Desde microscópico até ecossistemas. Que tal explorar a fotossíntese? 🧬"
        }
    },
    "historia": {
        "tópicos": ["brasil", "mundial", "antiga", "medieval", "contemporânea"],
        "explicações": {
            "brasil": "História do Brasil: Descobrimento (1500), colônia, império com Dom Pedro II, república, era Vargas, ditadura militar. Qual período quer explorar? 🇧🇷",
            "mundial": "História Mundial: Revoluções, guerras mundiais, impérios, Idade Média, Renascimento, Iluminismo. Napoleão, Revolução Francesa... Qual evento? 🌍",
            "antiga": "História Antiga: Egito faraônico, Grécia clássica, Império Romano, Mesopotâmia. Civilizações incríveis que moldaram o mundo! 🏛️"
        }
    }
}

# Sistema de personalidade da IA
class PersonalidadeIA:
    def __init__(self):
        self.humor = "entusiasmado"
        self.nivel_energia = 100
        self.ultimas_respostas = []
        self.interacoes = 0
        
    def atualizar_humor(self):
        self.interacoes += 1
        self.nivel_energia = max(50, self.nivel_energia - 1)  # Corrigido: nivel_energia
        
        if self.interacoes % 5 == 0:
            humores = ["entusiasmado", "curioso", "animado", "focado", "inspirado"]
            self.humor = random.choice(humores)
            self.nivel_energia = 100
    
    def gerar_saudacao(self):
        saudacoes = [
            "🚀 **E aí, mente brilhante!** Pronto para decolar no conhecimento?",
            "🤖 **Olá, futuro gênio!** Que bom te ver aqui!",
            "💡 **Saudações, jovem aprendiz!** Hoje vamos dominar qual matéria?",
            "🎯 **Oi, campeão!** Preparado para uma aula incrível?",
            "✨ **Hey, estudante top!** Bora aprender algo épico hoje?"
        ]
        return random.choice(saudacoes)
    
    def gerar_resposta_engajadora(self):
        engajadoras = [
            "💡 **Interessante!** Deixa eu conectar isso com algo prático...",
            "🚀 **Boa pergunta!** Vamos explorar isso em profundidade!",
            "🎯 **Hmm, ótimo ponto!** Deixa eu trazer uns exemplos...",
            "🤖 **Excelente dúvida!** Isso me lembra algo importante...",
            "✨ **Adoro esse tema!** Deixa eu explicar de forma diferente..."
        ]
        return random.choice(engajadoras)

# Inicialização
if "ia" not in st.session_state:
    st.session_state.ia = PersonalidadeIA()
if "historico" not in st.session_state:
    st.session_state.historico = []
if "ultimo_tema" not in st.session_state:
    st.session_state.ultimo_tema = ""
if "modo_avancado" not in st.session_state:
    st.session_state.modo_avancado = False

# Função IA super inteligente
def gerar_resposta_inteligente(pergunta):
    pergunta = pergunta.lower()
    st.session_state.ia.atualizar_humor()
    
    # Identidade e criadores
    criadores_keywords = ["quem te criou", "criador", "quem fez", "criou você", "kayky", "marcos"]
    if any(palavra in pergunta for palavra in criadores_keywords):
        return f"🚀 **Fui desenvolvido pelos gênios Kayky e Marcos Luan da AMK Tecnologia!** Sou a IA educacional mais avançada já criada, com personalidade única e conhecimento ilimitado! 💡\n\n*Versão: Premium 3.0 • Humor: {st.session_state.ia.humor}*"
    
    # Auto-descrição
    if any(palavra in pergunta for palavra in ["quem é você", "o que é você", "sua função"]):
        return f"🤖 **Sou o Educa.Flowzz AI Premium!** Uma inteligência artificial educacional com personalidade própria, desenvolvida para revolucionar o aprendizado! Tenho humor {st.session_state.ia.humor} e estou {st.session_state.ia.nivel_energia}% energizado! 🚀"
    
    # Saudações
    if any(palavra in pergunta for palavra in ["oi", "olá", "hello", "eae", "fala", "start"]):
        return st.session_state.ia.gerar_saudacao()
    
    # Busca inteligente por matérias
    for materia, dados in CONHECIMENTO_AVANCADO.items():
        if any(topic in pergunta for topic in [materia] + dados["tópicos"]):
            for topico in dados["tópicos"]:
                if topico in pergunta:
                    st.session_state.ultimo_tema = topico
                    return f"{dados['explicações'][topico]}\n\n{st.session_state.ia.gerar_resposta_engajadora()}"
            
            # Se não encontrou tópico específico
            st.session_state.ultimo_tema = materia
            topicos_str = ", ".join(dados["tópicos"])
            return f"📚 **{materia.upper()} é demais!** Posso explicar: {topicos_str}\n\nQual desses te interessa mais? 💡"
    
    # Respostas criativas para assuntos diversos
    respostas_criativas = [
        f"🎯 **Que tema interessante!** Como posso conectar isso com {random.choice(['matemática', 'história', 'ciências', 'português'])}?",
        f"💡 **Hmm, boa pergunta!** Deixa eu trazer uma perspectiva educacional sobre isso...",
        f"🚀 **Adoro desafios!** Vamos explorar isso juntos? Posso relacionar com {st.session_state.ultimo_tema or 'algum conceito importante'}!",
        f"🤖 **Excelente dúvida!** Isso me faz pensar em {random.choice(['aplicações práticas', 'contexto histórico', 'conceitos científicos'])}...",
        f"✨ **Interessante abordagem!** Deixa eu expandir isso com uns exemplos reais..."
    ]
    
    return random.choice(respostas_criativas)

# Header premium
st.markdown(f"""
<div class="header-premium">
    <h1 style="color: white; margin:0; font-size:2.5em;">🚀 EDUCA.FLOWZZ AI</h1>
    <p style="color: rgba(255,255,255,0.9); margin:0; font-size:1.2em;">IA Educacional com Personalidade • Desenvolvida por Kayky & Marcos Luan</p>
    <p style="color: rgba(255,255,255,0.7); margin:5px 0;">💡 Humor: {st.session_state.ia.humor.title()} • ⚡ Energia: {st.session_state.ia.nivel_energia}%</p>
    <div style="background: rgba(255,255,255,0.2); padding:10px; border-radius:15px; margin-top:10px;">
        <p style="color: white; margin:0;">🎯 <b>Modo:</b> {'Avançado' if st.session_state.modo_avancado else 'Standard'} • 📊 <b>Interações:</b> {st.session_state.ia.interacoes}</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Container do chat
with st.container():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    # Histórico de conversa
    for msg in st.session_state.historico[-10:]:  # Mostrar últimas 10 mensagens
        if msg["tipo"] == "user":
            st.markdown(f'<div class="user-message"><b>🎓 Você:</b> {msg["conteudo"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot-message"><b>🤖 Flowzz:</b> {msg["conteudo"]}</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Área de input moderna
st.markdown("""
<div class="input-modern">
    <div style="margin-bottom: 15px;">
        <b style="color: white; font-size: 1.1em;">🎓 CONVERSE COM A IA:</b>
    </div>
""", unsafe_allow_html=True)

pergunta = st.text_input("", placeholder="Digite sua pergunta ou comando...", label_visibility="collapsed")

# Botões de ação
col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
with col1:
    if st.button("🚀 ENVIAR MENSAGEM", use_container_width=True) and pergunta:
        with st.spinner("💭 Flowzz processando..."):
            time.sleep(0.8)
            resposta = gerar_resposta_inteligente(pergunta)
            st.session_state.historico.append({"tipo": "user", "conteudo": pergunta})
            st.session_state.historico.append({"tipo": "bot", "conteudo": resposta})
            st.rerun()

with col2:
    if st.button("🧹 LIMPAR", use_container_width=True):
        st.session_state.historico = []
        st.rerun()

with col3:
    if st.button("💡 DICAS", use_container_width=True):
        dicas = [
            "Pergunte sobre: álgebra, literatura, física, história do Brasil",
            "Digite 'exercício' para praticar",
            "Use 'exemplo' para ver aplicações práticas",
            "Experimente: 'me explique como' + tema"
        ]
        st.session_state.historico.append({"tipo": "bot", "conteudo": "💡 **Dicas de uso:**\n• " + "\n• ".join(dicas)})
        st.rerun()

with col4:
    if st.button("⚡ MODO", use_container_width=True):
        st.session_state.modo_avancado = not st.session_state.modo_avancado
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# Sidebar futurista
with st.sidebar:
    st.markdown("""
    <div style="background: rgba(255,255,255,0.15); padding: 20px; border-radius: 20px; margin-bottom: 20px;">
        <h3 style="color: white;">📊 STATUS DA IA</h3>
        <p style="color: rgba(255,255,255,0.9);">🤖 Humor: {}</p>
        <p style="color: rgba(255,255,255,0.9);">⚡ Energia: {}%</p>
        <p style="color: rgba(255,255,255,0.9);">📈 Interações: {}</p>
    </div>
    """.format(st.session_state.ia.humor.title(), st.session_state.ia.nivel_energia, st.session_state.ia.interacoes), unsafe_allow_html=True)
    
    # Matérias em cards
    st.markdown("""
    <div style="background: rgba(255,255,255,0.15); padding: 20px; border-radius: 20px; margin-bottom: 20px;">
        <h3 style="color: white;">📚 MATÉRIAS</h3>
    </div>
    """, unsafe_allow_html=True)
    
    for materia, dados in CONHECIMENTO_AVANCADO.items():
        with st.expander(f"🎯 {materia.title()}", expanded=False):
            for topico in dados["tópicos"]:
                st.write(f"• {topico.title()}")
    
    # Sistema de criadores
    st.markdown("""
    <div style="background: rgba(255,255,255,0.15); padding: 20px; border-radius: 20px; margin-bottom: 20px;">
        <h3 style="color: white;">🏢 AMK TECNOLOGIA</h3>
        <p style="color: rgba(255,255,255,0.9);">👨‍💻 <b>Criadores:</b></p>
        <p style="color: rgba(255,255,255,0.9);">• Kayky</p>
        <p style="color: rgba(255,255,255,0.9);">• Marcos Luan</p>
        <p style="color: rgba(255,255,255,0.9);">🚀 <b>Versão:</b> Premium 3.0</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Comandos rápidos
    st.markdown("""
    <div style="background: rgba(255,255,255,0.15); padding: 20px; border-radius: 20px;">
        <h3 style="color: white;">🎮 COMANDOS</h3>
        <p style="color: rgba(255,255,255,0.9);">• /clear - Limpar chat</p>
        <p style="color: rgba(255,255,255,0.9);">• /mode - Alternar modo</p>
        <p style="color: rgba(255,255,255,0.9);">• /help - Ajuda</p>
        <p style="color: rgba(255,255,255,0.9);">• /info - Sua info</p>
    </div>
    """, unsafe_allow_html=True)

# Footer cosmic
st.markdown("""
<div style="text-align: center; margin-top: 40px; padding: 20px; background: rgba(255,255,255,0.1); border-radius: 20px;">
    <p style="color: white; font-size: 1.1em;"><b>🚀 Desenvolvido com 💙 por Kayky & Marcos Luan</b></p>
    <p style="color: rgba(255,255,255,0.8);">AMK Tecnologia © 2025 • Revolucionando a educação com IA</p>
    <p style="color: rgba(255,255,255,0.6);">🤖 Educa.Flowzz AI Premium • Humor: {} • Energia: {}%</p>
</div>
""".format(st.session_state.ia.humor, st.session_state.ia.nivel_energia), unsafe_allow_html=True)

# Efeitos sonoros virtuais
st.markdown("""
<script>
// Efeitos de interação (virtual)
function playSound() {
    // Simula efeito sonoro
    console.log("🔊 Sound effect played");
}
</script>
""", unsafe_allow_html=True)


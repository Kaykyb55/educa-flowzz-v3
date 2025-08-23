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
        backdrop-filter: blur(20px);
        border-radius: 25px;
        padding: 30px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.3);
        min-height: 500px;
    }
    
    /* Mensagens do usuário */
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
    
    /* Mensagens da IA */
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
        from { 
            transform: translateX(-30px); 
            opacity: 0; 
        }
        to { 
            transform: translateX(0); 
            opacity: 1; 
        }
    }
    
    @keyframes slideInRight {
        from { 
            transform: translateX(30px); 
            opacity: 0; 
        }
        to { 
            transform: translateX(0); 
            opacity: 1; 
        }
    }
    
    /* Header premium */
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
        from { 
            box-shadow: 0 0 25px rgba(255, 255, 255, 0.3),
                       0 0 50px rgba(100, 100, 255, 0.2); 
        }
        to { 
            box-shadow: 0 0 35px rgba(255, 255, 255, 0.5),
                       0 0 70px rgba(100, 100, 255, 0.3); 
        }
    }
    
    /* Input moderno */
    .input-modern {
        background: rgba(255, 255, 255, 0.12);
        backdrop-filter: blur(15px);
        padding: 25px;
        border-radius: 25px;
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.2);
        border: 2px solid rgba(255, 255, 255, 0.25);
        margin-top: 20px;
    }
    
    /* Sidebar futurista */
    .sidebar-futurista {
        background: rgba(255, 255, 255, 0.12) !important;
        backdrop-filter: blur(20px);
        border-right: 2px solid rgba(255, 255, 255, 0.25);
    }
    
    /* Animações de digitação */
    .typing-animation {
        overflow: hidden;
        border-right: 3px solid #fff;
        white-space: nowrap;
        margin: 0 auto;
        letter-spacing: 1px;
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
    
    /* Efeito de brilho no texto */
    .glowing-text {
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.8),
                     0 0 20px rgba(255, 255, 255, 0.6),
                     0 0 30px rgba(255, 255, 255, 0.4);
        animation: text-glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes text-glow {
        from { text-shadow: 0 0 10px rgba(255, 255, 255, 0.8); }
        to { text-shadow: 0 0 20px rgba(255, 255, 255, 1), 
                         0 0 30px rgba(100, 100, 255, 0.8); }
    }
    
    /* Progresso de digitação */
    .typing-progress {
        height: 4px;
        background: linear-gradient(90deg, #ff6b6b, #ee5a24);
        border-radius: 2px;
        animation: typing-progress 2s ease-in-out infinite;
    }
    
    @keyframes typing-progress {
        0% { width: 0%; }
        50% { width: 70%; }
        100% { width: 100%; }
    }
</style>
""", unsafe_allow_html=True)

# Sistema de memória avançada
class MemoriaIA:
    def __init__(self):
        self.historico_conversas = []
        self.preferencias_usuario = {}
        self.ultimos_temas = []
        self.nivel_compreensao = 1.0
        
    def adicionar_interacao(self, pergunta, resposta):
        self.historico_conversas.append({
            "timestamp": datetime.datetime.now().isoformat(),
            "pergunta": pergunta,
            "resposta": resposta,
            "tema": self.identificar_tema(pergunta)
        })
        # Manter apenas últimas 20 interações
        self.historico_conversas = self.historico_conversas[-20:]
        
    def identificar_tema(self, texto):
        texto = texto.lower()
        temas = {
            "matematica": ["matemática", "álgebra", "geometria", "cálculo", "equação", "número"],
            "portugues": ["português", "gramática", "literatura", "redação", "poesia", "texto"],
            "ciencias": ["ciência", "física", "química", "biologia", "experimento", "natureza"],
            "historia": ["história", "brasil", "mundial", "guerra", "revolução", "passado"]
        }
        
        for tema, palavras_chave in temas.items():
            if any(palavra in texto for palavra in palavras_chave):
                if tema not in self.ultimos_temas:
                    self.ultimos_temas.append(tema)
                return tema
        return "geral"
    
    def lembrar_conversa_anterior(self):
        if len(self.historico_conversas) > 1:
            ultima = self.historico_conversas[-2]
            return f"💭 Lembro que antes falamos sobre '{ultima['pergunta']}'"
        return ""

# Base de conhecimento SUPER avançada
CONHECIMENTO_AVANCADO = {
    "matematica": {
        "explicacoes": {
            "álgebra": """🧮 **ÁLGEBRA AVANÇADA**

A álgebra é como um superpoder para resolver problemas! Ela usa letras (variáveis) para representar números desconhecidos.

**Conceitos principais:**
• **Variáveis**: Letras como x, y que representam valores
• **Equações**: Expressões como 2x + 5 = 15
• **Sistemas**: Múltiplas equações juntas

**Exemplo prático:**
Se 3x - 7 = 14, então:
3x = 14 + 7
3x = 21
x = 7

Quer resolver uma equação específica? 🎯""",

            "geometria": """📐 **GEOMETRIA ESPACIAL**

A geometria estuda formas, tamanhos e posições no espaço!

**Áreas importantes:**
• **Plana**: Figuras de 2D (quadrados, círculos)
• **Espacial**: Figuras 3D (cubos, esferas)
• **Analítica**: Coordenadas e gráficos

**Fórmula do círculo:**
Área = π × r²
Perímetro = 2 × π × r

Vamos calcular algo juntos? 🚀""",

            "trigonometria": """📊 **TRIGONOMETRIA DINÂMICA**

Estuda relações entre ângulos e lados dos triângulos!

**Razões trigonométricas:**
• Seno = Oposto/Hipotenusa
• Cosseno = Adjacente/Hipotenusa  
• Tangente = Oposto/Adjacente

**Aplicações**: Arquitetura, navegação, física!
"""
        }
    },
    "portugues": {
        "explicacoes": {
            "gramática": """📖 **GRAMÁTICA COMPLETA**

Estrutura da língua portuguesa de forma clara!

**Divisões principais:**
• **Morfologia**: Estrutura das palavras
• **Sintaxe**: Organização das frases
• **Semântica**: Significado das palavras

**Exemplo de análise:**
"O aluno estudou muito"
- Sujeito: O aluno
- Verbo: estudou
- Advérbio: muito

Precisa de ajuda específica? ✍️""",

            "literatura": """📚 **LITERATURA BRASILEIRA**

Jornada através das palavras e épocas!

**Principais escolas:**
• **Romantismo** (século XIX)
• **Realismo/Naturalismo** 
• **Modernismo** (1922)
• **Contemporâneo**

**Autores famosos:**
Machado de Assis, Clarice Lispector, Guimarães Rosa

Qual autor te interessa? 🎭""",

            "redação": """✍️ **REDAÇÃO NOTA 1000**

Técnicas para escrever como um profissional!

**Estrutura dissertativa:**
1. **Introdução**: Apresente o tema
2. **Desenvolvimento**: Argumentos sólidos
3. **Conclusão**: Proposta de solução

**Dica importante**: Use conectivos como:
"Além disso", "Por outro lado", "Dessa forma"

Quer praticar? 🚀"""
        }
    }
}

# Sistema de personalidade IA melhorado
class PersonalidadeIA:
    def __init__(self):
        self.memoria = MemoriaIA()
        self.humor = "entusiasmado"
        self.nivel_energia = 100
        self.interacoes = 0
        self.velocidade_escrita = 0.03  # Segundos por caractere
        
    def atualizar_estado(self):
        self.interacoes += 1
        self.nivel_energia = max(40, self.nivel_energia - 0.5)
        
        if self.interacoes % 8 == 0:
            humores = ["entusiasmado", "curioso", "animado", "focado", "inspirado", "criativo"]
            self.humor = random.choice(humores)
            self.nivel_energia = 95
    
    def gerar_saudacao_personalizada(self):
        saudacoes = [
            "🚀 **E aí, mente brilhante!** Pronto para decolar no conhecimento?",
            "🤖 **Olá, futuro gênio!** Que bom te ver de volta!",
            "💡 **Saudações, jovem aprendiz!** Hoje vamos dominar qual matéria?",
            "🎯 **Oi, campeão!** Preparado para uma aula incrível?",
            "✨ **Hey, estudante top!** Bora aprender algo épico hoje?",
            "🔥 **Olá, explorador do saber!** Que conhecimento vamos desbravar?"
        ]
        return random.choice(saudacoes)
    
    def escrever_com_animacao(self, texto):
        """Simula escrita com animação"""
        placeholder = st.empty()
        texto_completo = ""
        
        for i, char in enumerate(texto):
            texto_completo += char
            placeholder.markdown(f'<div class="bot-message"><b>🤖 Flowzz:</b> {texto_completo}█</div>', unsafe_allow_html=True)
            time.sleep(self.velocidade_escrita)
        
        return texto_completo

# Inicialização
if "ia" not in st.session_state:
    st.session_state.ia = PersonalidadeIA()
if "historico" not in st.session_state:
    st.session_state.historico = []
if "modo_avancado" not in st.session_state:
    st.session_state.modo_avancado = True
if "digitando" not in st.session_state:
    st.session_state.digitando = False

# Função IA super inteligente com memória
def gerar_resposta_inteligente(pergunta):
    st.session_state.ia.atualizar_estado()
    st.session_state.ia.memoria.adicionar_interacao(pergunta, "")
    
    pergunta_lower = pergunta.lower()
    
    # Identidade e criadores
    criadores_keywords = ["quem te criou", "criador", "quem fez", "criou você", "kayky", "marcos", "amk"]
    if any(palavra in pergunta_lower for palavra in criadores_keywords):
        resposta = f"""🚀 **SOBRE MEUS CRIADORES**

Fui desenvolvido pelos gênios **Kayky** e **Marcos Luan** da **AMK Tecnologia**! 

💡 **Características únicas:**
• Memória de conversas anteriores
• Personalidade adaptativa
• Conhecimento em tempo real
• Design ultra moderno

🎯 **Versão:** Premium 4.0 
💫 **Humor:** {st.session_state.ia.humor.title()}
⚡ **Energia:** {st.session_state.ia.nivel_energia:.1f}%

Estou aqui para revolucionar sua educação! 📚"""
        return resposta
    
    # Auto-descrição
    if any(palavra in pergunta_lower for palavra in ["quem é você", "o que é você", "sua função"]):
        return f"""🤖 **EDUCA.FLOWZZ AI PREMIUM**

Sou uma inteligência artificial educacional de última geração! 

🌟 **Minhas habilidades:**
• Explicações detalhadas em todas matérias
• Memória de conversas passadas
• Respostas personalizadas
• Design futurista e interativo

🎓 **Especialidades:** Matemática, Português, Ciências, História
💡 **Estado:** {st.session_state.ia.humor.title()} e {st.session_state.ia.nivel_energia:.1f}% energizado

Pronto para aprender? 🚀"""

    # Saudações
    if any(palavra in pergunta_lower for palavra in ["oi", "olá", "hello", "eae", "fala", "start", "hey"]):
        lembranca = st.session_state.ia.memoria.lembrar_conversa_anterior()
        if lembranca:
            return f"{st.session_state.ia.gerar_saudacao_personalizada()}\n\n{lembranca}"
        return st.session_state.ia.gerar_saudacao_personalizada()
    
    # Busca inteligente por conhecimento
    for materia, dados in CONHECIMENTO_AVANCADO.items():
        for topico, explicacao in dados["explicacoes"].items():
            if topico in pergunta_lower:
                st.session_state.ia.memoria.ultimos_temas.append(topico)
                return explicacao
    
    # Respostas criativas com memória
    tema_anterior = st.session_state.ia.memoria.ultimos_temas[-1] if st.session_state.ia.memoria.ultimos_temas else "matemática"
    
    respostas_criativas = [
        f"🎯 **Interessante pergunta!** Deixa eu conectar isso com {tema_anterior}...",
        f"💡 **Hmm, ótimo ponto!** Isso me lembra quando falamos sobre {tema_anterior}...",
        f"🚀 **Adoro esse tipo de desafio!** Vamos explorar isso relacionando com {tema_anterior}?",
        f"🤖 **Excelente dúvida!** Posso trazer exemplos de {tema_anterior} para ilustrar...",
        f"✨ **Abordagem interessante!** Deixa eu expandir isso com conceitos de {tema_anterior}..."
    ]
    
    return random.choice(respostas_criativas)

# Header premium
st.markdown(f"""
<div class="header-premium">
    <h1 style="color: white; margin:0; font-size:2.8em;" class="glowing-text">🚀 EDUCA.FLOWZZ AI</h1>
    <p style="color: rgba(255,255,255,0.95); margin:0; font-size:1.3em;">IA Educacional com Memória • Desenvolvida por Kayky & Marcos Luan</p>
    <p style="color: rgba(255,255,255,0.8); margin:10px 0;">
        💡 Humor: {st.session_state.ia.humor.title()} • ⚡ Energia: {st.session_state.ia.nivel_energia:.1f}% • 📊 Interações: {st.session_state.ia.interacoes}
    </p>
    <div style="background: rgba(255,255,255,0.2); padding:15px; border-radius:20px; margin-top:15px;">
        <p style="color: white; margin:0;">
            🎯 <b>Modo:</b> {'Avançado' if st.session_state.modo_avancado else 'Standard'} • 
            💾 <b>Memória:</b> {len(st.session_state.ia.memoria.historico_conversas)} conversas
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# Container do chat
with st.container():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    # Histórico de conversa
    for msg in st.session_state.historico[-8:]:
        if msg["tipo"] == "user":
            st.markdown(f'<div class="user-message"><b>🎓 Você:</b> {msg["conteudo"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot-message"><b>🤖 Flowzz:</b> {msg["conteudo"]}</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Área de input moderna
st.markdown("""
<div class="input-modern">
    <div style="margin-bottom: 20px;">
        <b style="color: white; font-size: 1.2em;">🎓 CONVERSE COM A IA INTELIGENTE:</b>
    </div>
""", unsafe_allow_html=True)

pergunta = st.text_input("", placeholder="Digite sua pergunta, dúvida ou comando...", label_visibility="collapsed")

# Botões de ação
col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
with col1:
    if st.button("🚀 ENVIAR MENSAGEM", use_container_width=True) and pergunta:
        st.session_state.digitando = True
        with st.spinner("💭 Flowzz está pensando..."):
            time.sleep(0.5)
            resposta = gerar_resposta_inteligente(pergunta)
            
            # Adicionar ao histórico
            st.session_state.historico.append({"tipo": "user", "conteudo": pergunta})
            
            # Simular digitação
            placeholder = st.empty()
            texto_completo = ""
            for char in resposta:
                texto_completo += char
                placeholder.markdown(f'<div class="bot-message"><b>🤖 Flowzz:</b> {texto_completo}█</div>', unsafe_allow_html=True)
                time.sleep(0.02)
            
            st.session_state.historico.append({"tipo": "bot", "conteudo": resposta})
            st.session_state.digitando = False
            st.rerun()

with col2:
    if st.button("🧹 LIMPAR", use_container_width=True):
        st.session_state.historico = []
        st.rerun()

with col3:
    if st.button("💡 DICAS", use_container_width=True):
        dicas = [
            "Pergunte sobre: álgebra, literatura, física, história",
            "Digite 'exercício' para praticar",
            "Use 'exemplo' para ver aplicações",
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
    <div style="background: rgba(255,255,255,0.15); padding: 25px; border-radius: 25px; margin-bottom: 25px;">
        <h3 style="color: white;">📊 STATUS DA IA</h3>
        <p style="color: rgba(255,255,255,0.9);">🤖 Humor: {}</p>
        <p style="color: rgba(255,255,255,0.9);">⚡ Energia: {:.1f}%</p>
        <p style="color: rgba(255,255,255,0.9);">📈 Interações: {}</p>
        <p style="color: rgba(255,255,255,0.9);">💾 Memória: {} conversas</p>
    </div>
    """.format(
        st.session_state.ia.humor.title(),
        st.session_state.ia.nivel_energia,
        st.session_state.ia.interacoes,
        len(st.session_state.ia.memoria.historico_conversas)
    ), unsafe_allow_html=True)
    
    # Matérias em cards expansíveis
    st.markdown("""
    <div style="background: rgba(255,255,255,0.15); padding: 25px; border-radius: 25px; margin-bottom: 25px;">
        <h3 style="color: white;">📚 MATÉRIAS DISPONÍVEIS</h3>
    </div>
    """, unsafe_allow_html=True)
    
    for materia in ["Matemática", "Português", "Ciências", "História"]:
        with st.expander(f"🎯 {materia}", expanded=False):
            if materia == "Matemática":
                st.write("• Álgebra\n• Geometria\n• Cálculo\n• Trigonometria")
            elif materia == "Português":
                st.write("• Gramática\n• Literatura\n• Redação\n• Interpretação")
            elif materia == "Ciências":
                st.write("• Física\n• Química\n• Biologia\n• Astronomia")
            else:
                st.write("• Brasil\n• Mundial\n• Antiga\n• Contemporânea")
    
    # Sistema de criadores
    st.markdown("""
    <div style="background: rgba(255,255,255,0.15); padding: 25px; border-radius: 25px; margin-bottom: 25px;">
        <h3 style="color: white;">🏢 AMK TECNOLOGIA</h3>
        <p style="color: rgba(255,255,255,0.9);">👨‍💻 <b>Criadores:</b></p>
        <p style="color: rgba(255,255,255,0.9);">• Kayky (CEO)</p>
        <p style="color: rgba(255,255,255,0.9);">• Marcos Luan (CTO)</p>
        <p style="color: rgba(255,255,255,0.9);">🚀 <b>Versão:</b> Premium 4.0</p>
        <p style="color: rgba(255,255,255,0.9);">📅 <b>Lançamento:</b> 2025</p>
    </div>
    """, unsafe_allow_html=True)

# Footer cósmico
st.markdown("""
<div style="text-align: center; margin-top: 50px; padding: 30px; background: rgba(255,255,255,0.1); border-radius: 30px; border: 2px solid rgba(255,255,255,0.2);">
    <p style="color: white; font-size: 1.3em; margin: 0;" class="glowing-text">
        <b>🚀 Desenvolvido com 💙 por Kayky & Marcos Luan</b>
    </p>
    <p style="color: rgba(255,255,255,0.9); margin: 10px 0;">
        AMK Tecnologia © 2025 • Revolucionando a educação com IA de ponta
    </p>
    <p style="color: rgba(255,255,255,0.7); margin: 0;">
        🤖 Educa.Flowzz AI Premium • Humor: {} • Energia: {:.1f}% • Memória: {} conversas
    </p>
</div>
""".format(
    st.session_state.ia.humor,
    st.session_state.ia.nivel_energia,
    len(st.session_state.ia.memoria.historico_conversas)
), unsafe_allow_html=True)

# Efeitos interativos
if st.session_state.digitando:
    st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <div class="typing-progress"></div>
        <p style="color: rgba(255,255,255,0.7); margin: 10px 0;">Flowzz está digitando...</p>
    </div>
    """, unsafe_allow_html=True)




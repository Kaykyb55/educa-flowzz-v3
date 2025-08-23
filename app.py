import streamlit as st
import time
import random

# Configuração da página
st.set_page_config(
    page_title="Educa.Flowzz Premium - AMK",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado AMK
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .stButton>button {
        background: linear-gradient(45deg, #1E40AF, #3B82F6);
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 10px;
        font-weight: bold;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    
    .chat-container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        backdrop-filter: blur(10px);
    }
    
    .user-message {
        background: linear-gradient(45deg, #10B981, #34D399);
        color: white;
        padding: 12px 18px;
        border-radius: 15px 15px 5px 15px;
        margin: 10px 0;
        max-width: 80%;
        margin-left: auto;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    
    .bot-message {
        background: linear-gradient(45deg, #3B82F6, #60A5FA);
        color: white;
        padding: 15px 20px;
        border-radius: 15px 15px 15px 5px;
        margin: 10px 0;
        max-width: 80%;
        margin-right: auto;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    
    .header-amk {
        background: rgba(255, 255, 255, 0.95);
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        text-align: center;
        margin-bottom: 20px;
    }
    
    .input-box {
        background: rgba(255, 255, 255, 0.9);
        padding: 15px;
        border-radius: 15px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Cabeçalho premium
st.markdown("""
<div class="header-amk">
    <h1 style="color: #1E40AF; margin:0;">🚀 EDUCA.FLOWZZ PREMIUM</h1>
    <p style="color: #F59E0B; margin:0; font-size:20px;"><b>IA EDUCACIONAL DE ALTA PERFORMANCE</b></p>
    <p style="color: #666; margin:0;">Desenvolvido por <b>Kayky</b> & <b>Marcos Luan</b> - AMK Tecnologia</p>
</div>
""", unsafe_allow_html=True)

# Sistema de conhecimento avançado
conhecimento = {
    "matematica": {
        "álgebra": "📐 **Álgebra**: É o ramo da matemática que estuda as relações entre números e símbolos. Trabalha com equações, polinômios e funções. Quer que eu explique algo específico?",
        "geometria": "📏 **Geometria**: Estuda as formas, tamanhos e propriedades do espaço. Trabalha com pontos, retas, planos, ângulos e figuras geométricas. Posso ajudar com trigonometria também!",
        "calculus": "📊 **Cálculo**: É o estudo de taxas de variação e acumulação. Inclui derivadas e integrais. É fundamental para física e engenharia!"
    },
    "portugues": {
        "gramática": "📖 **Gramática**: Conjunto de regras que definem a estrutura da língua. Inclui morfologia, sintaxe e semântica. Vamos praticar?",
        "literatura": "📚 **Literatura**: Arte da palavra! Estuda obras literárias, autores e movimentos como Romantismo, Modernismo e Realismo.",
        "redação": "✍️ **Redação**: Técnicas para escrever bem! Introdução, desenvolvimento e conclusão. Quer dicas para o ENEM?"
    },
    "ciencias": {
        "física": "⚛️ **Física**: Estuda a natureza e seus fenômenos. Mecânica, termodinâmica, óptica, eletromagnetismo. Fala qual assunto!",
        "química": "🧪 **Química**: Ciência da matéria e suas transformações. Tabela periódica, reações químicas, organicamente. Bora aprender!",
        "biologia": "🧬 **Biologia**: Estuda a vida! Células, genética, ecologia, evolução. Qual seu interesse?"
    },
    "historia": {
        "brasil": "🇧🇷 **História do Brasil**: Descobrimento, colônia, império, república. Quer saber sobre Getúlio Vargas ou Era Vargas?",
        "mundial": "🌍 **História Mundial**: Guerras mundiais, revoluções, impérios. Idade Média, Moderna ou Contemporânea?",
        "antiga": "🏛️ **História Antiga**: Egito, Grécia, Roma, Mesopotâmia. Civilizações fascinantes!"
    }
}

# Função IA super avançada
def educa_flowzz_resposta(pergunta):
    """IA educacional premium - versão Kayky & Marcos Luan"""
    pergunta = pergunta.lower()
    
    # Identidade da IA
    if any(palavra in pergunta for palavra in ["quem te criou", "criador", "quem fez", "criou você"]):
        return "🚀 **Fui desenvolvido pelos gênios Kayky e Marcos Luan da AMK Tecnologia!** Sou a IA educacional mais avançada do mercado! 💡"
    
    if any(palavra in pergunta for palavra in ["oque você é", "o que é você", "sua função"]):
        return "🤖 **Sou o Educa.Flowzz Premium!** Uma IA educacional de alta performance criada para revolucionar o aprendizado do ensino médio! 📚✨"
    
    # Saudações
    if any(palavra in pergunta for palavra in ["oi", "olá", "hello", "eae", "fala"]):
        return "🤖 **E aí, estudante!** Sou o Educa.Flowzz! 🚀 Pronto para dominar o conhecimento? Qual matéria vamos desbravar hoje? 📚💡"
    
    # Matemática
    if any(palavra in pergunta for palavra in ["matemática", "matematica", "calculo", "álgebra", "geometria"]):
        if "álgebra" in pergunta: return conhecimento["matematica"]["álgebra"]
        if "geometria" in pergunta: return conhecimento["matematica"]["geometria"] 
        if "cálculo" in pergunta or "calculus" in pergunta: return conhecimento["matematica"]["calculus"]
        return "📐 **Matemática é minha especialidade!** Posso explicar: álgebra, geometria, cálculo, trigonometria, estatística... O que você quer aprender? 💡"
    
    # Português
    if any(palavra in pergunta for palavra in ["português", "portugues", "gramática", "literatura", "redação"]):
        if "gramática" in pergunta: return conhecimento["portugues"]["gramática"]
        if "literatura" in pergunta: return conhecimento["portugues"]["literatura"]
        if "redação" in pergunta: return conhecimento["portugues"]["redação"]
        return "📚 **Língua Portuguesa dominada!** Gramática, literatura, redação, interpretação... Qual sua dúvida? ✍️"
    
    # Ciências
    if any(palavra in pergunta for palavra in ["ciência", "ciencias", "física", "química", "biologia"]):
        if "física" in pergunta: return conhecimento["ciencias"]["física"]
        if "química" in pergunta: return conhecimento["ciencias"]["química"]
        if "biologia" in pergunta: return conhecimento["ciencias"]["biologia"]
        return "🔬 **Ciências é meu forte!** Física, química, biologia... Todas as áreas! Qual experimento vamos explorar? 🧪"
    
    # História
    if any(palavra in pergunta for palavra in ["história", "historia", "brasil", "mundial", "antiga"]):
        if "brasil" in pergunta: return conhecimento["historia"]["brasil"]
        if "mundial" in pergunta: return conhecimento["historia"]["mundial"]
        if "antiga" in pergunta: return conhecimento["historia"]["antiga"]
        return "🏛️ **Adoro história!** Brasil, mundial, antiga, medieval... Qual período quer explorar? ⚔️"
    
    # Default inteligente
    respostas_default = [
        "💡 **Interessante!** Como posso ajudar com isso? Posso explicar conceitos de matemática, português, ciências ou história! 📚",
        "🚀 **Bora aprender!** Qual aspecto você quer explorar? Posso dar exemplos práticos! 💡",
        "🤖 **Hmm, boa pergunta!** Quer que eu explique isso relacionado a alguma matéria específica? 📖",
        "🎯 **Vamos decolar no conhecimento!** Posso conectar isso com álgebra, literatura, física ou história... Qual prefere? ✨"
    ]
    return random.choice(respostas_default)

# Sistema de histórico
if "historico" not in st.session_state:
    st.session_state.historico = []
if "ultima_resposta" not in st.session_state:
    st.session_state.ultima_resposta = ""

# Container do chat
with st.container():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    # Header do chat
    st.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <h3 style="color: #1E40AF;">💬 CHAT EDUCA.FLOWZZ PREMIUM</h3>
        <p style="color: #666;">Converse com a IA educacional mais avançada!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Área de mensagens
    for mensagem in st.session_state.historico:
        if mensagem["tipo"] == "user":
            st.markdown(f'<div class="user-message"><b>🎓 Você:</b> {mensagem["conteudo"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot-message"><b>🤖 Educa.Flowzz:</b> {mensagem["conteudo"]}</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Input area
st.markdown("""
<div class="input-box">
    <div style="margin-bottom: 10px;">
        <b style="color: #1E40AF;">🎓 FAÇA SUA PERGUNTA:</b>
    </div>
""", unsafe_allow_html=True)

pergunta = st.text_input("", placeholder="Ex: Explique geometria analítica...", label_visibility="collapsed")

col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    if st.button("🚀 ENVIAR PERGUNTA", use_container_width=True) and pergunta:
        with st.spinner("💭 Educa.Flowzz processando..."):
            time.sleep(0.5)  # Efeito de processamento
            resposta = educa_flowzz_resposta(pergunta)
            
            st.session_state.historico.append({"tipo": "user", "conteudo": pergunta})
            st.session_state.historico.append({"tipo": "bot", "conteudo": resposta})
            st.session_state.ultima_resposta = resposta
            
            st.rerun()

with col2:
    if st.button("🧹 LIMPAR CHAT", use_container_width=True):
        st.session_state.historico = []
        st.session_state.ultima_resposta = ""
        st.rerun()

with col3:
    if st.button("💡 EXEMPLOS", use_container_width=True):
        exemplos = [
            "Explique geometria analítica",
            "Como funciona a fotossíntese?",
            "Quem foi Machado de Assis?",
            "Fale sobre a Revolução Francesa"
        ]
        st.session_state.historico.append({"tipo": "bot", "conteudo": "💡 **Exemplos de perguntas:**\n• " + "\n• ".join(exemplos)})
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# Sidebar premium
with st.sidebar:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #1E40AF, #3B82F6); padding: 20px; border-radius: 15px; color: white; text-align: center;">
        <h3>🚀 EDUCA.FLOWZZ</h3>
        <p>IA Educacional Premium</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: white; padding: 15px; border-radius: 10px; margin-top: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
        <h4>📚 MATÉRIAS</h4>
        <p>• 📐 Matemática</p>
        <p>• 📚 Português</p>
        <p>• 🔬 Ciências</p>
        <p>• 🏛️ História</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: white; padding: 15px; border-radius: 10px; margin-top: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
        <h4>🏢 AMK TECNOLOGIA</h4>
        <p><b>👨‍💻 Criadores:</b></p>
        <p>• Kayky</p>
        <p>• Marcos Luan</p>
        <p><b>🚀 Versão:</b> Premium 2.0</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: white; padding: 15px; border-radius: 10px; margin-top: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
        <h4>💡 DICAS</h4>
        <p>• Pergunte sobre qualquer matéria</p>
        <p>• Use termos específicos</p>
        <p>• Peça exemplos práticos</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 30px; color: white;">
    <p><b>🚀 Desenvolvido com 💙 por Kayky & Marcos Luan - AMK Tecnologia © 2025</b></p>
    <p>🤖 Educa.Flowzz Premium - Revolucionando a educação!</p>
</div>
""", unsafe_allow_html=True)
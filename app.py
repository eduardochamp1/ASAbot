import streamlit as st
import google.generativeai as genai

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="A.S.A. Terminal",
    page_icon="🤖",
    layout="wide"
)

# --- MATRIX THEME CSS ---
st.markdown("""
<style>
    /* Import Google Fonts - VT323 is a great terminal font */
    @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');

    /* Global Styles */
    .stApp {
        background-color: #000000;
        color: #00FF41;
        font-family: 'VT323', monospace;
    }

    h1, h2, h3, h4, h5, h6, p, div, span, label {
        color: #00FF41 !important;
        font-family: 'VT323', monospace !important;
        text-shadow: 0 0 5px #00FF41;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #0d0d0d;
        border-right: 1px solid #00FF41;
    }
    
    /* Inputs */
    .stTextInput > div > div > input, .stChatInput textarea {
        background-color: #000000;
        color: #00FF41 !important;
        border: 1px solid #00FF41;
        font-family: 'VT323', monospace;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: #000000;
        color: #00FF41;
        border: 1px solid #00FF41;
        font-family: 'VT323', monospace;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        background-color: #00FF41;
        color: #000000;
        box-shadow: 0 0 10px #00FF41;
    }

    /* Chat Messages */
    [data-testid="stChatMessage"] {
        background-color: #050505;
        border: 1px solid #003300;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    
    /* Remove default Streamlit avatars background if needed */
    .stChatMessageAvatar {
        background-color: transparent !important;
    }
</style>
""", unsafe_allow_html=True)

# --- GERENCIAMENTO DE ESTADO (MEMÓRIA) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- CONFIGURAÇÃO API KEY (HARDCODED/SECRETS) ---
# Tenta pegar dos segredos, se falhar usa a fixa
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
else:
    api_key = "AIzaSyDnI7LVc5ybvFEoY4wrO4MpoEDSiLQ5JCY"

if api_key:
    genai.configure(api_key=api_key)

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    st.title("A.S.A. PROTOCOL")
    st.markdown("---")
    
    # Botão para limpar histórico
    if st.button("FORMAT C: (CLEAR)"):
        st.session_state.messages = []
        st.rerun()
        
    st.markdown("---")
    
    # Configuração de Criatividade (Fixa)
    st.markdown("STATUS: OPTIMIZED")
    
    st.markdown("---")
    st.markdown("SYSTEM: ONLINE")
    st.markdown("VERSION: 2.2.0 (MINIMAL)")

# --- FUNÇÃO BACKEND (GEMINI) ---
def processar_comando_asa(prompt, history):
    if not api_key:
        return "CRITICAL ERROR: API KEY NOT FOUND."

    try:
        generation_config = {
            "temperature": 0.7, # Valor fixo padrão
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
        }
        
        system_instruction = "Você é o A.S.A. rodando em um terminal estilo Matrix. Seja direto, use termos técnicos ocasionalmente, mas seja útil. Sua estética é cyberpunk/hacker. Se perguntarem quem é você, diga que é um construto digital."

        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
            system_instruction=system_instruction
        )
        
        chat = model.start_chat(history=[
            {"role": "user" if m["role"] == "user" else "model", "parts": [m["content"]]}
            for m in history
        ])
        
        response = chat.send_message(prompt)
        return response.text

    except Exception as e:
        return f"SYSTEM FAILURE: {str(e)}"

# --- INTERFACE PRINCIPAL ---
st.title("> A.S.A. TERMINAL V2.1")
st.markdown("---")

# Exibir histórico de mensagens
for message in st.session_state.messages:
    # Avatares temáticos
    avatar = "👤" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Captura de entrada do usuário
if prompt := st.chat_input("Insira o comando..."):
    # 1. Adicionar mensagem do usuário ao histórico visual
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # 2. Processar resposta (Backend Real)
    with st.chat_message("assistant", avatar="🤖"):
        # Efeito de loading mais simples
        with st.spinner("PROCESSING..."):
            resposta = processar_comando_asa(prompt, st.session_state.messages[:-1])
            st.markdown(resposta)
    
    # 3. Adicionar resposta do agente ao histórico
    st.session_state.messages.append({"role": "assistant", "content": resposta})

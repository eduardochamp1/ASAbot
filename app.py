import streamlit as st
import google.generativeai as genai
import time
import random

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="A.S.A. Interface",
    page_icon="🤖",
    layout="wide"
)

# --- GERENCIAMENTO DE ESTADO (MEMÓRIA) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    st.header("Configurações A.S.A.")
    
    # Input da API Key
    api_key = st.text_input("Gemini API Key", type="password", help="Cole sua chave da API do Google Gemini aqui.")
    
    if api_key:
        genai.configure(api_key=api_key)
    
    st.divider()

    # Botão para limpar histórico
    if st.button("Limpar Histórico"):
        st.session_state.messages = []
        st.rerun()
        
    st.divider()
    
    # Configuração de Criatividade
    criatividade = st.slider(
        "Nível de Criatividade", 
        min_value=0.0, 
        max_value=1.0, 
        value=0.7, 
        step=0.1
    )
    st.caption(f"Criatividade atual: {criatividade}")
    
    st.divider()
    st.markdown("### Sobre")
    st.markdown("Interface Web do Agente **A.S.A.**")

# --- FUNÇÃO BACKEND (GEMINI) ---
def processar_comando_asa(prompt, history):
    """
    Processa o comando usando a API do Google Gemini.
    """
    if not api_key:
        return "⚠️ Por favor, insira sua **Gemini API Key** na barra lateral para eu funcionar."

    try:
        # Configuração do Modelo
        generation_config = {
            "temperature": criatividade,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
        }
        
        # Instruções de Sistema (Persona)
        system_instruction = "Você é o A.S.A. (Agente de Suporte e Assistência). Você é um assistente virtual inteligente, prestativo e ligeiramente irônico. Responda de forma concisa e direta, mas com personalidade. Se o usuário falar português, responda em português."

        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
            system_instruction=system_instruction
        )
        
        # Converte histórico do Streamlit para o formato do Gemini
        chat = model.start_chat(history=[
            {"role": "user" if m["role"] == "user" else "model", "parts": [m["content"]]}
            for m in history
        ])
        
        # Envia a mensagem
        response = chat.send_message(prompt)
        return response.text

    except Exception as e:
        return f"❌ Erro ao processar: {str(e)}"

# --- INTERFACE PRINCIPAL ---
st.title("🤖 A.S.A. Interface")

if not api_key:
    st.warning("👈 Para começar, cole sua **Gemini API Key** na barra lateral.")
    st.info("Não tem uma chave? Crie grátis aqui: [Google AI Studio](https://aistudio.google.com/app/apikey)")

# Exibir histórico de mensagens
for message in st.session_state.messages:
    avatar = "👤" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Captura de entrada do usuário
if prompt := st.chat_input("Digite seu comando para o A.S.A...."):
    # 1. Adicionar mensagem do usuário ao histórico visual
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # 2. Processar resposta (Backend Real)
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("A.S.A. está pensando..."):
            # Passa o histórico (excluindo a última msg que acabamos de adicionar para evitar duplicação no envio se não tratada, mas a lib lida bem, aqui passamos o anterior)
            resposta = processar_comando_asa(prompt, st.session_state.messages[:-1])
            st.markdown(resposta)
    
    # 3. Adicionar resposta do agente ao histórico
    st.session_state.messages.append({"role": "assistant", "content": resposta})

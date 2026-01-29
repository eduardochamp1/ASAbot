import streamlit as st
import time
import random

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="A.S.A. Interface",
    page_icon="🤖",
    layout="wide"
)

# --- FUNÇÃO BACKEND SIMULADA ---
def processar_comando_asa(prompt):
    """
    Função dummy que simula o processamento do agente A.S.A.
    Substitua esta lógica pela chamada real ao seu agente.
    """
    # Simula um tempo de "pensamento"
    time.sleep(random.uniform(0.5, 2.0))
    
    # Respostas simuladas para teste
    respostas = [
        "Entendi seu comando. Estou processando...",
        "Interessante. Aqui está o que encontrei sobre isso.",
        "Poderia detalhar um pouco mais?",
        "Executando tarefa solicitada nos bastidores.",
        "Olá! Sou o A.S.A., seu assistente virtual. Como posso ajudar?"
    ]
    
    return random.choice(respostas)

# --- GERENCIAMENTO DE ESTADO (MEMÓRIA) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    st.header("Configurações A.S.A.")
    
    # Botão para limpar histórico
    if st.button("Limpar Histórico"):
        st.session_state.messages = []
        st.rerun()
        
    st.divider()
    
    # Configuração visual de criatividade (apenas exemplo)
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

# --- INTERFACE PRINCIPAL ---
st.title("🤖 A.S.A. Interface")

# Exibir histórico de mensagens
for message in st.session_state.messages:
    # Define o avatar com base no papel (user ou assistant)
    avatar = "👤" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Captura de entrada do usuário
if prompt := st.chat_input("Digite seu comando para o A.S.A...."):
    # 1. Adicionar mensagem do usuário ao histórico visual
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # 2. Processar resposta (Simulação do Backend)
    with st.chat_message("assistant", avatar="🤖"):
        # Placeholder para efeito de "digitando" se quiser, ou apenas spinner
        with st.spinner("A.S.A. está pensando..."):
            resposta = processar_comando_asa(prompt)
            st.markdown(resposta)
    
    # 3. Adicionar resposta do agente ao histórico
    st.session_state.messages.append({"role": "assistant", "content": resposta})

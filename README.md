# A.S.A. Interface Web

Interface web moderna para o agente A.S.A., construída com [Streamlit](https://streamlit.io/).

## Como Rodar

### Pré-requisitos
Certifique-se de ter o Python instalado. Instale as dependências:

```bash
pip install streamlit
```

### Executando Localmente
No terminal, navegue até a pasta do projeto e execute:

```bash
streamlit run app.py
```

O navegador abrirá automaticamente em `http://localhost:8501`.

### Executando na Rede Local (Ubuntu/Linux)
Para que outros dispositivos na sua rede acessem a interface:

1.  **Libere a porta no Firewall (se estiver ativo):**
    ```bash
    sudo ufw allow 8501/tcp
    ```

2.  **Execute o Streamlit apontando para 0.0.0.0:**
    ```bash
    streamlit run app.py --server.port 8501 --server.address 0.0.0.0
    ```

3.  **Acesse de outro dispositivo:**
    Descubra seu IP com `ip addr show` (procure por `inet` na interface correta, ex: `192.168.x.x`).
    No navegador do outro dispositivo, digite: `http://SEU_IP_AQUI:8501`.

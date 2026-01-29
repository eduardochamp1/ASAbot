# Guia de Implantação (Deployment)

Este guia ajudará você a colocar a interface do seu agente **A.S.A.** na internet usando o GitHub e o Streamlit Cloud.

## Passo 1: Criar Repositório no GitHub

1.  Acesse [github.com/new](https://github.com/new) e faça login.
2.  **Repository name**: Digite um nome (ex: `asa-interface`).
3.  **Public/Private**: Escolha **Public** (Gratuito e mais fácil para o Streamlit Cloud) ou **Private**.
4.  **NÃO** marque as opções de "Initialize this repository with..." (nós já criamos os arquivos locais).
5.  Clique em **Create repository**.

## Passo 2: Enviar Código para o GitHub

Copie a URL do repositório que você acabou de criar (algo como `https://github.com/SEU_USUARIO/asa-interface.git`).

Abra o terminal na pasta do projeto e execute:

### 2.1. Configurar Identidade (Se for sua primeira vez usando Git)
Se você nunca usou Git antes, precisará se identificar:
```bash
git config --global user.email "seu_email@exemplo.com"
git config --global user.name "Seu Nome"
```

### 2.2. Confirmar as alterações (Commit)
Como eu não consegui fazer o commit por falta de configuração, rode:
```bash
git commit -m "Commit inicial A.S.A."
```

### 2.3. Enviar para o GitHub
```bash
git branch -M main
git remote add origin https://github.com/eduardochamp1/ASAbot.git
git push -u origin main
```

> **Nota:** Se ele pedir senha, você precisará usar um "Personal Access Token" ou configurar autenticação SSH/Git Credential Manager.

## Passo 3: Conectar ao Streamlit Cloud

1.  Acesse [share.streamlit.io](https://share.streamlit.io/) e faça login com seu GitHub.
2.  Clique em **"New app"**.
3.  Selecione o repositório (`asa-interface`) que você acabou de criar.
4.  **Main file path**: Certifique-se de que está como `app.py`.
5.  Clique em **Deploy!**

## Pronto! 🚀
Em alguns minutos, seu app estará online e você receberá um link (ex: `https://asa-interface.streamlit.app`) para compartilhar ou acessar do celular.

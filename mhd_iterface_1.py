import streamlit as st

# Inicializar o estado da sessão para etapas e descrição
if "etapas" not in st.session_state:
    st.session_state["etapas"] = []
if "descricao_etapa" not in st.session_state:
    st.session_state["descricao_etapa"] = ""

# Título do aplicativo
st.title("Modelo Hipotético-Dedutivo no Xadrez")

# Seleção de tópicos
etapas_mhd = [
    "Base Teórica",
    "Hipótese",
    "Consequências",
    "Experimento",
    "Observações",
    "Avaliação",
]

topico_selecionado = st.selectbox("Escolha o tópico da etapa:", etapas_mhd)

# Dicas associadas aos tópicos
dicas = {
    "Base Teórica": "Explique a base teórica que fundamenta sua análise.",
    "Hipótese": "Formule a hipótese que será testada.",
    "Consequências": "Liste as consequências esperadas caso a hipótese seja verdadeira.",
    "Experimento": "Descreva como o experimento será conduzido para testar a hipótese.",
    "Observações": "Anote as observações obtidas durante o experimento.",
    "Avaliação": "Avalie os resultados à luz da hipótese e da base teórica.",
}

# Mostrar dica com base no tópico selecionado
st.info(dicas[topico_selecionado])

# Campo de texto para descrição da etapa
descricao = st.text_area("Descreva a etapa:", key="descricao_etapa")

# Botão para adicionar etapa
if st.button("Adicionar Etapa"):
    if descricao.strip():
        st.session_state["etapas"].append({
            "topico": topico_selecionado,
            "descricao": descricao,
        })
        st.session_state["descricao_etapa"] = ""  # Limpar o campo de descrição
    else:
        st.warning("A descrição da etapa não pode estar vazia.")

# Configuração do tabuleiro
st.subheader("Configuração do Tabuleiro")
fen_input = st.text_input("Insira a configuração FEN:")
if st.button("Atualizar Tabuleiro com FEN"):
    if fen_input.strip():
        st.session_state["fen"] = fen_input
    else:
        st.warning("O campo FEN não pode estar vazio.")

# Exibir tabuleiro atual
st.subheader("Tabuleiro Atual")
if "fen" in st.session_state and st.session_state["fen"]:
    st.text(f"FEN Atual: {st.session_state['fen']}")
else:
    st.text("O tabuleiro ainda não foi configurado.")

# Listar etapas adicionadas
st.subheader("Etapas Adicionadas")
if st.session_state["etapas"]:
    for i, etapa in enumerate(st.session_state["etapas"], start=1):
        st.write(f"**{i}. {etapa['topico']}**: {etapa['descricao']}")
else:
    st.text("Nenhuma etapa adicionada ainda.")

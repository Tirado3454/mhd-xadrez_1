import streamlit as st

# Definir as dicas para cada etapa
dicas = {
    "Base Teórica": "Explique a base teórica para a posição escolhida.",
    "Hipótese": "Formule uma hipótese com base na posição configurada.",
    "Consequências": "Descreva as consequências esperadas da sua hipótese.",
    "Experimento": "Detalhe como testar a hipótese na prática.",
    "Observações": "Anote as observações feitas durante o experimento.",
    "Avaliação": "Avalie os resultados obtidos e conclua o experimento."
}

# Inicializar o estado da sessão, se necessário
if "etapas" not in st.session_state:
    st.session_state.etapas = []
if "descricao_etapa" not in st.session_state:
    st.session_state.descricao_etapa = ""

# Título principal
st.title("Modelo Hipotético-Dedutivo no Xadrez")

# Seletor de etapas
topico = st.selectbox("Escolha o tópico da etapa:", list(dicas.keys()))

# Mostrar a dica correspondente
st.info(dicas[topico])

# Campo de texto para descrição da etapa
st.session_state.descricao_etapa = st.text_area("Descreva a etapa:", st.session_state.descricao_etapa)

# Botão para adicionar etapa
if st.button("Adicionar Etapa"):
    if st.session_state.descricao_etapa.strip():
        st.session_state.etapas.append({"tópico": topico, "descrição": st.session_state.descricao_etapa})
        st.session_state.descricao_etapa = ""  # Limpar o campo de descrição

# Configuração do Tabuleiro
st.subheader("Configuração do Tabuleiro")
fen = st.text_input("Insira a configuração FEN:")
if st.button("Atualizar Tabuleiro com FEN"):
    st.session_state.fen_atual = fen

# Exibir o tabuleiro atual
st.subheader("Tabuleiro Atual")
st.write("(O tabuleiro será renderizado aqui com base na FEN fornecida.)")

# Mostrar as etapas adicionadas
st.subheader("Etapas Adicionadas")
if st.session_state.etapas:
    for i, etapa in enumerate(st.session_state.etapas, start=1):
        st.write(f"**Etapa {i}: {etapa['tópico']}**")
        st.write(etapa["descrição"])
else:
    st.write("Nenhuma etapa adicionada ainda.")

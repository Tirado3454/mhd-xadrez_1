import streamlit as st
from streamlit_chessboard import chessboard

# Inicializando o estado da sessão
if "etapas" not in st.session_state:
    st.session_state["etapas"] = []
if "descricao_etapa" not in st.session_state:
    st.session_state["descricao_etapa"] = ""
if "fen" not in st.session_state:
    st.session_state["fen"] = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

# Função para atualizar as dicas com base no tópico selecionado
def atualizar_dica(topico):
    dicas = {
        "Base Teórica": "Descreva a base teórica que fundamenta a etapa.",
        "Hipótese": "Defina a hipótese a ser testada.",
        "Consequências": "Liste as consequências esperadas da hipótese.",
        "Experimento": "Explique como será realizado o experimento.",
        "Observações": "Relate as observações feitas durante o experimento.",
        "Avaliação": "Avalie os resultados obtidos."
    }
    return dicas.get(topico, "Selecione um tópico para ver a dica.")

# Interface do usuário
st.title("Modelo Hipotético-Dedutivo no Xadrez")

# Seleção do tópico
topico = st.selectbox(
    "Selecione o tópico da etapa:",
    ["Base Teórica", "Hipótese", "Consequências", "Experimento", "Observações", "Avaliação"]
)

# Atualiza e exibe a dica com base no tópico selecionado
dica = atualizar_dica(topico)
st.info(dica)

# Campo para descrever a etapa
st.session_state.descricao_etapa = st.text_area(
    "Descreva a etapa:",
    value=st.session_state.descricao_etapa,
    key="descricao_etapa"
)

# Botão para adicionar nova etapa
if st.button("Adicionar Etapa"):
    nova_etapa = {
        "topico": topico,
        "descricao": st.session_state.descricao_etapa,
        "fen": st.session_state.fen
    }
    st.session_state.etapas.append(nova_etapa)
    st.session_state.descricao_etapa = ""  # Limpar o campo de descrição
    st.success("Etapa adicionada com sucesso!")

# Editor do tabuleiro de xadrez
st.subheader("Configuração do Tabuleiro")
st.session_state.fen = st.text_input("Atualizar tabuleiro com FEN:", value=st.session_state.fen)

# Renderizar o tabuleiro
chessboard(fen=st.session_state.fen, theme="green")

# Exibir as etapas adicionadas
st.subheader("Etapas Adicionadas")
for i, etapa in enumerate(st.session_state.etapas):
    st.write(f"**Etapa {i+1}: {etapa['topico']}**")
    st.write(etapa["descricao"])
    st.write(f"Tabuleiro: {etapa['fen']}")

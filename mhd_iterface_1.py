import streamlit as st
from streamlit_chessboard import chessboard

# Inicialização do estado da sessão
if "etapas" not in st.session_state:
    st.session_state["etapas"] = []
if "descricao_etapa" not in st.session_state:
    st.session_state["descricao_etapa"] = ""
if "dica" not in st.session_state:
    st.session_state["dica"] = "Selecione uma etapa para ver a dica."
if "fen" not in st.session_state:
    st.session_state["fen"] = "start"

# Função para obter a dica com base na etapa selecionada
def obter_dica(etapa):
    dicas = {
        "Base Teórica": "Descreva o conhecimento teórico relacionado a esta posição.",
        "Hipótese": "Formule uma hipótese com base na posição atual do tabuleiro.",
        "Consequências": "Quais são as consequências possíveis da sua hipótese?",
        "Experimento": "Descreva o experimento para testar sua hipótese.",
        "Observações": "Anote as observações feitas durante o experimento.",
        "Avaliação": "Avalie os resultados obtidos e tire conclusões."
    }
    return dicas.get(etapa, "Selecione uma etapa para ver a dica.")

# Interface principal
st.title("Modelo Hipotético-Dedutivo no Xadrez")

# Seleção de etapa
topicos = ["Base Teórica", "Hipótese", "Consequências", "Experimento", "Observações", "Avaliação"]
etapa_selecionada = st.selectbox("Selecione o tópico da etapa:", topicos)

# Atualizar a dica com base na etapa selecionada
st.session_state["dica"] = obter_dica(etapa_selecionada)

# Exibir dica
st.info(st.session_state["dica"])

# Campo de descrição da etapa
st.session_state["descricao_etapa"] = st.text_area("Descreva a etapa:", value=st.session_state["descricao_etapa"], key="descricao_etapa")

# Botão para adicionar etapa
if st.button("Adicionar Etapa"):
    nova_etapa = {
        "etapa": etapa_selecionada,
        "descricao": st.session_state["descricao_etapa"],
        "fen": st.session_state["fen"]
    }
    st.session_state["etapas"].append(nova_etapa)
    st.session_state["descricao_etapa"] = ""  # Limpar o campo de descrição
    st.success(f"Etapa '{etapa_selecionada}' adicionada com sucesso!")

# Configuração do tabuleiro de xadrez
st.markdown("### Configuração do Tabuleiro")
st.session_state["fen"] = st.text_input("Atualizar tabuleiro com FEN:", value=st.session_state["fen"], key="fen")

# Exibir o tabuleiro de xadrez
chessboard(fen=st.session_state["fen"], key="chessboard")

# Exibir etapas adicionadas
if st.session_state["etapas"]:
    st.markdown("### Etapas Adicionadas")
    for i, etapa in enumerate(st.session_state["etapas"], 1):
        st.markdown(f"**Etapa {i}: {etapa['etapa']}**")
        st.write(f"Descrição: {etapa['descricao']}")
        st.write(f"FEN: {etapa['fen']}")

import streamlit as st
from streamlit_chessboard import chessboard

def main():
    st.title("Modelo Hipotético-Dedutivo no Xadrez")

    if "etapas" not in st.session_state:
        st.session_state.etapas = []

    if "descricao_etapa" not in st.session_state:
        st.session_state.descricao_etapa = ""

    if "fen" not in st.session_state:
        st.session_state.fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

    # Tópicos do MHD
    topicos = {
        "Base Teórica": "Explique a base teórica do problema.",
        "Hipótese": "Formule uma hipótese para o problema.",
        "Consequências": "Liste as consequências esperadas.",
        "Experimento": "Descreva o experimento para testar a hipótese.",
        "Observações": "Anote as observações do experimento.",
        "Avaliação": "Avalie os resultados do experimento."
    }

    # Seleção do tópico
    topico_selecionado = st.selectbox("Selecione o tópico da etapa:", list(topicos.keys()), key="topico")

    # Exibir a dica correspondente ao tópico
    st.info(topicos[topico_selecionado])

    # Campo para descrever a etapa
    st.session_state.descricao_etapa = st.text_area("Descreva a etapa:", st.session_state.descricao_etapa)

    # Botão para adicionar a etapa
    if st.button("Adicionar Etapa"):
        if st.session_state.descricao_etapa:
            nova_etapa = {
                "tópico": topico_selecionado,
                "descrição": st.session_state.descricao_etapa
            }
            st.session_state.etapas.append(nova_etapa)
            st.session_state.descricao_etapa = ""  # Limpar o campo de descrição
            st.success("Etapa adicionada com sucesso!")
        else:
            st.warning("Por favor, descreva a etapa antes de adicioná-la.")

    # Configuração do tabuleiro
    st.subheader("Configuração do Tabuleiro")
    fen_input = st.text_input("Insira a configuração FEN:", st.session_state.fen)

    if st.button("Atualizar Tabuleiro com FEN"):
        st.session_state.fen = fen_input

    # Exibir o tabuleiro atual
    st.subheader("Tabuleiro Atual")
    chessboard(fen=st.session_state.fen, height=350)

    # Exibir as etapas adicionadas
    st.subheader("Etapas Adicionadas")
    for i, etapa in enumerate(st.session_state.etapas, start=1):
        st.markdown(f"**Etapa {i}:**")
        st.write(f"**Tópico:** {etapa['tópico']}")
        st.write(f"**Descrição:** {etapa['descrição']}")

if __name__ == "__main__":
    main()

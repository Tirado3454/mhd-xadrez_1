import streamlit as st
import chess
import chess.svg
from streamlit_chessboard import chessboard

# Inicializar o estado da aplicação
if "etapas" not in st.session_state:
    st.session_state["etapas"] = []
if "descricao_etapa" not in st.session_state:
    st.session_state["descricao_etapa"] = ""
if "fen" not in st.session_state:
    st.session_state["fen"] = chess.Board().fen()

# Função para adicionar uma nova etapa
def adicionar_etapa():
    if st.session_state.descricao_etapa:
        st.session_state.etapas.append(
            {
                "etapa": st.session_state.etapa_selecionada,
                "descricao": st.session_state.descricao_etapa,
                "fen": st.session_state.fen,
            }
        )
        st.session_state.descricao_etapa = ""  # Limpar o campo de descrição

# Dicionário de dicas por etapa
dicas = {
    "Base Teórica": "Descreva os fundamentos teóricos relacionados à posição do tabuleiro.",
    "Hipótese": "Formule uma hipótese com base na posição inicial das peças no tabuleiro.",
    "Consequências": "Liste as possíveis consequências que podem ocorrer a partir dessa posição.",
    "Experimento": "Descreva um experimento prático que pode ser realizado com essa posição.",
    "Observações": "Registre observações obtidas a partir do experimento.",
    "Avaliação": "Avalie os resultados do experimento em relação à hipótese inicial.",
}

# Título da aplicação
st.title("Modelo Hipotético-Dedutivo no Xadrez")

# Seção de seleção de etapas e descrição
st.sidebar.header("Configuração da Etapa")

# Seleção da etapa
st.session_state.etapa_selecionada = st.sidebar.selectbox(
    "Selecione a etapa do MHD", list(dicas.keys())
)

# Exibição da dica correspondente à etapa selecionada
st.sidebar.info(dicas[st.session_state.etapa_selecionada])

# Campo para descrever a etapa
st.sidebar.text_area(
    "Descreva a etapa:",
    value=st.session_state.descricao_etapa,
    on_change=lambda: setattr(
        st.session_state, "descricao_etapa", st.sidebar.text_area("Descreva a etapa:")
    ),
    key="descricao_etapa",
)

# Botão para adicionar nova etapa
st.sidebar.button("Adicionar Etapa", on_click=adicionar_etapa)


    # Visualizar tabuleiro configurado
    st.markdown("### Tabuleiro Atual")
    st.image(render_tabuleiro_customizado(st.session_state.current_board), use_container_width=True)

# ExibiÃ§Ã£o da tabela dinÃ¢mica
st.subheader("Tabela do Modelo HipotÃ©tico-Dedutivo")
if not st.session_state.mhd_data.empty:
    for index, row in st.session_state.mhd_data.iterrows():
        st.markdown(f"**Etapa:** {row['Etapa']}")
        st.markdown(f"**DescriÃ§Ã£o:** {row['DescriÃ§Ã£o']}")
        st.image(render_tabuleiro_customizado(chess.Board(row['FEN'])), use_container_width=True)
else:
    st.info("Nenhuma etapa adicionada ainda.")

# Exportar a tabela para CSV
st.markdown("### ExportaÃ§Ã£o de Dados")
if not st.session_state.mhd_data.empty:
    csv_data = st.session_state.mhd_data.to_csv(index=False)
    st.download_button(
        label="Baixar Tabela como CSV",
        data=csv_data,
        file_name="mhd_xadrez.csv",
        mime="text/csv"
    )
else:
    st.info("Nenhum dado disponÃ­vel para exportaÃ§Ã£o.")
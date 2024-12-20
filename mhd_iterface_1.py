import streamlit as st
import pandas as pd
import chess
import chess.svg

# Configuração inicial da interface
st.set_page_config(page_title="Modelo Hipotético-Dedutivo no Xadrez", layout="centered")
st.title("♟️ Modelo Hipotético-Dedutivo no Xadrez")
st.write("Configure e salve posições personalizadas no tabuleiro.")

# Inicialização da tabela de dados
if "mhd_data" not in st.session_state:
    st.session_state.mhd_data = pd.DataFrame(columns=["Etapa", "Descrição", "FEN"])

# Inicialização do tabuleiro
if "current_board" not in st.session_state:
    st.session_state.current_board = chess.Board()

# Configuração do tabuleiro com FEN
st.markdown("### Configuração do Tabuleiro")
fen_input = st.text_input(
    "Insira a notação FEN para configurar o tabuleiro:", 
    value=st.session_state.current_board.fen()
)

if st.button("Atualizar Tabuleiro com FEN"):
    try:
        st.session_state.current_board.set_fen(fen_input)
        st.success("Tabuleiro atualizado com sucesso!")
    except ValueError:
        st.error("Notação FEN inválida. Por favor, insira uma notação correta.")

# Formulário para entrada dos dados
st.markdown("### Adicionar Nova Etapa")
with st.form("mhd_form"):
    etapa = st.selectbox("Selecione a Etapa", ["Base Teórica", "Hipótese", "Consequências", "Experimento", "Observações", "Avaliação"])
    descricao = st.text_area("Descreva a etapa:", height=100)

    # Visualizar tabuleiro configurado
    st.markdown("### Tabuleiro Atual")
    st.image(chess.svg.board(board=st.session_state.current_board), use_column_width=True)

    submitted = st.form_submit_button("Adicionar Etapa")
    if submitted:
        if descricao.strip():
            nova_entrada = pd.DataFrame({
                "Etapa": [etapa],
                "Descrição": [descricao],
                "FEN": [st.session_state.current_board.fen()]
            })
            st.session_state.mhd_data = pd.concat([st.session_state.mhd_data, nova_entrada], ignore_index=True)
            st.success(f"Etapa '{etapa}' adicionada com sucesso!")
        else:
            st.error("A descrição não pode estar vazia!")

# Exibição da tabela dinâmica
st.subheader("Tabela do Modelo Hipotético-Dedutivo")
if not st.session_state.mhd_data.empty:
    for index, row in st.session_state.mhd_data.iterrows():
        st.markdown(f"**Etapa:** {row['Etapa']}")
        st.markdown(f"**Descrição:** {row['Descrição']}")
        st.image(chess.svg.board(chess.Board(row['FEN'])), use_column_width=True)
else:
    st.info("Nenhuma etapa adicionada ainda.")

# Exportar a tabela para CSV
if not st.session_state.mhd_data.empty:
    st.download_button(
        label="Baixar Tabela como CSV",
        data=st.session_state.mhd_data.to_csv(index=False),
        file_name="mhd_xadrez.csv",
        mime="text/csv"
    )

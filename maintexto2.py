import streamlit as st
import pandas as pd

# Títulos e introdução
st.title("Seleção de Questões - Ensino de Ciência e Xadrez")
st.markdown("### Escolha as questões que deseja incluir em sua aula:")

# Banco de questões organizadas por categorias
questoes = {
    "Observação": [
        "Quais aspectos desta posição no tabuleiro merecem maior atenção?",
        "O que você pode inferir observando a posição das peças do adversário?",
        "Que padrões podem ser identificados nesta situação?",
        "O que a estrutura do tabuleiro sugere sobre os planos do adversário?",
    ],
    "Hipótese": [
        "Se você mover esta peça, o que espera que aconteça?",
        "Qual seria o impacto de priorizar uma jogada defensiva em vez de uma ofensiva?",
        "Que hipóteses você pode levantar sobre as intenções do adversário?",
        "Como esta jogada pode afetar sua estratégia de médio e longo prazo?",
    ],
    "Dedução": [
        "Quais consequências lógicas derivam desta hipótese?",
        "Se esta peça for capturada, como isso mudará o equilíbrio de poder no tabuleiro?",
        "Que ameaças podem surgir a partir desta posição?",
        "Quais possibilidades devem ser previstas após esta sequência de movimentos?",
    ],
    "Análise": [
        "O resultado da jogada confirmou ou refutou sua hipótese?",
        "Como você avalia as consequências da sua decisão no tabuleiro?",
        "Que ajustes são necessários para melhorar sua abordagem?",
        "Que lições você pode tirar desta sequência de jogadas?",
    ],
}

# Armazenar as seleções
selecoes = {}

# Interface para seleção de questões
for categoria, perguntas in questoes.items():
    st.markdown(f"#### {categoria}")
    selecoes[categoria] = []
    for pergunta in perguntas:
        if st.checkbox(pergunta, key=f"{categoria}_{pergunta}"):
            selecoes[categoria].append(pergunta)

# Botão para exportar as questões selecionadas
st.markdown("### Exportar Questões Selecionadas")
if st.button("Exportar para CSV"):
    # Convertendo as seleções para um DataFrame
    perguntas_selecionadas = [
        {"Categoria": categoria, "Pergunta": pergunta}
        for categoria, perguntas in selecoes.items()
        for pergunta in perguntas
    ]
    if perguntas_selecionadas:
        df = pd.DataFrame(perguntas_selecionadas)
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="Baixar CSV",
            data=csv,
            file_name="questoes_selecionadas.csv",
            mime="text/csv",
        )
    else:
        st.warning("Nenhuma questão foi selecionada para exportação.")

if st.button("Exportar para PDF"):
    from fpdf import FPDF

    perguntas_selecionadas = [
        {"Categoria": categoria, "Pergunta": pergunta}
        for categoria, perguntas in selecoes.items()
        for pergunta in perguntas
    ]
    if perguntas_selecionadas:
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Questões Selecionadas", ln=True, align="C")
        pdf.ln(10)
        for item in perguntas_selecionadas:
            pdf.set_font("Arial", style="B", size=12)
            pdf.cell(200, 10, txt=f"Categoria: {item['Categoria']}", ln=True)
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, item["Pergunta"])
            pdf.ln(5)
        pdf_output = pdf.output(dest="S").encode("latin1")
        st.download_button(
            label="Baixar PDF",
            data=pdf_output,
            file_name="questoes_selecionadas.pdf",
            mime="application/pdf",
        )
    else:
        st.warning("Nenhuma questão foi selecionada para exportação.")

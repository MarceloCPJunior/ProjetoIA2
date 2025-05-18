import streamlit as st
import pandas as pd

from app.services.tratamento_dados import TratamentoDados
from controllers.arquivo_controller import carregar_arquivo

st.set_page_config(page_title="Análise ENADE", layout="wide")

st.title("Sistema de Processamento de Dados ENADE")

# Etapa 1: Upload do arquivo
st.header("1. Upload do Arquivo")
df = carregar_arquivo()

# Etapa 2: Tratamento e Visualização dos dados
if df is not None:
    st.success("Arquivo carregado com sucesso!")

    # Etapa 3: Normalizar headers
    df = TratamentoDados.normalizar_colunas(df)

    # Etapa 4: Visualização do DataFrame normalizado
    st.subheader("Pré-visualização dos dados normalizados")
    st.dataframe(df.head())

    try:
        registros = TratamentoDados.converter_para_registros(df)
        st.success(f"{len(registros)} registros carregados com sucesso!")

        # Opção para visualizar todos os dados
        if st.checkbox("Exibir todos os registros convertidos"):
            st.subheader("Todos os registros convertidos")
            # Como registros são instâncias de Pydantic, convertemos para dicionário antes de exibir
            registros_dict = [r.model_dump() for r in registros]
            st.dataframe(pd.DataFrame(registros_dict))

    except Exception as e:
        st.error(f"Erro ao converter dados: {e}")
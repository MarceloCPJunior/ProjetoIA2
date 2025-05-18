import pandas as pd
from typing import List

from app.models.registro import Registro


class TratamentoDados:
    @staticmethod
    def normalizar_colunas(df: pd.DataFrame) -> pd.DataFrame:
        colunas_convertidas = {
            "NU_ANO": "nu_ano",
            "CO_CURSO": "co_curso",
            "CO_IES": "co_ies",
            "CO_CATEGAD": "co_categoria",
            "CO_ORGACAD": "co_orgacad",
            "CO_GRUPO": "co_grupo",
            "CO_MODALIDADE": "co_modalidade",
            "CO_MUNIC_CURSO": "co_municipio",
            "CO_UF_CURSO": "co_uf",
            "CO_REGIAO_CURSO": "co_regiao",
        }
        return df.rename(columns=colunas_convertidas)

    @staticmethod
    def converter_para_registros(df: pd.DataFrame) -> List[Registro]:
        df_normalizado = TratamentoDados.normalizar_colunas(df)
        dados = df_normalizado.to_dict(orient="records")
        return [Registro(**linha) for linha in dados]

from pydantic import BaseModel, Field

class Registro(BaseModel):
    nu_ano: int = Field(alias="NU_ANO")
    co_curso: int = Field(alias="CO_CURSO")
    co_ies: int = Field(alias="CO_IES")
    co_categoria: int = Field(alias="CO_CATEGAD")
    co_orgacad: int = Field(alias="CO_ORGACAD")
    co_grupo: int = Field(alias="CO_GRUPO")
    co_modalidade: int = Field(alias="CO_MODALIDADE")
    co_municipio: int = Field(alias="CO_MUNIC_CURSO")
    co_uf: int = Field(alias="CO_UF_CURSO")
    co_regiao: int = Field(alias="CO_REGIAO_CURSO")

    model_config = {
        "populate_by_name": True  # <- isso permite passar nu_ano=..., co_curso=..., etc.
    }
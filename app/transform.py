'''imports'''
from typing import Literal
import pandas as pd


def filter_data(
    df: pd.DataFrame,
    columns: str,
    value: str
) -> pd.DataFrame:
    '''filtra o df de acordo com a coluna informada'''
    return df[df[columns] == value]



def group_data(
    df: pd.DataFrame,
    coluna_agrupar: str,
) -> pd.DataFrame:
    '''Agrupa os dados pela coluna informada'''
    colunas_metricas = [
        "Vendas Valor",
        "Vendas Unidades"
    ]
    return (
        df.groupby(coluna_agrupar)[colunas_metricas]
        .sum()
        .reset_index()
        .sort_values(by="Vendas Valor", ascending=False)
    )


def merge_data(
    df_left: pd.DataFrame,
    df_right: pd.DataFrame,
    chave_left: str,
    chave_right: str,
    how: Literal["left", "right", "inner", "outer"] = "left",
    validate: Literal["one_to_one", "one_to_many", "many_to_one", "many_to_many"] | None = None,
) -> pd.DataFrame:
    '''Faz o merge nas tabelas'''
    df_left = df_left.copy()
    df_right = df_right.copy()
    
    df_left[chave_left] = df_left[chave_left].astype(str).str.strip()
    df_right[chave_right] = df_right[chave_right].astype(str).str.strip()
    
    return pd.merge(
        left=df_left,
        right=df_right,
        how=how,
        left_on=chave_left,
        right_on=chave_right,
        validate=validate,
        suffixes=("_varejo", "_atacado")
    )

'''imports'''
from pathlib import Path

import pandas as pd


def load_data(df: pd.DataFrame, path: Path) -> None:
    '''salva o df no path especificado em formato .xlsx'''
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_excel(path)

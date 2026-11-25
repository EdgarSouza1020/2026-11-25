'''imports'''
from pathlib import Path
import pandas as pd

def load_data(path: Path) -> pd.DataFrame:
    '''recebe um caminho e carrega uma base .xlsx'''
    return pd.read_excel(path)

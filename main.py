'''imports'''
from app import config
from app import extract
from app import transform
from app import load

def main():
    
    df = extract.load_data(config.INPUT_DIR / "export.xlsx")
    
    print(df["Markets"].unique())

    df_varejo = transform.filter_data(df, "Markets", "L4L AS Int SC")
    df_atacado = transform.filter_data(df, "Markets", "L4L C&C Int SC")
    
    df_varejo_agrupado = transform.group_data(df_varejo, "CATEGORIAS SCANTRACK")
    df_atacado_agrupado = transform.group_data(df_atacado, "CATEGORIAS SCANTRACK")
    
    df_unificado = transform.merge_data(df_varejo_agrupado, df_atacado_agrupado, "CATEGORIAS SCANTRACK", "CATEGORIAS SCANTRACK")
    
    print(df_unificado.head(20))
    
if __name__ == "__main__":
    main()

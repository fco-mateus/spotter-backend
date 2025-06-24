import pandas as pd
from fastapi import UploadFile, HTTPException

def ler_arquivo(file: UploadFile) -> pd.DataFrame:
    if file.filename.endswith('.csv'):
        df = pd.read_csv(file.file, dtype=str)
    elif file.filename.endswith('.xlsx'):
        df = pd.read_excel(file.file, dtype=str)
    else:
        raise HTTPException(status_code=400, detail="Formato de arquivo não suportado. Use .csv ou .xlsx")
    return df

"""
This is a boilerplate pipeline 'data_ingestion'
generated using Kedro 0.19.13
"""
import pandas as pd


def extract_transform_html_table(columns_mapping: dict) -> pd.DataFrame:
    """Função genérica para extrair tabelas HTML."""
    data = {
        "Date": [
            "May 21, 2025", "May 20, 2025", "May 19, 2025", "May 18, 2025", "May 15, 2025",
            "May 14, 2025", "May 13, 2025", "May 12, 2025", "May 11, 2025", "May 08, 2025",
            "May 07, 2025", "May 06, 2025", "May 05, 2025", "May 04, 2025", "May 01, 2025",
            "Apr 30, 2025", "Apr 29, 2025", "Apr 28, 2025", "Apr 27, 2025", "Apr 24, 2025",
            "Apr 23, 2025", "Apr 22, 2025"
        ],
        "Price": [
            167.82, 164.99, 161.49, 165.37, 164.93,
            164.77, 162.50, 161.97, 163.10, 177.07,
            177.84, 177.63, 179.98, 179.57, 179.77,
            182.10, 181.91, 180.45, 182.46, 182.49,
            184.83, 191.31
        ],
        "Open": [
            164.99, 161.49, 165.37, 164.93, 164.77,
            162.50, 161.97, 163.10, 177.11, 177.84,
            177.59, 179.96, 179.59, 179.81, 182.18,
            181.91, 180.45, 183.37, 181.48, 182.36,
            191.41, 198.19
        ],
        "High": [
            167.82, 164.99, 165.37, 165.37, 164.93,
            164.77, 162.50, 163.10, 177.11, 177.84,
            177.84, 179.96, 179.98, 179.81, 182.18,
            182.10, 181.91, 183.37, 182.46, 182.49,
            191.41, 198.19
        ],
        "Low": [
            164.99, 161.49, 161.49, 164.93, 164.77,
            162.50, 161.97, 161.97, 163.10, 177.07,
            177.59, 177.63, 179.59, 179.57, 179.77,
            181.91, 180.45, 180.45, 181.48, 182.36,
            184.83, 191.31
        ],
        "Change %": [
            "+1.72%", "+2.17%", "-2.35%", "+0.27%", "+0.10%",
            "+1.40%", "+0.33%", "-0.69%", "-7.89%", "-0.43%",
            "+0.12%", "-1.31%", "+0.23%", "-0.11%", "-1.28%",
            "+0.10%", "+0.81%", "-1.10%", "-0.02%", "-1.27%",
            "-3.39%", "-3.47%"
        ]
    }

    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'], format='%b %d, %Y')
    df = df.sort_values('Date', ascending=False).reset_index(drop=True)
    df['Date'] = df['Date'].dt.strftime('%b %d, %Y')

    return transform_html_table(df, columns_mapping)


def transform_html_table(raw_data: pd.DataFrame, columns_mapping: dict) -> pd.DataFrame:
    """Transformação de dados html."""
    df = raw_data.rename(columns=columns_mapping)

    df['dat_ref'] = pd.to_datetime(df['dat_ref'], format='%b %d, %Y').dt.dat_ref
    df['change_percentage'] = df['change_percentage'].str.replace('%', '', regex=False)

    # Cast numérico
    columns_cast = list(columns_mapping.values())
    columns_cast.remove('dat_ref')

    for col in columns_cast:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    return df

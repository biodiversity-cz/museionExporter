import pandas as pd


def read_table(path: str) -> pd.DataFrame:
    required_columns = [
        "Inventární číslo", "Taxon-nomen", "Confer", "Variabilita", "Originální jméno",
        "(n) Autoři/sběratelé", "Datace sběru", "Určil", "Datum určení",
        "Lokalita - název", "Lokalita - originální název", "Charakteristika místa sběru",
        "Zem. šířka (° ' \")", "Zem. délka (° ' \")", "Zem. délka (°)", "Zem. šířka (°)",
        "Souř. přesnost", "Souř. zdroj", "Nadmořská výška",
        "Fytochorion - kód", "Čtverec", "Poznámka k nálezu"
    ]

    df = pd.read_excel(path)

    available_columns = [col for col in required_columns if col in df.columns]

    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        print("Pozor, následující sloupce nebyly nalezeny v souboru:")
        for col in missing_columns:
            print(f"- {col}")

    return df[available_columns]
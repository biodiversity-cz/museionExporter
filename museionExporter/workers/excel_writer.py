import pandas as pd


def write_to_excel(data: pd.DataFrame, output_path: str, sheet_name: str = 'ready4JACQ') -> None:
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        data.to_excel(writer, index=False, sheet_name = sheet_name)


        worksheet = writer.sheets[sheet_name]

        # Projdeme všechny sloupce a upravíme jejich šířku
        for col in worksheet.columns:
            max_length = 0
            column = col[0].column_letter  # Získáme písmeno sloupce

            for cell in col:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(cell.value)
                except:
                    pass

            adjusted_width = (max_length + 2)  # Přidáme 2 pro mezeru
            worksheet.column_dimensions[column].width = adjusted_width

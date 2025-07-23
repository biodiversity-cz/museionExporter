from museionexporter.exportTypes import ExportTypes
from museionexporter.workers.dwc_writer import create_dwc
from museionexporter.workers.excel_writer import write_to_excel
from museionexporter.export_jacq.pipeline import Pipeline as Jacq
from museionexporter.export_dwc.pipeline import Pipeline as DwC
from museionexporter.export_pladias.pipeline import Pipeline as Pladias


def process_uploaded_file(input_path, output_path, type_str: str,
                          dwc_description: str = "Dataset created from Museion data",
                          dwc_license_name: str = "Creative Commons Attribution 4.0 International",
                          dwc_citation: str = "Museion, Czech Republic",
                          dwc_rights: str = ""):
    pipeline_map = {
        ExportTypes.JACQ.value: (Jacq),
        ExportTypes.PLADIAS.value: (Pladias),
        ExportTypes.DWC.value: (DwC),
    }

    entry = pipeline_map.get(type_str)
    if not entry:
        raise ValueError(f"Neznámý exportní typ: {type_str}")

    pipeline_class = entry
    pipeline = pipeline_class(input_path)
    output_data = pipeline.run()

    if type_str == ExportTypes.DWC.value:
        create_dwc(output_data, output_path, dwc_description, dwc_license_name, dwc_citation,
                   dwc_rights)
    else:
        write_to_excel(output_data, output_path)

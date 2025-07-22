from museionExporter.exportTypes import ExportTypes
from museionExporter.workers.dwc_writer import create_dwc
from museionExporter.workers.excel_writer import write_to_excel
from museionExporter.export_jacq.pipeline import Pipeline as Jacq
from museionExporter.export_dwc.pipeline import Pipeline as DwC
from museionExporter.export_pladias.pipeline import Pipeline as Pladias

def process_uploaded_file(input_path, output_path, type_str: str):
    pipeline_map = {
        ExportTypes.JACQ.value: (Jacq, write_to_excel),
        ExportTypes.PLADIAS.value: (Pladias, write_to_excel),
        ExportTypes.DWC.value: (DwC, create_dwc),
    }

    entry = pipeline_map.get(type_str)
    if not entry:
        raise ValueError(f"Neznámý exportní typ: {type_str}")

    pipeline_class, writer_function = entry

    pipeline = pipeline_class(input_path)
    output_data = pipeline.run()
    writer_function(output_data, output_path)


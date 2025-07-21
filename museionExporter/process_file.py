from museionExporter.exportTypes import ExportTypes
from museionExporter.workers.excel_writer import write_to_excel
from museionExporter.export_jacq.pipeline import Pipeline as Jacq
from museionExporter.export_pladias.pipeline import Pipeline as Pladias

def process_uploaded_file(input_path, output_path, type_str: str):

    if type_str == ExportTypes.JACQ.value:
        pipeline = Jacq(input_path)
    else:
        pipeline = Pladias(input_path)

    output_data = pipeline.run()
    write_to_excel(output_data, output_path)
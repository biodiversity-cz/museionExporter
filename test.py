from museionexporter.exportTypes import ExportTypes
from museionexporter.process_file import process_uploaded_file

input_path = "test/lenka.xlsx"
output_path = "test/output.zip"

process_uploaded_file(input_path, output_path, ExportTypes.DWC.value)

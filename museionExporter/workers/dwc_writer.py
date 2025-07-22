import pandas as pd
from dwcahandler import DwcaHandler, MetaElementTypes
from dwcahandler.dwca import ContentData
from dwcahandler import Eml

def create_dwc(
    data: pd.DataFrame,
    output_path: str,
    dataset_name: str = "occurrences.xlsx",
    description: str = "Dataset created from Museion data",
    license_name: str = "Creative Commons Attribution 4.0 International",
    citation: str = "Museion, Czech Republic",
    rights: str = ""
) -> None:
    core = ContentData(
        data=data,
        type=MetaElementTypes.OCCURRENCE,
        keys=["occurrenceID"]
    )

    eml = Eml(
        dataset_name=dataset_name,
        description=description,
        license=license_name,
        citation=citation,
        rights=rights,
    )

    DwcaHandler.create_dwca(
        core_csv=core,
        ext_csv_list=None,
        eml_content=eml,
        output_dwca=output_path
    )

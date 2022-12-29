from download import download_data


from kfp.components import (
    InputPath,
    OutputPath,
    create_component_from_func,
    load_component_from_file
)

download_data_op = create_component_from_func(
    func = download_data,
    packages_to_install=[
        "google-api-python-client==2.61.0",
        "pathlib==1.0.1",
        "google-cloud-storage==2.5.0",
        "schedule==1.1.0",
        "dnspython==2.2.1",
        "pymongo==4.2.0",
        "python-dotenv==0.21.0",
        "Pillow==7.1.2",
        "torch==1.12.1",
        "numpy==1.21.6"
    ]
)

download_data_op()

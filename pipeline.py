from kfp import dsl
from kfp import compiler
import os

@dsl.pipeline(name='My Pipeline', description='A pipeline with 3 steps')
def my_pipeline():
    data_prep = dsl.ContainerOp(
        name='Data Preparation',
        image='quynhtl/today_code1:latest',
        command=['python', 'download.py'],
        arguments=['--input-dir', '/data/input', '--output-dir', '/data/output'],
        file_outputs = {"output": "/data/output.zip"}
    )

    model_train = dsl.ContainerOp(
        name='Model Training',
        image='quynhtl/today_code1:latest',
        command=['python', 'pytorch_images_classification.py'],
        arguments=['--data-dir', data_prep.outputs['output'], '--output-dir', "./model_train.zip"],
        file_outputs = {"model_path" : "./model/model_train.zip"}
    )
    model_train.after(data_prep)


    # input_path = model_train.inputs['/data/output'].path
    # print(f'Input path of model_train: {input_path}')

    # # Check the contents of the input directory
    # input_dir = os.path.join(input_path, 'data_prep')
    # print(f'Contents of input directory: {os.listdir(input_dir)}')

    model_version = dsl.ContainerOp(
        name='Model Versioning',
        image='quynhtl/today_code1:latest',
        command=['python', 'version_data.py'],
        arguments=['--model-dir', model_train.outputs['model_path'], '--version-dir', '/version']
    )
    model_version.after(model_train)


if __name__ == '__main__':
    compiler.Compiler().compile(my_pipeline, 'my_pipeline.zip')
import zipfile
import os

predict_datadir = 'data'
zip_filename = 'cifar10_train.zip'

predict_filepath = f'{predict_datadir}/{zip_filename}'

filename = zip_filename.rsplit('.', 1)[0]

with zipfile.ZipFile(predict_filepath, 'r') as zip_ref:
    # data/cifar10_train
    zip_predictdatapth = os.path.join(predict_datadir, filename)
    zip_ref.extractall(zip_predictdatapth)
    # # if unzip a same dir name, move files below it out and delete the redundant dir
    for subdir_filename in os.listdir(zip_predictdatapth):
        if subdir_filename == filename:
            os.system(f'mv {zip_predictdatapth}/{filename}/* {zip_predictdatapth}/')
            os.system(f'rm -rf {zip_predictdatapth}/{filename}')

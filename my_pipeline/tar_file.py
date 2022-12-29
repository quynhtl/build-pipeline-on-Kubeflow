# import tarfile
# import builtins
# tarfile = builtins.__import__('tarfile')
# # Tạo một đối tượng TarFile cho tập tin tar
# tar = tarfile.TarFile('ouput.tar.gz','w:gz')

# # Thêm các thư mục vào tập tin tar
# tar.add('./data/train')
# tar.add('./data/validation')

# # Đóng đối tượng TarFile
# tar.close()


import tarfile
import os.path

def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

if __name__ == "__main__":
    make_tarfile('data.tar', 'data')


import os
import zipfile


def compress_files(file_list=None, archive='students.dat'):
    if file_list is None:
        file_list = ['students.txt', 'courses.txt', 'marks.txt']
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
        for fp in file_list:
            if os.path.exists(fp):
                z.write(fp)
    return archive


def decompress_files(archive='students.dat', extract_dir='.'):
    if not os.path.exists(archive):
        return []
    with zipfile.ZipFile(archive, 'r') as z:
        z.extractall(path=extract_dir)
        return z.namelist()
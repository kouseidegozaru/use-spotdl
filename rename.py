from mutagen.easyid3 import EasyID3
import os

def get_file_name(path):
    return os.path.basename(path)

def parse_file_name(file_name):
    file_name_no_slash = file_name.replace('/', '-')
    file_name = file_name_no_slash.replace('\\', '-')
    return file_name.translate(str.maketrans('', '', ':*?"<>|'))

def get_album_name(path):
    id3 = EasyID3(path)
    return id3['album'][0]

def get_disc_number(path):
    id3 = EasyID3(path)
    return id3.get('discnumber', [None])[0]

def get_track_number(path):
    id3 = EasyID3(path)
    return id3['tracknumber'][0]

def rename(path, new_file_name):
    return path.replace(get_file_name(path), new_file_name)

def get_all_file_path(dir_path):
    file_paths = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

def replace_file_name(file_name):
    return file_name.replace('The Beatles - ', '').replace('George Martin - ', '')

def new_file_name(path):
    album_name = get_album_name(path)
    track_number = get_track_number(path)
    disc_number = get_disc_number(path)
    file_name = get_file_name(path)
    replaced_file_name = replace_file_name(file_name)
    new_name = f"{track_number} - {replaced_file_name}"
    parsed_name = parse_file_name(new_name)
    return parsed_name

class NameGroup:
    def __init__(self, file_path, new_file_path) -> None:
        self.file_path = file_path
        self.new_file_path = new_file_path

def rename_all_files(dir_path):
    file_paths = get_all_file_path(dir_path)
    
    file_path_groups = []
    for file_path in file_paths:
        new_file_path = rename(file_path, new_file_name(file_path))
        file_path_groups.append(NameGroup(file_path, new_file_path))
    
    for file_path_group in file_path_groups:
        os.rename(file_path_group.file_path, file_path_group.new_file_path)

if __name__ == "__main__":
    dir_path = input("Enter the directory path: ")
    rename_all_files(dir_path)
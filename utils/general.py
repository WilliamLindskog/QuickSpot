# Import 

from os import listdir, unlink
from shutil import rmtree
from os.path import join, islink, isfile, isdir

# Function 

def empty_folder(path : str, string_part = None) -> None:
    """
        Removes items in folder. 

        Attributes: 
            path: The path is going to be emptied. 
            string_part: Specific files

        Returns:
            None
    """

    # Remove files 
    for filename in listdir(path):

        # Check if string part is None
        if string_part is None:
            file_path = join(path, filename)
            try:
                if isfile(file_path) or islink(file_path):
                    unlink(file_path)
                elif isdir(file_path):
                    rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

        else: 
            if string_part in filename:
                file_path = join(path, filename)
            try:
                if isfile(file_path) or islink(file_path):
                    unlink(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
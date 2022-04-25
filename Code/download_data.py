# Import 

import sys
import wget

sys.path.append('')

from configparser import ConfigParser
from utils.general import empty_folder

# Functions

def main() -> None:

    # Remove content in tmp folder
    empty_folder('./tmp/')

    # Create config parser
    parser = ConfigParser()
    parser.read('./etc/config.ini')

    # Get download link
    url = parser["'Data'"]['url']
    
    # Get data (hm doesn't work without password and account)
    filename = wget.download(url = url, out = './Data/Asteroid/asteroid_data')
    print(filename)

if __name__ == '__main__':
    main()
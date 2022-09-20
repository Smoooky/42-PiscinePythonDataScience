import sys
import subprocess

import os


def is_in_venv() -> bool:
    return os.environ['VIRTUAL_ENV'] == os.getcwd() + "/sstyr"


def install_packages(packages: list, output_file='requirements.txt') -> str:
    if not is_in_venv():
        raise RuntimeError('Wrong virtual environment or it is not running!')
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', *packages])
    installed_packages = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = installed_packages.decode('utf-8')
    print(installed_packages)
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(installed_packages)


if __name__ == '__main__':
    try:
        install_packages(['beautifulsoup4', 'pytest'])
    except RuntimeError as err:
        print(f'Runtime error: {err.args[0]}')
    except KeyError as err:
        print(f'Key error: {err.args[0]}')

# -*- coding: utf-8 -*-
# Author; alin m elena, alin@elena.re
# Contribs;
# Date: 26-07-2024
# ©alin m elena, GPL v3 https://www.gnu.org/licenses/gpl-3.0.en.html

from urllib.request import urlretrieve
from pathlib import Path

default_url = "https://raw.githubusercontent.com/imagdau/Tutorials/main/data/"

def get_data(url: str=default_url, filename: str| list[str] = "", folder: str="data") -> None:
    p = Path(folder)
    p.mkdir(parents=True, exist_ok=True)
    save_file = p/filename
    path, headers = urlretrieve(url+filename, save_file)
    if path.exists():
        print(f"saved in {save_file}")
    else:
        print(f"{save_file} could not be downloaded, check url.")
# example
# from data import get_data
# get_data(filename="LiFePO4_supercell.cif")

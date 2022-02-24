#!/bin/bash
python -m venv my_env
source my_env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python -m ipykernel install --name=pyomo_tutorial
jupyter notebook MaxFlow_Abstract.ipynb


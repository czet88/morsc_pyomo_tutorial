#!/bin/bash
python -m venv my_env
if [[ "$OSTYPE" == "msys" ]]; then
	source ./my_env/Scripts/activate
else 
	source my_env/bin/activate
fi
pip install --upgrade pip
pip install -r requirements.txt
python -m ipykernel install --name=pyomo_tutorial
jupyter notebook MaxFlow_Abstract.ipynb


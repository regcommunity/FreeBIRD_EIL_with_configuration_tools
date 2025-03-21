#!/bin/bash
cd birds_nest
pip install --upgrade pip --quiet
python -m pip install django==5.1.3 --quiet
python -m pip install pyecore==0.15.1 --quiet
python -m pip install unidecode==1.3.8 --quiet
python manage.py runserver
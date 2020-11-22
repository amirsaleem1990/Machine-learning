#!/bin/bash
ipynb-py-convert EDA-by-column.py EDA-by-column.ipynb
jupyter nbconvert --to notebook --execute  EDA-by-column.ipynb --output EDA-by-column.ipynb
jupyter nbconvert --to html EDA-by-column.ipynb
gopen EDA-by-column.html
read -p "Press any key when you closed your Summary: "; rm -f EDA-by-column.{ipynb,html}
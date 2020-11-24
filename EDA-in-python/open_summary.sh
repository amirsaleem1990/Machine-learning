#!/bin/bash
ipynb-py-convert EDA-by-column.py EDA-by-column.ipynb
if [[ $? != 0 ]] ; then exit ; fi
jupyter nbconvert --to notebook --execute  EDA-by-column.ipynb --output EDA-by-column.ipynb
if [[ $? != 0 ]] ; then exit ; fi
jupyter nbconvert --to html EDA-by-column.ipynb
if [[ $? != 0 ]] ; then exit ; fi
gopen EDA-by-column.html
read -p "Press any key when you closed your Summary: "
echo -e "\nRemoving files EDA-by-column.{ipynb,html}.......... "
DEL -rf EDA-by-column.{ipynb,html}
if [[ $? == 0 ]] ; then
	echo -e "\nFiles removed Successfully\n"
fi
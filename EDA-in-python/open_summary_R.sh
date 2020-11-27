#!/bin/bash
cp Modeling.{R,py}
ipynb-py-convert Modeling.py Modeling.ipynb
./py-to-R.py
if [[ $? != 0 ]] ; then exit ; fi
jupyter nbconvert --to notebook --execute  Modeling.ipynb --output Modeling.ipynb
if [[ $? != 0 ]] ; then exit ; fi
jupyter nbconvert --to html Modeling.ipynb
if [[ $? != 0 ]] ; then exit ; fi
gopen Modeling.html
read -p "Press any key when you closed your Summary: "
echo -e "\nRemoving files Modeling.{ipynb,html}.......... "
DEL -rf DEL -rf Modeling.{ipynb,html}
DEL -rf Modeling.py
if [[ $? == 0 ]] ; then
	echo -e "\nFiles removed Successfully\n"
fi

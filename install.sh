#!/bin/bash

if [ -z "$VIRTUAL_ENV" ]; then
	VIRTUAL_ENV=env
	echo "VIRTUAL_ENV unset, setting to " $VIRTUAL_ENV
fi

python -m venv $VIRTUAL_ENV
source $VIRTUAL_ENV/Scripts/activate
pip install -r requirements.txt


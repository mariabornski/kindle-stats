#!/bin/bash

if [ -z "$VIRTUAL_ENV" ]; then
	VIRTUAL_ENV=env
	echo "VIRTUAL_ENV unset, setting to " $VIRTUAL_ENV
fi

rm -rf $VIRTUAL_ENV

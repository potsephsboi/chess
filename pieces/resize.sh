#!/bin/bash

cd black

for img in *
do
	convert -resize 101% $img $img
done

cd ..
cd white

for img in *
do
	convert -resize 101% $img $img
done


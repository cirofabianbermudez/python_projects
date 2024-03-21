#!/bin/bash

list=$(ls -1 ../images/*.png | sort -V)
magick convert $list output.pdf

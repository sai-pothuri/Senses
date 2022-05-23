#!/bin/sh

TEXT=$(tesseract $FILE_NAME stdout)
echo $TEXT
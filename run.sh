#!/bin/bash 


filename=$1
if [ -z $filename ]
then
	echo "help:"
	echo "		$0 filename_for_output"
	exit
fi
url=https://www.iana.org/assignments/service-names-port-numbers/
filename=service-names-port-numbers.csv
echo "downloading the file from $url$filename"
wget -q $url$filename -O $filename

echo "generate $filename"
python3 generate_service_port_json.py > $filename.json

echo "done!"
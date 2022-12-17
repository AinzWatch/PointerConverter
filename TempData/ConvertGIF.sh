#!/bin/bash

get_filename() {
	prefix=${1%/*} 
	resume=${1#"$prefix"}
	gif_name=${resume#/*}
	name=${gif_name%*.gif}
}

create_cursorfile(){
	Counter_image=0
	f=$(find . -name "image-*" -printf '%h\0%d\0%p\n' | sort -t '\0' -n | awk -F '\0' '{print $3}')
	for FILE in $f
	do
		echo "32 2 4 image-"$Counter_image".png 116" >> image.cursor
		Counter_image=$(( Counter_image + 1))
	done
	xcursorgen image.cursor "$name"
}

clean(){
	mv "$name" ../../Pointers
	cd ..
	rm -r "$name"
}
input="filepaths.txt" 
while IFS= read -r line
do
	get_filename "$line"
	mkdir -p "$name"
	cd "$name"
	convert "$line" -verbose -coalesce -resize 32x32 image.png
	create_cursorfile
	clean

done < "$input"


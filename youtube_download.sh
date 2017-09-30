#/bin/sh

echo $# $1 $2

if [ $# -eq 0 ]; then
	echo "Usage: $0 list_url output_file";
	exit 1;
fi

python ./youtube-list.py $1 | grep ^data-video-id | uniq | sed 's/data-video-id/python youtube-dl.py https:\/\/www.youtube.com\/watch?v/' > $2

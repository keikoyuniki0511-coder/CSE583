mkdir pronto
cd pronto
touch README.txt
echo "this is pronto data" > README.txt
mkdir data
cd data
curl -o open_data_year_one.zip https://s3.amazonaws.com/pronto-data/open_data_year_one.zip
unzip open_data_year_one.zip
head 2015_trip_data.csv

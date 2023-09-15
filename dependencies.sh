sudo apt-get update

#install python and pip
sudo apt install python3-pip

#install aws cli
sudo apt install unzip
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

#install python libraries
sudo pip install apache-airflow
sudo pip install pandas
sudo pip install requests
sudo pip install beautifulsoup4
sudo pip install lxml
sudo pip install html5lib
sudo pip install boto3
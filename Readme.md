### PM Project №2 step by step

##### 1. Launch EC2 instance on AWS
Create EC2 instance by this [Tutorial](https://catalog.workshops.aws/general-immersionday/en-US/basic-modules/10-ec2/ec2-linux)
Note the number of port, that set when we create security rule. We need it to specify it when launching docker. In tutorial it is port 80 for HTTP protocol.

##### 2. Install Docker and Docker Compose on EC2
Connect EC2 by SSH and run:
```commandline
sudo yum update -y
sudo amazon-linux-extras install docker
sudo service docker start
sudo systemctl enable docker
sudo usermod -a -G docker ec2-user
sudo reboot
```
Wait some time, while instance reboot and run:
```commandline
docker info
```
If something goes wrong, look this [Tutorial](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-container-image.html#create-container-image-install-docker) (click on **Installing Docker on Amazon Linux 2** there)
Install docker-compose
```commandline
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose version
```

##### 3. Clone this project to EC2 and launch API
Run
```commandline
git clone https://github.com/ispectre87/PM_Project_2.git
```
Go to EC2 Public IPv4 DNS, add **/hello** to it, you must see message.
Note, that protocol must be HTTP, link must be like **http://**bla-bla-bla.compute.amazonaws.com**/hello**.

##### 4. Connect API to S3

Roman must write something usefull here))

##### 5. Connect API to RDS with Postgres
Create database on RDS
In crud_server_app/.env write database credentials.


If you want to connect to RDS Postgres directly from EC2 terminal, install _psql_ on EC2:

Copy whole block, Enter
```commandline
sudo tee /etc/yum.repos.d/pgdg.repo<<EOF
[pgdg13]
name=PostgreSQL 13 for RHEL/CentOS 7 - x86_64
baseurl=https://download.postgresql.org/pub/repos/yum/13/redhat/rhel-7-x86_64
enabled=1
gpgcheck=0
EOF
```
Then
```commandline
sudo yum update
sudo yum install postgresql13 postgresql13-server
```
To connect to RDS Postgres run:
```commandline
psql --host=<your_host> --port=5432 --username=pm_user --dbname=pm_db
```
Now you can run SQL-commands directly to database


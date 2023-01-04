### PM Project №2 step by step

##### 1. Launch EC2 instance on AWS
Create EC2 instance by this [Tutorial](https://catalog.workshops.aws/general-immersionday/en-US/basic-modules/10-ec2/ec2-linux)
Note the number of port, that set when we create security rule. We need it to specify it when launching docker. In tutorial it is port 80 for HTTP protocol.

##### 2. Install all needed to EC2
```commandline
sudo yum update -y
sudo amazon-linux-extras install docker -y
sudo service docker start
sudo systemctl enable docker
sudo usermod -a -G docker ec2-user
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo yum update -y
sudo yum install git -y
git clone https://github.com/ispectre87/PM_Project_2.git
echo "@reboot docker-compose -f /home/ec2-user/PM_Project_2/docker-compose.yml up" > tmfl
sudo crontab < tmfl
docker version
docker-compose version
```

##### 4. Connect API to S3
###### Create an IAM instance profile:
1) Open the IAM console.
2) Choose **Roles**, and then choose **Create role**.
3) Select **AWS Service**, and then choose **EC2** under **Use Case**.
4) Select **Next**.
5) Select **Create policy**.
6) Choose **S3FullAccess** policy from list (or another needed policy)
7) Choose next and set name to policy.
8) Return to **Create role** and choose policy, which you created.
9) Select **Next**.
10) Enter a **Role name**, and then select **Create role**.
###### Attach the IAM instance profile to the EC2 instance 
1) Open the Amazon EC2 console.
2) Choose **Instances**.
3) Select the instance.
4) Choose the **Actions** tab, choose **Security**, and then choose **Modify IAM role**
###### Validate access to S3 bucket

Command for checking connection:
```commandline
aws s3 ls s3://<bucket_name>
```
You can see all files in the bucket. Note that, "pm-bucket-project" is the name of bucket.

##### 5. Connect API to RDS with Postgres
Create database on RDS
Don't connect it to EC2 instance, create security groups instead, one with inbound rules for database and other
for outbound rules for all instances and sources
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
psql --host=your_host --port=5432 --username=pm_user --dbname=pm_db
```
Now you can run SQL-commands directly to database

To update project credentials run:
```commandline
echo "DATABASE_LINK=<host> port=5432 dbname=<db_name> connect_timeout=10 user=<username> password=<password>
BUCKET_NAME=<bucket_name>
FILE_NAME=<file_name> > /Project_2_AWS/crud_server_app/.env
```
### PM Project №2 step by step

##### 1. Launch EC2 instance on AWS
Create EC2 instance by this [Tutorial](https://catalog.workshops.aws/general-immersionday/en-US/basic-modules/10-ec2/ec2-linux)
Note the number of port, that set when we create security rule. We need it to specify it when launching docker. In tutorial it is port 80 for HTTP protocol.

##### 2. Install Docker on EC2
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

##### 3. Clone this project to EC2 and launch API
Run
```commandline
git clone https://github.com/ispectre87/PM_Project_2.git
cd PM_Project_2
docker build -t project_2:v.0.1 .
docker run -p 80:8080 project_2:v.0.1 -t api
```
Go to EC2 Public IPv4 DNS, add **/hello** to it, you must see message.
Note, that protocol must be HTTP, link must be like **http://**bla-bla-bla.compute.amazonaws.com**/hello**.

##### 4. Connect API to S3

Roman must write something usefull here))

##### 5. Connect API to RDS with Postgres

Someone else must write something usefull here))
Test string
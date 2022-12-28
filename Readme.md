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

##### Clone this project to EC2
Run

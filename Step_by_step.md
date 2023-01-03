1. Create VPC with subnets
2. Create EC2, attach to EC2 role of S3FullAccess
3. Create S3_bucket
4. Create postgres database on RDS, don't connect to instance but allow all connections for Postgres type from anywhere. Create table **Users** in database.
5. Install all needed to EC2. Enter credentials. Add docker-compose up to crontab.
6. Generate [AMI](https://catalog.workshops.aws/general-immersionday/en-US/basic-modules/10-ec2/ec2-auto-scaling/ec2-auto-scaling/1-ec2-as#generate-a-custom-ami-of-the-web-server-created-in-the-ec2-linux-lab:)
7. Create a new [Security Group for our Auto Scaling Group](https://catalog.workshops.aws/general-immersionday/en-US/basic-modules/10-ec2/ec2-auto-scaling/ec2-auto-scaling/1-ec2-as#create-a-new-security-group-for-our-auto-scaling-group:) 
8. Creating a [Launch Template](https://catalog.workshops.aws/general-immersionday/en-US/basic-modules/10-ec2/ec2-auto-scaling/ec2-auto-scaling/2-ec2-as#creating-a-launch-template)
9. [Create Auto Scaling Group](https://catalog.workshops.aws/general-immersionday/en-US/basic-modules/10-ec2/ec2-auto-scaling/ec2-auto-scaling/3-ec2-as#create-auto-scaling-group)
10. [Creating a Load Balancer Security Group](https://catalog.workshops.aws/general-immersionday/en-US/basic-modules/10-ec2/ec2-auto-scaling/ec2-auto-scaling/4-ec2-as#creating-a-load-balancer-security-group)
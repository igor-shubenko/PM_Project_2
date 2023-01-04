1. Create VPC with public subnets
2. Create EC2, attach to EC2 role of S3FullAccess
3. Create S3_bucket
4. Create postgres database on RDS. Don't connect it to EC2 instance, create security groups instead, one with inbound rules for database and other
for outbound rules for all instances and sources. 
5. Install all needed to EC2. Enter credentials. Add docker-compose up to crontab. In crud_server_app/.env write database credentials.
6. Generate [AMI](https://catalog.workshops.aws/general-immersionday/en-US/basic-modules/10-ec2/ec2-auto-scaling/ec2-auto-scaling/1-ec2-as#generate-a-custom-ami-of-the-web-server-created-in-the-ec2-linux-lab:)
7. Create a new [Security Group for our Auto Scaling Group](https://catalog.workshops.aws/general-immersionday/en-US/basic-modules/10-ec2/ec2-auto-scaling/ec2-auto-scaling/1-ec2-as#create-a-new-security-group-for-our-auto-scaling-group:) 
8. Creating a [Launch Template](https://catalog.workshops.aws/general-immersionday/en-US/basic-modules/10-ec2/ec2-auto-scaling/ec2-auto-scaling/2-ec2-as#creating-a-launch-template). In launch template security group select our Auto_Scalling_SG. Dont include subnet in launch template.
9. [Create Auto Scaling Group](https://catalog.workshops.aws/general-immersionday/en-US/basic-modules/10-ec2/ec2-auto-scaling/ec2-auto-scaling/3-ec2-as#create-auto-scaling-group)
    - during creation ASG create Application Load Balancer. Load balancer scheme: Internet-facing
      - create target group
10. [Creating a Load Balancer Security Group](https://catalog.workshops.aws/general-immersionday/en-US/basic-modules/10-ec2/ec2-auto-scaling/ec2-auto-scaling/4-ec2-as#creating-a-load-balancer-security-group). Balancer SG should allow traffic to Auto_scalling_sg. ASG should allow inbound traffic from balancer.
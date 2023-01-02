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
###### Create an IAM instance profile:
1) Open the IAM console.
2) Choose **Roles**, and then choose **Create role**.
3) Select **AWS Service**, and then choose **EC2** under **Use Case**.
4) Select **Next**.
5) Select **Create policy**.
6) Choose **JSON** and enter:
```commandline
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket"
            ],
            "Resource": "arn:aws:s3:::pm-bucket-project"
        },
        {
            "Action": [
                "s3:DeleteObject",
                "s3:GetObject",
                "s3:PutObject",
                "s3:PutObjectAcl"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:s3:::pm-bucket-project/*"
        }
    ]
}
```

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
1) Install the AWS CLI on your EC2 instance.
```commandline
sudo apt-get update 
sudo apt-get install -yy less
sudo apt-get install curl
sudo apt-get install unzip
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```
2) Enter following command:
```commandline
aws s3 ls s3://pm-bucket-project
```
You can see all files in the bucket. Note that, "pm-bucket-project" is the name of bucket.
##### 5. Connect API to RDS with Postgres

Someone else must write something usefull here))
Test string
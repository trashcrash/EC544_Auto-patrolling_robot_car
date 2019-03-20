# Set the environment for AWS rekognition
## Prepare the AWS console
### Add a user
**1.** After logging in your AWS console, find and click "IAM" in "services" dropdown menu</br></br>
<img src="https://github.com/trashcrash/EC544_Auto-patrolling_robot_car/blob/master/Rekognition/images/IAM.jpeg"></br></br>
**2.** Click users on the left, and fill the blanks with your user's name and password</br></br>
<img src="https://github.com/trashcrash/EC544_Auto-patrolling_robot_car/blob/master/Rekognition/images/AddUser_1.png"></br></br>
**3.** Attach the policies, including three existing policies and one custom policy. The three existing policies can be selected from the policies listed below: "AmazonS3FullAccess" (for AWS cloud storage), "AmazonRekognitionFullAccess" (for rekognition) and "AmazonSNSFullAccess" (for messages). </br></br>
<img src="https://github.com/trashcrash/EC544_Auto-patrolling_robot_car/blob/master/Rekognition/images/AddUser_2.png"></br></br>
**4.** A new policy should be created. Click "create policy" and edit the policy as the follows. </br></br>
<img src="https://github.com/trashcrash/EC544_Auto-patrolling_robot_car/blob/master/Rekognition/images/AddUser_3.png"></br></br>
**5.** Name the policy as AddRole (or any name you like)</br></br>
<img src="https://github.com/trashcrash/EC544_Auto-patrolling_robot_car/blob/master/Rekognition/images/AddUser_4.png"></br></br>
**6.** Next, move to the review page. It should look like this</br></br>
<img src="https://github.com/trashcrash/EC544_Auto-patrolling_robot_car/blob/master/Rekognition/images/AddUser_5.png"></br></br>
**7.** The user is created after you've done your review. Don't forget to download the credentials. </br></br>
<img src="https://github.com/trashcrash/EC544_Auto-patrolling_robot_car/blob/master/Rekognition/images/AddUser_6.png"></br></br>
### Download and configure AWS CLI
AWS Command Line Interface(CLI) is downloaded for simplifying the configuration process. This part is optional, but you need to set things up manually otherwise. </br>
Install AWS CLI: ```$ pip install awscli --upgrade --user``` </br>
Before the configuration, there's information needed. Go to AWS console -> IAM -> users, click your username and open "security credentials" tag</br></br>
<img src="https://github.com/trashcrash/EC544_Auto-patrolling_robot_car/blob/master/Rekognition/images/Access_Key.png"></br></br>
Click "create access key" and download the csv file generated. </br>
Now you can open your terminal and enter ```aws configure``` </br>
The access key ID and secret access key are in the csv file you just downloaded. The region format is like "us-east-1", find your region and enter correspondingly. The default output format can be "json", "text" or "table". Here we choose "json".
### Create a role for SNS
A role is needed to publish messages. Find and enter "role" in IAM, create a new role, and choose SNS service. </br></br>
<img src="https://github.com/trashcrash/EC544_Auto-patrolling_robot_car/blob/master/Rekognition/images/AddRole_1.png"></br></br>
Continue with the default settings, and enter the role name. </br></br>
<img src="https://github.com/trashcrash/EC544_Auto-patrolling_robot_car/blob/master/Rekognition/images/AddRole_2.png"></br></br>
### Create SNS topic
The SNS service needs a topic to publish messages. Find and click "Simple Notification Service" in "services" dropdown menu, and create a topic. </br></br>
<img src="https://github.com/trashcrash/EC544_Auto-patrolling_robot_car/blob/master/Rekognition/images/CreateSNSTopic_1.png"></br></br>
Continue with the default settings, and enter the topic name. </br></br>
<img src="https://github.com/trashcrash/EC544_Auto-patrolling_robot_car/blob/master/Rekognition/images/CreateSNSTopic_2.png"></br></br>
### Activate AWS S3 buckets
The test videos have to be uploaded to a bucket for Rekognition to analyze. Find S3 in "services" and create a bucket. </br></br>
<img src="https://github.com/trashcrash/EC544_Auto-patrolling_robot_car/blob/master/Rekognition/images/CreateBucket_1.png"></br></br>
### Get the arns
Two arns are needed to start Rekognition service. Your role arn can be found at IAM -> Roles -> "Your role name". </br></br>
The SNS topic arn can be found at Simple Notification Service -> Topics -> "Your topic name". </br></br>
### Start rekognition
The sample codes are provided here. </br>
Before you execute the code, make sure you have AWS python SDK "boto3" installed. </br>
Simply use pip in your terminal: ```pip install boto3```</br></br>
```upload.py``` uploads your video or picture in the current directory to your bucket. </br>
```start_reko.py``` starts the rekognition service. If success, it will return a **JobId**. Copy this value. </br>
Paste the JobId to ```get_result.py```, and the result is saved in json format. </br>
**Note that you need to replace some of the values in the files with your own values (bucket name, arns, video name, etc.)**

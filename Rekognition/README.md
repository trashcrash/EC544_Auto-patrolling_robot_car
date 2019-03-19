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
A role is needed to publish messages. Find and enter "role" in IAM, create a new role, and choose SNS service. </br>

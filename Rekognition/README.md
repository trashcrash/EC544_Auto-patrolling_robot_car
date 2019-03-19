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

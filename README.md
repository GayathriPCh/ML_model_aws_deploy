# ML_model_aws_deploy
Firstly make sure to have model.pkl file by running the given jupyter notebook. 
![image](https://github.com/user-attachments/assets/150c9f81-aedd-4f01-b453-cc4e1139152f)

### Step 1: Launch EC2 Instance
1. Log in to the AWS Console.
2. Go to EC2 Dashboard by searching for "EC2" in the search bar.
3. Click "Launch Instance".
4. Choose Ubuntu Server 20.04 LTS as your AMI (Amazon Machine Image).
5. Configure security groups to allow HTTP (port 80) and SSH (port 22).
6. Click Launch and download the key pair (`placement.pem`).

![image](https://github.com/user-attachments/assets/22c2346f-370c-4689-beca-4888685dc88d)
![image](https://github.com/user-attachments/assets/d3bdbf85-4f24-4f36-a31d-0cb76edff10a)
![image](https://github.com/user-attachments/assets/ba3423a4-5c91-407c-aa6c-efcc61caa3c6)
![image](https://github.com/user-attachments/assets/a38259ed-084e-4979-a2bd-454eefeb6dfa)

7. Click on "Create New Key Pair".

![image](https://github.com/user-attachments/assets/620cf2d8-5150-44b1-9691-f8608f7a58e0)
![image](https://github.com/user-attachments/assets/307db7f0-7aff-44c0-bc6a-5870852ef9cc)
![image](https://github.com/user-attachments/assets/86dd566b-b368-49b8-858b-8fe3e5438c4a)
![image](https://github.com/user-attachments/assets/e7901609-c36d-4849-af33-2b9423044a04)
![image](https://github.com/user-attachments/assets/520c47b2-4005-4417-8dfa-09718897152d)
![image](https://github.com/user-attachments/assets/f2f6a630-6d98-4f87-bae3-91131e0fbd0d)

### Step 2: Connect to Your EC2 Instance
1. In your AWS console, go to the EC2 Dashboard.
2. Select your instance (as shown in Image 2) and click **Connect**.
3. In the "Connect" tab, select the SSH client option (as seen in Image 3).
4. Copy the SSH command provided:
   
   ```bash
   ssh -i "placement.pem" ubuntu@ec2-18-208-232-118.compute-1.amazonaws.com
   ```

![image](https://github.com/user-attachments/assets/1985c7e0-dbc1-4096-8a2c-82dbda032362)
![image](https://github.com/user-attachments/assets/df70c808-cabb-468f-be22-99d648b643ce)
Paste the copied command on git bash. It will enable ubuntu environment, by connecting Ec2 
![image](https://github.com/user-attachments/assets/c9294d40-10a5-4cef-8861-8267338fda10)
![image](https://github.com/user-attachments/assets/16c2f65a-ae2a-4aed-80a5-ff16b61b6d08)
![image](https://github.com/user-attachments/assets/5f727f1a-27d2-48a1-9b23-f38c1e6e2ce5)
![image](https://github.com/user-attachments/assets/451a88e8-b4f0-474e-9450-5677de955257)
![image](https://github.com/user-attachments/assets/603209db-0282-4dd8-9059-d9dc08050293)
![image](https://github.com/user-attachments/assets/6583c4ea-b257-498a-8759-47dc8c23b4f9)
![image](https://github.com/user-attachments/assets/df4ac47c-46db-4dc4-9871-f223b07c8790)
![image](https://github.com/user-attachments/assets/b1630b93-ff40-49d2-abde-d043b2013e1c)

Now open the normal git bash in a new terminal, and paste the following command to transfer files from local to the ec2 environment via WinSCP. 
If your project folder is located at `C:\Users\YourName\Desktop\flask-app`, the command would look like this:


![image](https://github.com/user-attachments/assets/8e06702d-1e07-42b4-8350-0c166d19fe4c)
![image](https://github.com/user-attachments/assets/7dc42364-8413-497d-88a3-ad9c4b6eb92e)

![image](https://github.com/user-attachments/assets/ad1b83e9-5731-4422-8d47-5e5745fa5f05)
```

Let me know if you'd like to adjust anything!

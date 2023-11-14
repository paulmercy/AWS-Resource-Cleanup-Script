# AWS-Resource-Cleanup-Script
This script utilizes the Boto3 library to clean up various AWS resources, including EC2 instances, S3 buckets, IAM users, and RDS instances. Be cautious when running this script, as it will irreversibly delete resources.

## Prerequisites
- Python installed on your machine
- Boto3 library installed (`pip install boto3`)

## Usage
1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/aws-resource-cleanup.git

2. Change into the project directory:

   ```bash
   cd aws-resource-cleanup

3. Open the script file (`cleanup_script.py`) and replace the placeholder values for `YOUR_ACCESS_KEY` and `YOUR_SECRET_KEY` with your AWS credentials.
4. Run the script:
   
   ```bash
   python cleanup_script.py

## Important Note
This script will delete all EC2 instances, S3 buckets, IAM users, and RDS instances in the specified AWS region. Ensure that you have backed up any essential data and have confirmed your intention to delete these resources.

## Disclaimer
Use this script at your own risk. The author is not responsible for any accidental deletion of critical resources. Always review and understand the script before running it in a production environment.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

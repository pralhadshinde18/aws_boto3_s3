import boto3

# s3 = boto3.resource('s3')
# s3.meta.client.download_file('pralhadbucket18', 'gitfiledata', '/home/pralhad/Documents/git.txt')

s3 = boto3.client('s3')
s3.download_file('pralhadbucket18', 'gitfiledata', '/home/pralhad/Documents/git.txt')

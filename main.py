from boto3.session import Session

ACCESS_KEY = '******'
SECRET_ACCESS_KEY = '********'

session = Session(aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_ACCESS_KEY)

s3 = session.resource('s3')
bucket = 'bucket-p18'
my_bucket = s3.Bucket(bucket)
# print(my_bucket)

#to check which object are available in bucket
# for s3_files in my_bucket.objects.all():
#     print(s3_files.key)


#object upload to

# file_to_be_uploaded = '/home/pralhad/Documents/git.txt'
# object_name = 'gitfile'
# my_bucket.upload_file(file_to_be_uploaded,object_name)
#
#
# for s3_files in my_bucket.objects.all():
#     print(s3_files.key)
#     print('object is uploaded')


#delete object

key = 'wallpaperflare.com_wallpaper.jpg'

my_bucket.delete_objects(Delete={'Objects': [{'Key': key}]})

from django.shortcuts import render
from django.http import HttpResponse
from django.http import QueryDict
import smtplib
from email.mime.text import MIMEText
from django.http import HttpResponse, JsonResponse
# import uuid
# import boto3
# from boto3.dynamodb.conditions import Attr

# # DynamoDB Cursor
# db = boto3.resource(service_name = 'dynamodb',region_name = 'us-east-1', #,endpoint_url="http://localhost:8000"
    # aws_access_key_id = 'AKIA6EW7VDYX7MWK3X26',
    # aws_secret_access_key = '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')

# # Test DynamoDB
# def dynamoTest(request):
#     data = {
#         "docId":uuid.uuid4().hex,
#         "aList":['I','am','a','list']
#     }
#     db.Table('test_one').put_item(Item = data)
#     return JsonResponse({'status':'success'})

# Home page
def home(request):
    return render(request, 'index.html')
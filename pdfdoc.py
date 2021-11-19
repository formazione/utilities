#pdfdoc

# pip install cloudmersive-convert-api-client

from __future__ import print_function
import time
import cloudmersive_convert_api_client
from cloudmersive_convert_api_client.rest import ApiException
from pprint import pprint
# Configure API key authorization: Apikey
configuration = cloudmersive_convert_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'
# create an instance of the API class
api_instance = cloudmersive_convert_api_client.ConvertDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = 'ALL.pdf' # file | Input file to perform the operation on.
try:
	# Convert PDF to Word DOCX Document
	api_response = api_instance.convert_document_pdf_to_docx(input_file)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ConvertDocumentApi->convert_document_pdf_to_docx: %s\n" % e)
from instamojo_wrapper import Instamojo
from django.conf import settings



if settings.IS_UNDER_DEVELOPMENT == True: 
     instamojo_api = Instamojo(api_key=INSTAMOJO_PRIVATE_TEST_API_KEY,auth_token=INSTAMOJO_PRIVATE_TEST_AUTH_TOKEN)
 else: 
     instamojo_api = Instamojo(api_key=settings.INSTAMOJO_PRIVATE_LIVE_API_KEY,auth_token=settings.INSTAMOJO_PRIVATE_LIVE_AUTH_TOKEN)
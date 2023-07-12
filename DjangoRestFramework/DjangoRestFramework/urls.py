from django.contrib import admin
from django.urls import path, include
from DjangoRestFramework.views import TesView

from rest_framework.authtoken.views import obtain_auth_token #built in view that we dont have to create

urlpatterns = [
  path('admin/', admin.site.urls),
  path('api-auth/', include('rest_framework.urls')),
  path('', TesView.as_view(), name='test'),
  path('api/token/', obtain_auth_token, name='obtain')
]

#mkvirtualenv name
#pip install djangorestframework

'''
For Python 3.3 or newer, Commands for installing, creating and activate virtual environment has been changed.
For creating new environment:
py -m venv myapp              
To activate your virtual environment:
.\myapp\Scripts\activate
'''

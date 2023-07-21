from rest_framework import serializers
from account.models import *

# create serailizers here

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models=Users
        feilds = "__all__"

class UserAddresse(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = UserAddresses
        feilds = "__all__"
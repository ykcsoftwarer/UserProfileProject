from rest_framework import serializers
from .models import UserProfile



# class UserProfileSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = UserProfile
#         fields = (
#             'id',
#             'username',
#             ' first_name ',
#             'last_name ',
#             'age ',
#             ' bio ',
#             'register_date ',
#         )
        

class UserProfileSerializer(serializers.ModelSerializer):
    
    born_year = serializers.SerializerMethodField()  # read_only
    path = serializers.StringRelatedField() # read_only
    path_id = serializers.IntegerField()
    
    class Meta:
        model = UserProfile
        # fields = "__all__"
        fields = (
            
            'username',
            'first_name',
            'last_name ',
            'age',
            'bio',
            'register_date ',
        )
        
    
    def get_born_year(self, obj):
        import datetime
        current_time = datetime.datetime.now()
        return current_time.year - obj.age
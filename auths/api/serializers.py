from auths.models import CustomUser 
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    
    class Meta:
        model = CustomUser 
        fields = ["id", "email", "password", "password2", "is_employer"]
        extra_kwargs = {
            "password": {"write_only": True}
        }
        
    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("The two passwords do not match !")
        return data 
    
    def create(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]
        confirm_account = CustomUser.objects.filter(email=email)
        if confirm_account.exists():
            raise serializers.ValidationError("An account already exists with this email")
        new_account = CustomUser.objects.create_user(email=email, password=password)
        return new_account
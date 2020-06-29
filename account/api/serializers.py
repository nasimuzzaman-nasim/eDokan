from rest_framework import serializers
from account.models import UserProfile, BaseAccount


class BaseAccountSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = BaseAccount
        fields = [
            'username',
            'email',
            'check_staff',
            'staff_id',
            'password',
            'password2',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):

        account = None
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        check_staff = self.validated_data['check_staff']

        if password != password2:
            raise serializers.ValidationError({
                'password': 'password doesn\'t match!'
        })

        if check_staff:
            staff_id = self.validated_data['staff_id']
            if staff_id == '1000':
                account = BaseAccount(
                    username = self.validated_data['username'],
                    email = self.validated_data['email'],
                    check_staff = True,
                    staff_id = staff_id,
                    is_staff = True,
                )
            else:
                raise serializers.ValidationError({'staff_id': 'Staff ID isn\'t valid!'})
        else:
            account = BaseAccount(
                username = self.validated_data['username'],
                email = self.validated_data['email'],
            )
        
        account.set_password(password)
        account.is_active = True #------------------------------------- NEED TO CHHANGE -----------------------------
        account.save()
        profile = UserProfile(base=account)
        profile.save()
        return account

        


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'dp',
            'first_name',
            'last_name',
            'balance',
            'delivery_address',
            'contact_no',
        ]

        extra_kwargs = {
            'balance': {'read_only': True}
        }
        # fields = '__all__'


import imghdr

import requests
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

User = get_user_model()


class FacebookBackend:
    api_base = 'https://graph.facebook.com/v3.2'
    api_me = f'{api_base}/me'

    def authenticate(self, access_token):
        params = {
            'access_token': access_token,
            'fields': ','.join([
                'id',
                'first_name',
                'last_name',
                'picture.type(large)',
            ]),
        }

        response = requests.get(self.api_me, params)
        data = response.json()
        print(data)
        facebook_id = data['id']
        first_name = data['first_name']
        last_name = data['last_name']
        url_img_profile = data['picture']['data']['url']

        img_response = requests.get(url_img_profile)
        img_data = img_response.content

        ext = imghdr.what('', h=img_data)

        f = SimpleUploadedFile(f'{facebook_id}.{ext}', img_response.content)

        try:
            user = User.objects.get(username=facebook_id)
            user.last_name = last_name
            user.first_name = first_name
            user.save()

        except User.DoesNotExist:
            user = User.objects.create_user(
                username=facebook_id,
                first_name=first_name,
                last_name=last_name,
                img_profile=f,
            )

        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
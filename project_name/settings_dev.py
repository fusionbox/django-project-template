DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '{{ project_name }}',
        'USER': '{{ project_name }}_user',
    }
}

from fabric.api import env, roles

from fusionbox.fabric import fb_env
from fusionbox.fabric.django import stage, deploy

# env.roledefs['live'] = ['fusionbox@{{ project_name }}.com']

fb_env.project_name = '{{ project_name }}'

stage = roles('dev')(stage)

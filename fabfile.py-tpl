from fabric.api import env, roles

from fusionbox.fabric.django.new import stage, deploy


def dev():
    env.project_name = '{{ project_name }}.dev'
    env.vassal_name = '{{ project_name }}_dev'

    return ['fusionbox@{{ project_name }}.dev.fusionbox.com']


# def live():
#     env.project_name = '{{ project_name }}.com'
#     env.vassal_name = '{{ project_name }}_com'

#     return ['fusionbox@demo.{{ project_name }}.com']


env.roledefs['dev'] = dev
#env.roledefs['live'] = live

stage = roles('dev')(stage)
#deploy = roles('live')(deploy)

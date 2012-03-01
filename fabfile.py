from fusionbox.fabric_helpers import *

env.roledefs = {
        'dev': ['dev.fusionbox.com'],
        }

env.project_name = '{{ project_name }}'
env.short_name = '{{ project_name }}'

stage = roles('dev')(stage)

command = '/home/debian/projects/venv/bin/gunicorn'
pythonpath = '/home/debian/projects/venv/bistro_site/'
bind = '0.0.0.0:8001'
workers = 5
user = 'debian'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=bistro_site.settings'

source /home/debian/projects/venv/bin/activate    
exec gunicorn -c "/home/debian/projects/venv/bistro_site/gunicorn_config.py" bistro_site.wsgi 

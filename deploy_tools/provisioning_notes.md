##Required packages
* nginx
* Python3
* Git
* pip
* virtualenv

## Nginx vritual host config

* see nginx.template.conf
* replace SITENAME with your site 
```
# sed  s/SITENAME/pokuslol.tk/ nginx.template.conf > /etc/nginx/sites-available/pokus.tk
```

##Upstart job
* see gunicorn-upstart.template.conf
* replace SITENAME with your site
```
# sed  s/SITENAME/pokuslol.tk/ gunicorn-upstart.template.conf > /etc/init/gunicorn-pokuslol.tk.conf
```
##Folder structure
Assume we have a user at /home/username

	/home/username
	└── sites
    	└── SITENAME
        	 ├── database
        	 ├── source
        	 ├── static
         	 └── virtualenv
    

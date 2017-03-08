Update your no-ip.com domain name through crontab
=================================================

What does it do?
------------------

Run the script to update your IP on no-IP. I suggest running it using cron.

Installation
------------

*Requirements
This little script requires the ``requests`` python module from http://docs.python-requests.org/en/latest/

.. code-block:: bash

	git clone git@github.com:jonwedell/update-noip.git
	
	cd update-noip
	
	pip3 install -r requirements.txt
	

Configuration
=============

The script
----------

1. Clone the script

.. code-block:: bash
	
	git clone git@github.com:jonwedell/update-noip.git

2. Edit the script with your username, password, hostname and ip addresses bag.

.. code-block:: pycon
	
	HOSTNAME = "yourhostname.no-ip.com"
	USERNAME = "username"
	PASSWORD = "password" 

Execution
---------
To run the script once you edited the parameters.

.. code-block:: bash
	
	python3 update_noip.py

Crontab
-------

.. code-block:: bash

	@hourly   /usr/bin/python3 /<path_to_python_script>/update_noip.py >> /dev/null 2>&1



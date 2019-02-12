# Nice Redfish

## Context

As a Product Manager in a IaaS company, and with no formal computer science education or training, I always relied on self teaching to improve my technical skills. I decided to initiate this project to use as a guideline and a logbook for my experiments. Each "target" will be documented in this file, and code will be stored in a separate folder of this repo.

I aim at improving my coding skills, my knowledge of git, SQL, tests, integration and deployment with the modern toolbox of any DevOps.

If you enjoy the reading or want to comment about my implementation and/or propose new solution, feel free to do so. I firmly believe that constructive criticism and peer review are the best tools for self-improvement.

### Objectives

Improve understanding of my co-workers field and my customer expectations.

Develop and iterate a "simple" application to deploy and operate in an increasing level of feature, quality control and automation.

### Functional design

Web server with API that respond to a first name as a parameter.
Basic Error handling must be implemented.

### Technical stack

List will expand with the project life.

- Python 3.7
- Flask
- Gunicorn
- SQLite
- Supervisor
- NGINX
- letsencrypt
- Cronjob

## Step 1

- Simple python webserver that answer to the query parameter
- Implement logging
- Implement testing

I underestimated the time and complexity to prepare a simple python server "as production ready as possible".
I will investigate and setup automated deployment with wsgi for the next steps.

## Step 2

- Store request and IP of origin for different behavior:
  - _'Nice to meet you'_ for the first request (name, source ip)
  - _'Hello again'_ the next times
- Add Ansible deployment for the server (CentOS)
  - .ansible.cfg contains:
    > [defaults]\
    > host_key_checking = False
- Setup Supervisor for autostart/restart as a service
- Implement functionnal testing (will be carried over)

Fedora and Ansible do not work very well together so I switched to CentOS 7 (on which I have more experience)
uWSGI will be implemented alongside NGINX and SSL certificate.

Next steps might need infrastructure automated deployment.

## Step 3

- DB entries have 1hr lifetime (redfish has short memory)
- Deployed with ssl certificate (letsencrypt), nginx and wsgi(gunicorn). On this point I needed to confront myself to SELINUX (which I'm not familiar with, and not easy to debug). I need to investigate
- Moved *fake* template to actual files in ansible directories

It seems that lifetime management might only be ok with a cronjob. I explored event (mysql) and trigger (posgre) but with no satisfaction. Crontab is now deployed and activated through configuration management.
I did not used letsencrypt ansible module due to lack of understanding of the module behavior and I prefered call certbot shell command directly.

## Step 4

- Package python application (rolled back)
- Proxy converted from port to local socket
- Test to check deployed SSL certificate
- Freeze for release

I spent an incredible amount of time debugging packaging, path to files to include. My conclusion is when shipping an application, I should not package it except if it meant to be used as an import/dependency. Standalone application is meant to be in /opt/.
Fun fact, if you want to use nginx after certbot, you must start it beforehad or it wont be callable by systemd (Thanks to a long github bug report thread)
The --test-cert or --staging parameter does not provide a root CA that can be tested in the last test, so I removed it alltogether. Every run now deploy a fully-fledge SSL certificate.

### Topics to investigate

- SELINUX
- CI/CD
- CONTAINER
- SERVERLESS
- SALT
- TERRAFORM
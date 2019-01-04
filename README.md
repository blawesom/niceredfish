# Nice Redfish
## Context:
As a Product Manager in a IaaS company, and with no formal computer science education or training, I always relied on self teaching to improve my technical skills. I decided to initiate this project to use as a guideline and a logbook for my experiments. Each "target" will be documented in this file, and code will be stored in a separate folder of this repo.

I aim at improving my coding skills, my knowledge of git, SQL, tests, integration and deployment with the modern toolbox of any DevOps.

If you enjoy the reading or want to comment about my implementation and/or propose new solution, feel free to do so. I firmly believe that constructive criticism and peer review are the best tools for self-improvement.

### Objectives:
Improve understanding of my co-workers field and my customer expectations.

Develop and iterate a "simple" application to deploy and operate in an increasing level of feature, quality control and automation.

### Functional design:
Web server with API that respond to a first name as a parameter.
Basic Error handling must be implemented.

### Technical stack:
List will expand with the project life.
- Python 3.7
- Flask
- SQLite

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
  - Store only 1hr of requests (redfish has short memory)
- Add Ansible deployment for the server (CentOS)
- Setup Supervisor for autostart/restart as a service
- Implement functionnal testing (will be carried over)

Fedora and Ansible do not work very well together so I switched to CentOS 7 (on which I have more experience)
uWSGI will be implemented alongside NGINX and SSL certificate.

Next steps might need infrastructure setup as well.
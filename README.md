# KokiPay Billing System

This application is adapted from Silver, a billing system build by www.presslabs.com. You can see the  original readme message below.

The purpose of this adaptation is to make the system compatible for hosting the WebODM project in a SaaS environment. This SaaS-based WebODM project is called Koki. Koki is Django-based as well, and therefore the synergy in technology made it a natural choice.

This adaptation is made available under the same terms as the original Silver project with the Apache license, viewable at the repository home.

# Build Modifications

The first changes necessary were to configure Silver into the Koki environment, which includes Docker and PostgreSQL. There were several places where MySQL assumptions had to be modified. In this process, Celery task management was also integrated and Redis replaced RabbitMQ. Numerous package conversion incompatibilities were encountered. Therefore the build files were modified to accommodate these requirements and issues.

In addition, issues with static file collection affected the proper user interface, and these needed to be corrected too.

The target system tested was Ubuntu 22.04. No other platforms have been tested.
Docker version 26.1.3 was used.

## Build
```%docker-compose build

## Docker Startup
```docker-compose up -d
docker-compose start

## Full Shutdown
```docker-compose down

## Rebuilding After Source Modifications

To rebuild after making modifications to existing top-level or silver files, or new files in the silver directory, follow these steps:
1) Full shutdown
2) Build
3) Docker startup

# Original Presslabs Readme File

## [silver](https://www.presslabs.com/code/silver/)

[![Build Status](https://ci.presslabs.net/api/badges/silverapp/silver/status.svg?ref=refs/heads/master)](https://ci.presslabs.net/silverapp/silver)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fsilverapp%2Fsilver.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fsilverapp%2Fsilver?ref=badge_shield)

**A Django automated billing system with a REST API.**

Silver was developed by the awesome engineering team at
[Presslabs](https://www.presslabs.com/), a Managed WordPress Hosting
provider.

For the complete installation and configuration guide, check the [Silver Docs](https://www.presslabs.com/code/silver/).

For more open-source projects, check [Presslabs Code](https://www.presslabs.com/code/).

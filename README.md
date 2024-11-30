# zabbix-netskope

Zabbix Template for Netskope API Rest V2 

## Description

This template get information about Netskope from Netskope API Rest V2.

## Templates 

- **Template Netskope Publishers API Rest V2** 

## Netskope Tenant API Permissions

|Template|API Endpoint|Permissions|
|-|-|-|
|Template Netskope Publishers API Rest V2|`/api/v2/infrastructure/publishers`|Read|


## Configuration

Create a Host and assign template **Template Netskope Publishers API Rest V2** with one interface Agent (127.0.0.1) and set macros value

|Macro|Value|Description|
|-|-|-|
|`{$NETSKOPE.TENANTURL}`|https://mytenant.eu.goskope.com|Base URL of your Netskope tenant|
|`{$NETSKOPE.APITOKEN}`|`xxxxxxxxxxxxxxxxxxxxxx`|API Token Generated on Netskope tenant|

## Discovery

Template will execute a discovery on Publishers API endpoint every 1h create items for each Publisher.

![screenshot](images/Netskope-Publisher-Discovery.png)

## Item Prototypes

- Autoupgrade enabled
- DTLS support
- EEE Support
- IP Address
- Latency
- LBrokerConnect
- nwa ba
- Registered
- Status
- Stitcher POP
- Upgrade error code
- Upgrade error detail
- Upgrade requested
- Upgrade status
- Version
- Version string

![screenshot](images/Netskope-Publisher-ItemsPrototype.png)


## Trigger Prototypes

|Trigger|Severity|
|-|-|
|Publisher \[{#NETSKOPE.PUBLISHER.NAME}\] Autoupgrade changed|Warning|
|Publisher \[{#NETSKOPE.PUBLISHER.NAME}\] DTLS Support changed|Informational|
|Publisher \[{#NETSKOPE.PUBLISHER.NAME}\] EEE Support changed|Informational|
|Publisher \[{#NETSKOPE.PUBLISHER.NAME}\] IP Address changed|Informational|
|Publisher \[{#NETSKOPE.PUBLISHER.NAME}\] Latency is high|Warning|
|Publisher \[{#NETSKOPE.PUBLISHER.NAME}\] No data on last 20m|Disaster|
|Publisher \[{#NETSKOPE.PUBLISHER.NAME}\] not connected|High|
|Publisher \[{#NETSKOPE.PUBLISHER.NAME}\] outdated (min version accepted v{$NETSKOPE.PUBLISHER.MIN_VERSION})|Warning|
|Publisher \[{#NETSKOPE.PUBLISHER.NAME}\] upgrade error|Warning|

![screenshot](images/Netskope-Publisher-TriggerPropotype.png)

## Publisher example

![screenshot](images/Netskope-Publisher-Items-Example.png)
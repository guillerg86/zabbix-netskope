# zabbix-netskope

Zabbix Template for Netskope API Rest V2 


## Description

This template get information about Netskope from Netskope API Rest V2.

## Templates (under development)
- **Template Netskope Publishers API Rest V2**: 

## Netskope Tenant API 

|API Endpoint|Permissions|
|-|-|
|`/api/v2/infrastructure/publishers`|Read|


## Configuration

Create a Host and assign template **Template Netskope Publishers API Rest V2** with one interface Agent (127.0.0.1) and set macros value

|Macro|Value|Description|
|-|-|-|
|`{$NETSKOPE.TENANTURL}`|https://mytenant.eu.goskope.com|Base URL of your Netskope tenant|
|`{$NETSKOPE.APITOKEN}`|`xxxxxxxxxxxxxxxxxxxxxx`|API Token Generated on Netskope tenant|

## Discovery

Template will execute a discovery on Publishers endpoint each 1h and create items for each Publisher.


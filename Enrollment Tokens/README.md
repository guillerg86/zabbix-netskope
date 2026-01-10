# Netskope Enrollment Tokens Monitoring for Zabbix

This repository provides a Zabbix template to monitor **Netskope Enrollment Tokens** using the **Netskope REST API**, allowing visibility into token status, usage and expiration.

---

## 🧩 Template Overview

### 🔑 Template Netskope Enrollment Tokens by HTTPS.yaml

This template:

- Uses the **Netskope REST API** to retrieve enrollment tokens.
- Discovers all available enrollment tokens.
- Creates monitoring items and triggers per token.
- Is designed to minimize API usage while keeping token information up to date.
- Removes the fields auth_token & encrypt_token for security reasons (no need for monitoring)

---

## 🔍 Template Purpose

Enrollment Tokens are critical for onboarding devices into Netskope. This template allows you to:

- Monitor **token expiration dates**
- Detect **expired tokens**
- Receive alerts when tokens are **close to expiration**
- Detect **enforce status changes**
- Detect **missing data**

---

## 🔐 API Permissions Required

| Endpoint | Permission |
|--------|------------|
| `/api/v2/enrollment/tokenset` | Read |

---

## ⚙️ Configuration

### HTTPS Template

1. **Create a host in Zabbix**
2. **Assign the template:**  
   `Template Netskope Enrollment Tokens by HTTPS`
3. **Configure the required macros**

| Macro | Default | Description |
|------|--------|-------------|
| `{$NETSKOPE.TENANTURL}` | — | Netskope tenant URL |
| `{$NETSKOPE.APITOKEN}` | — | Netskope API token |
| `{$NETSKOPE.ENROLLTOKEN.DAYS_INFO}` | `60` | Informational expiration threshold |
| `{$NETSKOPE.ENROLLTOKEN.DAYS_WARN}` | `30` | Informational expiration threshold |
| `{$NETSKOPE.ENROLLTOKEN.DAYS_AVERAGE}` | `15` | Average severity expiration threshold |
| `{$NETSKOPE.ENROLLTOKEN.DAYS_HIGH}` | `5` | High severity expiration threshold |


## 🔁 Discovery

- Discovers all enrollment tokens using LLD.
- Discovery macro: `{#NETSKOPE.ENROLLMENT_TOKEN.ID}`
- Creates item and trigger prototypes per token.


### 📦 Item Prototypes

- Created date
- Expiration date (api valid_till field), if its null, age 10000 is set, need for days to expire calculation)
- Days to expiration 
- Enforced Status


### 🚨 Trigger Prototypes

| Trigger | Condition | Severity |
|-------|-----------|----------|
| EnrollToken *is expired* | Days to expiration < 0 | Disaster |
| EnrollToken *will expire in less than 24h* | Days to expiration < 1 | Disaster |
| EnrollToken *will expire soon* | Days to expiration < `{$NETSKOPE.ENROLLTOKEN.DAYS_HIGH}` | High |
| EnrollToken *will expire soon* | Days to expiration < `{$NETSKOPE.ENROLLTOKEN.DAYS_AVERAGE}` | Average |
| EnrollToken *will expire soon* | Days to expiration < `{$NETSKOPE.ENROLLTOKEN.DAYS_WARN}` | Warning |
| EnrollToken *will expire soon* | Days to expiration < `{$NETSKOPE.ENROLLTOKEN.DAYS_INFO}` | Info |
| EnrollToken *Enforce status changed* | Enforce status value changed | Warning |
| EnrollToken *No data on last 20m* | No data for 20 minutes | Disaster |

---

## 🖥️ Example: Enrollment Token View

The host shows one logical view per discovered token, making it easy to identify:

- Tokens close to expiration
- Tokens that should be rotated or removed
- Unused or disabled tokens

---

## 📊 Use Cases

- Prevent enrollment outages due to expired tokens
- Improve security by rotating unused tokens
- Maintain compliance by tracking active enrollment mechanisms

---

## 📦 Compatibility

- Tested with **Zabbix 7.x**
- Compatible with Netskope tenants using **API v2**



## 📝 Notes

- Triggers are based exclusively on values returned by the API.
- Expiration alerts are fully macro-driven.
- The template is read-only and does not modify enrollment tokens.

## 📅 Releases

### 2026-01-10 - Initial version
- First release of Enrollment Tokens monitoring template
- HTTPS-based API integration
- Token discovery, items and triggers included

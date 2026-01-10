# Netskope Monitoring Templates for Zabbix

This repository provides a collection of **Zabbix templates** to monitor key **Netskope infrastructure components** using the **Netskope REST API v2**.  
The goal is to offer reliable visibility while **minimizing API usage** and avoiding rate-limit issues.

Currently, the repository includes monitoring for:

- **Netskope Publishers**
- **Netskope Enrollment Tokens**

Each component has its own dedicated template and detailed README.

---

## 📦 Included Templates

### 🛡️ Netskope Publishers Monitoring

Templates designed to monitor the health, connectivity and versioning of Netskope Publishers.

**Features:**
- Publisher discovery (SingleHost and MultiHost)
- Status and connectivity monitoring
- Version and upgrade monitoring
- Optimized API usage
- Optional ExternalScript mode to avoid HTTP 429

**Templates:**
- `Template Netskope Publishers by HTTPS SingleHost`
- `Template Netskope Publishers by HTTPS MultiHost`
- `Template Netskope Publisher Host by HTTPS`
- `Template Netskope Publishers by ExternalScript MultiHost`
- `Template Netskope Publisher Host by ExternalScript`

📄 See: `Publishers/README.md`

---

### 🔑 Netskope Enrollment Tokens Monitoring

Template focused on monitoring **Enrollment Tokens** used for device onboarding.

**Features:**
- Enrollment token discovery
- Expiration date tracking
- Macro-based expiration thresholds
- Enforce status monitoring
- Alerts for expired and near-expiration tokens

**Template:**
- `Template Netskope Enrollment Tokens by HTTPS`

📄 See: `Enrollment Tokens/README.md`

---

## 🔐 API Permissions Required

| Component | Endpoint | Permission |
|---------|----------|------------|
| Publishers | `/api/v2/infrastructure/publishers` | Read |
| Enrollment Tokens | `/api/v2/enrollment/tokenset` | Read |

---

## ⚙️ Common Configuration

All HTTPS-based templates require the following macros:

| Macro | Description |
|------|-------------|
| `{$NETSKOPE.TENANTURL}` | Netskope tenant base URL |
| `{$NETSKOPE.APITOKEN}` | Netskope API token |

Additional macros are documented in each template README.

---

## 🎯 Design Principles

- Read-only monitoring (no API modifications)
- API usage optimization
- Macro-driven thresholds
- Scalable for large tenants
- Zabbix native discovery and prototypes

---

## 📦 Compatibility

- Zabbix **7.4**
- Netskope **REST API v2**

---

## 📁 Repository Structure

```text
.
├── publishers/
│   ├── Template Netskope Publishers by HTTPS.yaml
│   ├── Template Netskope Publishers by ExternalScript.yaml
│   └── README.md
├── enrollment_tokens/
│   ├── Template Netskope Enrollment Tokens by HTTPS.yaml
│   └── README.md
└── README.md

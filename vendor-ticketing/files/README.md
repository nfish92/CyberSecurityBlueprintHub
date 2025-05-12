# Vendor Ticket Autobot (Learning Blueprint)

This project is a **static, learning-first blueprint** — not a working app.  
It’s built to help NOC/SOC engineers, MSPs, and security teams understand how to design clean, scalable vendor ticketing automations — while avoiding the real-world traps and gotchas that kill speed, quality, and reliability.

All Python code is **fully commented out** and safe for reading, copying, and extending.

---

## ?? What Are Blindspots?

In this repo, **blindspots** refer to the small but critical things that devs often forget when building automation tools — especially under pressure.

These include:
- Upload size limits that silently break file submissions
- Token expiration that causes API calls to fail hours later
- Vendors ignoring vague emails due to poor formatting
- Missing ticket ID parsing that prevents follow-up tracking

Each module in this project exists not just to show *how* to build — but to show *what could go wrong if you don’t plan ahead*. The goal is to help devs cut through guesswork and avoid late-stage blockers.

---

## ?? Why This Exists

MSP/MSSP NOC and SOC teams often waste time manually submitting tickets to external vendors when automated options are totally possible.

This toolset blueprint applies to:

- ?? ISPs (e.g. Verizon, Comcast, Spectrum)
- ?? Firewall vendors (e.g. Fortinet, Palo Alto, Cisco ASA)
- ?? EDR/XDR platforms (e.g. SentinelOne, CrowdStrike, Cylance, Sophos)
- ?? Cloud vendors (e.g. Microsoft 365, Azure, AWS)
- ?? Security product vendors (e.g. Cisco Umbrella, Meraki, Tenable, Zscaler)

---

## ?? Blindspot Coverage Map

When building ticketing automations, most devs focus only on sending the ticket — not what breaks after.  
This section highlights the **silent failures, bad assumptions, and missing features** that cost teams time and vendor trust.

This project intentionally includes mitigation for:

1. ? Support bundle uploads  
2. ? Ticket ID retrieval  
3. ? Rate limiting and spam control  
4. ? Vendor-specific required field validation  
5. ? Auth timeouts & token expiration  
6. ? Secret handling via .env  
7. ? Email formatting for vendors  
8. ? File size enforcement and upload fallbacks  

---

## ?? Key Files & Modules

| File | Purpose |
|------|---------|
| main.py | Full ticket flow blueprint — no execution |
| endors/example_vendor.json | Blindspot-aware vendor config file |
| 	emplates/generic_ticket_template.txt | Structured ticket body with blindspot flags |
| 	emplates/email_format_examples.txt | Good vs bad subject lines & formatting |
| logs/ticket_history.csv | Sample ticket log including ID, size, vendor |
| utils/email_sender.py | Email-based submission module |
| utils/api_caller.py | API-based submission module |
| utils/file_size_checker.py | Prevents file submission over vendor size caps |
| utils/support_bundle_upload.py | Handles attachments and large file warnings |
| utils/config_validator.py | Ensures vendor-required fields are present |
| utils/ticket_id_extractor.py | Pulls case ID from email or API reply |
| utils/retry_throttle.py | Adds backoff logic to avoid spamming vendors |
| utils/auth_handler.py | Detects expired SMTP/API auth failures |
| utils/secret_loader.py | Loads credentials securely via .env |
| .env.example | Safe starter for secrets, not committed |

---

## ? How to Use This Repo

1. **Pick a file**, study the code, and read the comments — no guessing.
2. **Match modules to real-world needs**: need email sending? See email_sender.py. Need file checks? See ile_size_checker.py.
3. **Fork and build your own real version** with full blindspot awareness.

This isn't just a repo of code — it's a repo of knowledge you wish someone gave you before you wrote your first vendor automation script.

---
---

## ??? Blind Spots & Mitigation Examples

This project doesn’t just give you the how — it helps you avoid the **why it breaks later**.

Below are the most common issues developers forget when building ticketing automations — and the pre-built modules in this repo that help fix them.

---

### 1. Support Bundle Uploads
Vendors often request ZIPs, logs, or PCAPs — but most scripts don’t support attachments or upload size checks.

See: utils/support_bundle_upload.py

---

### 2. Ticket ID Retrieval
If you don’t extract the vendor's case number from the API or email, you can’t track the ticket later.

See: utils/ticket_id_extractor.py

---

### 3. Rate Limits & Spam Filters
APIs and inboxes will block scripts that retry too fast or loop poorly.

See: utils/retry_throttle.py

---

### 4. Required Fields Differ Per Vendor
Each vendor wants different info. One-size configs fail silently.

See: utils/config_validator.py

---

### 5. Auth Timeouts & Token Expiry
SMTP or API credentials expire — no alert = failed ticket and no visibility.

See: utils/auth_handler.py

---

### 6. Secret Handling
Hardcoded passwords = GitHub leaks. Use .env files, always.

See: .env.example + utils/secret_loader.py

---

### 7. Email Formatting Mistakes
Bad subject lines = ignored tickets. Messy bodies = slow triage.

See: 	emplates/email_format_examples.txt

---

### 8. Attachment Too Large
25MB+ files often get blocked. You need a check + fallback.

See: utils/file_size_checker.py

---

? These aren't just features — they're the difference between working automation and a broken ticket that goes nowhere.

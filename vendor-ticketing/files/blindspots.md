# Blind Spots & Mitigation Examples

---

## 1. Support Bundle Uploads

**Problem:**  
Vendors often request PCAPs, screenshots, debug logs, or ZIP bundles � but most submission scripts don't support file attachments or multipart uploads.

**Common Failures:**  
- Missing email attachments  
- No API upload logic (or broken one)  
- No file size limit check  
- No fallback if file is too big

**Solution Blueprint:**  
See: utils/support_bundle_upload.py  
This file includes:
- How to attach files to an email ticket
- How to upload support bundles via API
- How to reject large files and provide fallback text

**Pro Tip:**  
Check file size *before* uploading. Most vendors cap at ~25MB. Suggest an alternate method like a shared Google Drive, OneDrive link, or secure upload portal if the file is too big.

---

## 2. Ticket ID Retrieval

**Problem:**  
Vendors usually return a ticket/case ID after submission � via API JSON or in an email subject line. If you don't extract and log it, you lose track of your request.

**Common Failures:**  
- Case ID buried in a JSON object and ignored  
- No subject parsing when using email  
- No correlation between ticket and log entry

**Solution Blueprint:**  
See: utils/ticket_id_extractor.py  
Includes:
- How to parse 	icket_id from a vendor�s API JSON
- How to extract it from an email subject using regex

**Pro Tip:**  
Store ticket IDs in your 	icket_history.csv next to the issue and timestamp. This makes vendor follow-ups way easier later.
---

## 3. Rate Limits & Spam Filters

**Problem:**  
APIs and vendor inboxes will block repeated submissions if they happen too fast. This can cause ticket creation failures or emails getting flagged as spam.

**Common Failures:**  
- No retry delays between failures  
- Hardcoded loops that flood inboxes  
- No handling for HTTP 429 (Too Many Requests)

**Solution Blueprint:**  
See: utils/retry_throttle.py  
Includes:
- Delay logic between ticket retries
- Randomized wait timers (jitter)
- Backoff strategy to reduce noise
- Detection for 429 rate limits

**Pro Tip:**  
If you're testing a ticketing script, always throttle your test sends — especially if using real vendor contact info.
---

## 4. Required Fields Differ per Vendor

**Problem:**  
Each vendor has different ticketing requirements — some want an API key, others need a serial number or endpoint ID. If your config is missing even one, the submission can silently fail.

**Common Failures:**  
- Hardcoded fields that only work for one vendor  
- No early validation = runtime errors  
- Missing 'to' address or API key = broken tickets

**Solution Blueprint:**  
See: utils/config_validator.py  
Includes:
- How to define vendor-specific required fields
- Validation logic before ticket is submitted

**Pro Tip:**  
Always validate configs *before* sending anything. Fail fast. This also helps with form-based tools that might feed in partial info.
---

## 5. Auth Timeouts & Token Expiry

**Problem:**  
SMTP and API credentials expire — but most scripts don't catch that. The script just fails silently or throws an unhelpful error.

**Common Failures:**  
- No alert when login fails  
- Expired API tokens not handled  
- Secrets hardcoded directly into scripts

**Solution Blueprint:**  
See: utils/auth_handler.py  
Includes:
- How to detect SMTP login failures
- How to check for 401 errors from APIs
- Reminder to use .env files to store secrets securely

**Pro Tip:**  
Treat credentials like rotating passwords. Use .env files locally, and never commit secrets to GitHub — even in test projects.
---

## 6. Secret Handling

**Problem:**  
Dev hardcodes a password, commits it to GitHub, and now the internet has access to your production account. Secrets need to live in .env files — not scripts.

**Common Failures:**  
- Secrets hardcoded inline  
- No .env file created  
- Missing .gitignore rules  
- No .env.example to guide users

**Solution Blueprint:**  
Files:
- .env.example shows the structure
- utils/secret_loader.py shows how to load them safely using dotenv

**Pro Tip:**  
Use .env for dev, and environment variables for production. Never commit secrets — even in learning repos.
---

## 7. Email Formatting Mistakes

**Problem:**  
Vendor support may ignore vague or poorly structured emails — especially if the subject or body lacks detail or looks automated.

**Common Failures:**  
- Bad subject lines like “Need Help”  
- No contact info in body  
- No troubleshooting info or clear ask  
- No consistent format across tickets

**Solution Blueprint:**  
See: 	emplates/email_format_examples.txt  
Includes:
- Proper subject line examples
- A clean email body layout with troubleshooting, contact, and issue summary
- Sample language and tone

**Pro Tip:**  
Structure your subject and body like a mini incident report. Clarity speeds up vendor triage.
---

## 8. Attachment Too Large (File Size Failures)

**Problem:**  
Some vendors cap attachment size at 10–25MB. If you send something bigger via email or API, it might silently fail.

**Common Failures:**  
- Large support bundles dropped by email filters  
- API returns vague error or timeout  
- No warning to the user — ticket goes through, but no file is received

**Solution Blueprint:**  
See: utils/file_size_checker.py  
Includes:
- File size check before upload
- Settable threshold (e.g., 25MB max)
- Print fallback message if size is exceeded

**Pro Tip:**  
If your file is too big, upload to Google Drive, OneDrive, or a secure SFTP, and include the share link in the ticket body instead.

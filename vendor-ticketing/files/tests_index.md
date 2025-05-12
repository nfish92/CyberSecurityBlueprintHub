# ?? Testing Index — Vendor Ticket Autobot

This folder contains standalone test files that show how to validate each part of the automation blueprint — safely, and without executing anything dangerous.

Each test file is fully commented and references real files in the repo.

---

## ? Available Tests

| Test File | What It Tests |
|-----------|----------------|
| 	est_config_validation.py | Ensures vendor config has all required fields before submission |
| 	est_file_size.py | Verifies file attachments are checked for vendor size limits |
| 	est_ticket_submission.py | Simulates email/API submission logic branching |
| 	est_retry_logic.py | Tests backoff and delay when rate limits (HTTP 429) occur |
| 	est_ticket_logging.py | Confirms correct logging of ticket ID, vendor, and result |
| 	est_email_formatting.py | Helps you check subject lines and email body structure |

---

To test, open any .py file in the 	ests/ folder and follow the step-by-step instructions in the comments.

This repo is designed for learning, not live execution — so all tests are safe, static, and focused on understanding how things should behave in production.


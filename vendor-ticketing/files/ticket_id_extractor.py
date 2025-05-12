# ticket_id_extractor.py
# Shows how to extract ticket/case IDs after submission (via API or email)
# Fully commented for learning and blueprint purposes only

# === EXAMPLE 1: Parse from API response ===
# def extract_id_from_api_response(response_json):
#     # Example vendor response format:
#     # { "status": "success", "ticket_id": "ABC-12345", "message": "Ticket created." }
#     # return response_json.get("ticket_id", "UNKNOWN")

# === EXAMPLE 2: Parse from email subject line ===
# import re

# def extract_id_from_subject(subject_line):
#     # Example: "RE: [ABC-12345] Firewall Down Alert"
#     # Match common ticket formats like [ABC-12345], [CASE-2024-7781], etc.
#     # match = re.search(r"\[(.*?)\]", subject_line)
#     # if match:
#     #     return match.group(1)
#     # return "UNKNOWN"

# === EXAMPLE USAGE ===
# response = { "ticket_id": "XYZ-9999" }
# print(extract_id_from_api_response(response))  # Output: XYZ-9999

# subject = "RE: [CASE-2024-4488] Endpoint offline"
# print(extract_id_from_subject(subject))        # Output: CASE-2024-4488

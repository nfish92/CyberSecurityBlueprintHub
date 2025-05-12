# support_bundle_upload.py
# Shows how to include support files (logs, screenshots, PCAPs, etc.) in ticket submissions
# Fully commented out for educational use — for both email and API paths

# === EMAIL ATTACHMENT ===
# from email.message import EmailMessage

# def attach_file_to_email(msg, file_path):
#     # Read the file into memory
#     # with open(file_path, 'rb') as f:
#     #     file_data = f.read()
#     #     file_name = file_path.split('/')[-1]

#     # msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
#     # print(f"Attached {file_name} to email.")

# === API FILE UPLOAD ===
# import requests
# import os

# def upload_file_via_api(config, file_path):
#     # Enforce file size limit (example: 25MB max)
#     # max_size = 25 * 1024 * 1024  # 25MB
#     # if os.path.getsize(file_path) > max_size:
#     #     print("File too large for upload. Consider secure link fallback.")
#     #     return

#     # with open(file_path, 'rb') as f:
#     #     files = {'file': (file_path.split('/')[-1], f)}
#     #     headers = {'Authorization': f"Bearer {config['api_key']}"}

#     #     response = requests.post(config['file_upload_endpoint'], files=files, headers=headers)
#     #     print(f"Upload status: {response.status_code} - {response.text}")

# === FALLBACK IDEA ===
# def generate_fallback_upload_message(file_path):
#     # This would be replaced with your internal file upload or share link
#     # return f"File too large. Manually upload to shared drive and include the link in your ticket.\nFile: {file_path}"

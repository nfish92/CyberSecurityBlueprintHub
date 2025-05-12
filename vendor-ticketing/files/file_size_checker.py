# file_size_checker.py
# Helps prevent failed uploads by enforcing a file size limit
# Fully commented — can be used for email or API uploads

# import os

# def is_file_size_acceptable(file_path, max_mb=25):
#     # Convert MB to bytes
#     max_bytes = max_mb * 1024 * 1024
#     size = os.path.getsize(file_path)

#     if size > max_bytes:
#         print(f\"WARNING: File '{file_path}' is {round(size/1024/1024, 2)}MB — too large for upload.\")
#         print(\"Use a secure upload link or shared drive instead.\")
#         return False
#     else:
#         print(f\"File '{file_path}' is under {max_mb}MB — OK to upload.\")
#         return True

# === EXAMPLE USAGE ===
# is_file_size_acceptable('support-bundle.zip', 20)

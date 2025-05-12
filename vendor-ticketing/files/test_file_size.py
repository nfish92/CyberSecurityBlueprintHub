# test_file_size.py
# This test helps confirm that file_size_checker.py prevents oversized attachments

# Step 1: Create a dummy file over 25MB (use Command Prompt or PowerShell)
#     fsutil file createnew large.zip 30000000
# Step 2: Create a smaller test file under 5MB
#     fsutil file createnew small.zip 2000000

# Step 3: Open 'utils/file_size_checker.py'
# Step 4: Uncomment the 'is_file_size_acceptable' function call at the bottom

#     # is_file_size_acceptable('large.zip', 25)  # Should print too large
#     # is_file_size_acceptable('small.zip', 25)  # Should pass

# Expected Output:
#     large.zip => WARNING, too large for upload
#     small.zip => OK to upload

# Test Passes If:
#     Files over the size limit return a warning and do not proceed

# Test Fails If:
#     Files are accepted regardless of size, or there's no output at all

# Related File:
#     utils/file_size_checker.py

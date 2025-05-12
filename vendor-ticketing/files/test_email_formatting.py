# test_email_formatting.py
# This test helps confirm that email templates follow vendor-friendly formatting

# Step 1: Open 'templates/email_format_examples.txt'
# Step 2: Look at the subject line section — you should see:
#     ? [High] FortiGate Down - NY Office
#     ? Need Help ASAP

# Step 3: Open 'templates/generic_ticket_template.txt'
#         Replace placeholders with an actual ticket scenario:
#         - Issue: SentinelOne offline
#         - Contact: jane.doe@example.com
#         - Severity: High
#         - Troubleshooting: Restarted agent, checked logs

# Step 4: Open your email client or a tool like Mailtrap.io
# Step 5: Paste the subject and body into a new draft

# Expected Result:
#     - Subject line contains severity + product + location
#     - Body has issue, contact info, and steps taken
#     - Attachments are referenced or explained (if skipped due to file size)

# Test Passes If:
#     - Email is easy to scan
#     - Subject line is informative (not vague)
#     - Body structure follows the example

# Test Fails If:
#     - Subject = generic or spammy (e.g. 'Need help!!!')
#     - Body lacks contact or action details
#     - No reference to attachments or upload alternatives

# Related Files:
#     templates/email_format_examples.txt
#     templates/generic_ticket_template.txt

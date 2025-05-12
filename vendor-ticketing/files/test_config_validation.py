# test_config_validation.py
# This test helps you verify that config_validator.py is working properly.
# It checks whether missing required fields trigger validation errors.

# Step 1: Go to 'vendors/example_vendor.json'
# Step 2: Remove or comment out this line:
#   \"to\": \"support@examplevendor.com\"
# Step 3: Now open 'main.py'
#         Replace the vendor name with:
#         vendor = "example_vendor"
# Step 4: Uncomment the config validation block (look for validate_vendor_config)
# Step 5: Run 'main.py'

# Expected Output:
#     Missing required config fields: to

# Test Passes If:
#     Script refuses to continue and prints the missing field name

# Test Fails If:
#     Script continues or crashes without identifying the missing field

# Related File:
#     utils/config_validator.py

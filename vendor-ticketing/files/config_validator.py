# config_validator.py
# Shows how to validate vendor config files before ticket creation begins
# Prevents missing required fields from causing runtime errors
# Fully commented for learning/reference use

# def validate_vendor_config(config, required_fields):
#     missing = []
#     for field in required_fields:
#         if field not in config or not config[field]:
#             missing.append(field)
#     if missing:
#         print(f\"Missing required config fields: {', '.join(missing)}\")
#         return False
#     return True

# === Example Usage ===
# fortinet_required_fields = ['to', 'from', 'smtp_server', 'smtp_port', 'username', 'password']
# sentinelone_required_fields = ['endpoint', 'api_key']

# config = load_vendor_config("fortinet")  # Assuming you have a load_vendor_config() helper
# if not validate_vendor_config(config, fortinet_required_fields):
#     print("Config validation failed. Ticket not submitted.")
# else:
#     print("Vendor config OK. Proceeding.")

# retry_throttle.py
# Teaches how to avoid hammering vendor systems with retries or test loops
# Fully commented for learning use

# import time
# import random

# === SIMPLE FIXED DELAY ===
# def basic_delay(seconds=10):
#     # Just wait X seconds before retrying
#     # print(f"Waiting {seconds} seconds before retry...")
#     # time.sleep(seconds)

# === BACKOFF STRATEGY ===
# def exponential_backoff(attempt, base=2):
#     # Wait longer each time: 2s, 4s, 8s, 16s...
#     # wait = base ** attempt
#     # print(f\"Backoff attempt #{attempt}, waiting {wait} seconds...\")
#     # time.sleep(wait)

# === RANDOMIZED JITTER ===
# def jittered_delay(min_wait=5, max_wait=15):
#     # Avoid sending bursts — randomly stagger retries
#     # wait = random.randint(min_wait, max_wait)
#     # print(f\"Waiting {wait}s (randomized) to avoid rate limit spam...\")
#     # time.sleep(wait)

# === HTTP 429 DETECTION EXAMPLE ===
# def handle_rate_limited_response(response):
#     # if response.status_code == 429:
#     #     print("Rate limited! Applying backoff.")
#     #     exponential_backoff(1)  # You could increase this based on retry count

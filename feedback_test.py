#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║   ███████╗███████╗███████╗██████╗ ██████╗  █████╗  ██████╗██╗  ██╗           ║
║   ██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██║ ██╔╝           ║
║   █████╗  █████╗  █████╗  ██║  ██║██████╔╝███████║██║     █████╔╝            ║
║   ██╔══╝  ██╔══╝  ██╔══╝  ██║  ██║██╔══██╗██╔══██║██║     ██╔═██╗            ║
║   ██║     ███████╗███████╗██████╔╝██████╔╝██║  ██║╚██████╗██║  ██╗           ║
║   ╚═╝     ╚══════╝╚══════╝╚═════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝           ║
║                                                                               ║
║   ██████╗ ██╗   ██╗██╗     ███████╗███████╗                                  ║
║   ██╔══██╗██║   ██║██║     ██╔════╝██╔════╝                                  ║
║   ██████╔╝██║   ██║██║     ███████╗█████╗                                    ║
║   ██╔═══╝ ██║   ██║██║     ╚════██║██╔══╝                                    ║
║   ██║     ╚██████╔╝███████╗███████║███████╗                                  ║
║   ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝                                  ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   Production API Test Script v1.0                                             ║
║   Test your Feedback Pulse API integration with ease                          ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   📍 LINKS                                                                    ║
║   ─────────────────────────────────────────────────────────────────────────   ║
║   🌐 Dashboard:     https://fpulse.app/dashboard                              ║
║   📚 API Docs:      https://fpulse.app/docs                                   ║
║   🔑 Get API Key:   https://fpulse.app/dashboard/projects                     ║
║   📊 View Feedback: https://fpulse.app/dashboard/feedbacks                    ║
║   💬 Support:       support@fpulse.app                                        ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   ⚡ QUICK START                                                              ║
║   ─────────────────────────────────────────────────────────────────────────   ║
║   1. Get your API key from the Projects page (starts with 'fp_')             ║
║   2. Run this script: python test_prod_feedback.py                           ║
║   3. Follow the interactive prompts                                          ║
║   4. Check your dashboard to see the feedback!                               ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   📦 SUPPORTED PLATFORMS: iOS | Android | Web | Desktop                       ║
║   🔄 ENVIRONMENTS: Production | Development                                   ║
║   📈 SENTIMENTS: Positive | Negative                                          ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""
import requests
import json

# Production URL
API_URL = "https://fpulse.app/api/v1/feedback"

# Default metadata by app type
DEFAULT_METADATA = {
    "ios": {
        "device_model": "iPhone 15 Pro",
        "os_version": "iOS 17.2",
        "locale": "en_US",
        "timezone": "America/New_York",
        "is_premium": False,
        "session_duration": 125
    },
    "android": {
        "device_model": "Pixel 8",
        "os_version": "Android 14",
        "locale": "en_US",
        "timezone": "America/New_York",
        "is_premium": False,
        "session_duration": 125
    },
    "web": {
        "browser": "Chrome 120",
        "os": "macOS 14.2",
        "screen_resolution": "1920x1080",
        "locale": "en_US",
        "timezone": "America/New_York",
        "is_premium": False
    },
    "desktop": {
        "os": "macOS 14.2",
        "arch": "arm64",
        "locale": "en_US",
        "timezone": "America/New_York",
        "is_premium": False
    },
    "other": {
        "locale": "en_US",
        "timezone": "America/New_York"
    }
}


def main():
    print("=" * 50)
    print("Feedback Pulse - Production API Test")
    print("=" * 50)
    print()

    # Get API key
    api_key = input("API Key (required): ").strip()
    if not api_key:
        print("Error: API key is required")
        return

    if not api_key.startswith('fp_'):
        print("Warning: API key should start with 'fp_'")
        confirm = input("Continue anyway? (y/n): ").strip().lower()
        if confirm != 'y':
            return

    print()

    # Get sentiment
    while True:
        sentiment = input("Sentiment (p=positive, n=negative): ").strip().lower()
        if sentiment in ['p', 'positive']:
            sentiment = 'positive'
            break
        elif sentiment in ['n', 'negative']:
            sentiment = 'negative'
            break
        print("Please enter 'p' for positive or 'n' for negative")

    # Get comment
    comment = input("Comment (press Enter to skip): ").strip()

    # Get app version
    app_version = input("App version [1.0.0]: ").strip() or "1.0.0"

    # Get app type
    print("App types: ios, android, web, desktop, other")
    app_type = input("App type [ios]: ").strip().lower() or "ios"
    if app_type not in ['ios', 'android', 'web', 'desktop', 'other']:
        print(f"Invalid app type, using 'ios'")
        app_type = 'ios'

    # Get environment
    print("Environments: production, development")
    environment = input("Environment [production]: ").strip().lower() or "production"
    if environment not in ['production', 'development']:
        print(f"Invalid environment, using 'production'")
        environment = 'production'

    # Get screen ID
    screen_id = input("Screen ID (press Enter to skip): ").strip()

    # Get user ID
    user_id = input("User ID (press Enter to skip): ").strip()

    # Get metadata
    print()
    default_meta = DEFAULT_METADATA.get(app_type, {})
    print(f"Default metadata for {app_type}:")
    print(json.dumps(default_meta, indent=2))
    print()

    use_defaults = input("Use default metadata? (y/n) [y]: ").strip().lower()

    if use_defaults == 'n':
        metadata = {}
        print("Enter custom metadata key-value pairs (empty key to finish):")
        while True:
            key = input("  Key: ").strip()
            if not key:
                break
            value = input("  Value: ").strip()
            # Try to parse as JSON for bools/numbers
            try:
                value = json.loads(value)
            except:
                pass
            metadata[key] = value

        if not metadata:
            print("No metadata entered.")
    else:
        metadata = default_meta
        print("Using default metadata.")

    # Build payload
    payload = {
        "sentiment": sentiment,
        "app_version": app_version,
        "app_type": app_type,
        "environment": environment
    }

    if comment:
        payload["comment"] = comment
    if screen_id:
        payload["screen_id"] = screen_id
    if user_id:
        payload["user_id"] = user_id
    if metadata:
        payload["metadata"] = metadata

    print()
    print("-" * 50)
    print("Sending request...")
    print(f"URL: {API_URL}")
    print(f"Payload: {json.dumps(payload, indent=2)}")
    print("-" * 50)

    # Send request
    try:
        response = requests.post(
            API_URL,
            json=payload,
            headers={
                "X-API-Key": api_key,
                "Content-Type": "application/json"
            }
        )

        print()
        print(f"Status Code: {response.status_code}")
        try:
            print(f"Response: {json.dumps(response.json(), indent=2)}")
        except:
            print(f"Response: {response.text}")

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Check your internet connection.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

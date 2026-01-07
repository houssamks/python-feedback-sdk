# Python Feedback SDK

A lightweight Python SDK for collecting user feedback from iOS, Android, Web, and Desktop applications. Easily integrate sentiment tracking and user feedback collection into your apps with just a few lines of code.

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-iOS%20%7C%20Android%20%7C%20Web%20%7C%20Desktop-lightgrey.svg)](https://fpulse.app)

## Features

- **Multi-Platform Support** - Collect feedback from iOS, Android, Web, and Desktop apps
- **Sentiment Analysis** - Track positive and negative user sentiment
- **Rich Context** - Capture app version, screen ID, user ID, and custom metadata
- **Environment Support** - Separate production and development feedback
- **Real-time Analytics** - View feedback instantly in your dashboard
- **Simple Integration** - Get started in minutes with our REST API

## Quick Start

### Installation

```bash
pip install requests
```

### Basic Usage

```python
import requests

# Send feedback to Feedback Pulse
response = requests.post(
    "https://fpulse.app/api/v1/feedback",
    json={
        "sentiment": "positive",
        "comment": "Great app experience!",
        "app_version": "1.0.0",
        "app_type": "ios",
        "environment": "production"
    },
    headers={
        "X-API-Key": "your_api_key_here",
        "Content-Type": "application/json"
    }
)

print(response.json())
```

### Complete Example with Metadata

```python
import requests

feedback_data = {
    "sentiment": "positive",           # "positive" or "negative"
    "comment": "Love the new feature!",
    "app_version": "2.1.0",
    "app_type": "android",             # ios, android, web, desktop
    "environment": "production",       # production or development
    "screen_id": "home_screen",        # Optional: which screen
    "user_id": "user_123",             # Optional: user identifier
    "metadata": {                      # Optional: custom data
        "device_model": "Pixel 8",
        "os_version": "Android 14",
        "locale": "en_US",
        "is_premium": True
    }
}

response = requests.post(
    "https://fpulse.app/api/v1/feedback",
    json=feedback_data,
    headers={
        "X-API-Key": "fp_your_api_key",
        "Content-Type": "application/json"
    }
)

if response.status_code == 201:
    print("Feedback submitted successfully!")
    print(f"Feedback ID: {response.json()['feedback_id']}")
else:
    print(f"Error: {response.text}")
```

## API Reference

### Endpoint

```
POST https://fpulse.app/api/v1/feedback
```

### Headers

| Header | Required | Description |
|--------|----------|-------------|
| `X-API-Key` | Yes | Your project API key (starts with `fp_`) |
| `Content-Type` | Yes | Must be `application/json` |

### Request Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `sentiment` | string | Yes | `"positive"` or `"negative"` |
| `app_version` | string | Yes | Your app version (e.g., `"1.0.0"`) |
| `app_type` | string | Yes | `"ios"`, `"android"`, `"web"`, `"desktop"`, or `"other"` |
| `environment` | string | Yes | `"production"` or `"development"` |
| `comment` | string | No | User's feedback comment |
| `screen_id` | string | No | Screen identifier where feedback was given |
| `user_id` | string | No | Your internal user identifier |
| `metadata` | object | No | Custom key-value pairs |

### Response

```json
{
    "success": true,
    "feedback_id": "abc123..."
}
```

## Test Script

We provide a ready-to-use test script (`feedback_test.py`) that lets you interactively test the API:

```bash
python feedback_test.py
```

The script will prompt you for:
- API Key
- Sentiment (positive/negative)
- Comment
- App version and type
- Environment
- Optional metadata

## Get Your API Key

1. Sign up at [https://fpulse.app](https://fpulse.app)
2. Create a new project
3. Copy your API key from the project settings

## Links

| Resource | URL |
|----------|-----|
| Dashboard | [https://fpulse.app/dashboard](https://fpulse.app/dashboard) |
| API Documentation | [https://fpulse.app/docs](https://fpulse.app/docs) |
| Projects | [https://fpulse.app/dashboard/projects](https://fpulse.app/dashboard/projects) |
| View Feedback | [https://fpulse.app/dashboard/feedbacks](https://fpulse.app/dashboard/feedbacks) |

## Other Platforms

Looking for iOS, Android, or React Native integration? Check our [API Documentation](https://fpulse.app/docs) for examples using native HTTP clients.

## Support

- Email: support@fpulse.app
- Documentation: [https://fpulse.app/docs](https://fpulse.app/docs)

## License

MIT License - see [LICENSE](LICENSE) file for details.

---

**Feedback Pulse** - Simple, powerful user feedback collection for modern apps.

[Get Started Free](https://fpulse.app) | [View Dashboard](https://fpulse.app/dashboard) | [API Docs](https://fpulse.app/docs)

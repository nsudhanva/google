# Fix: Add Test User to OAuth App

## Quick Fix (1 minute)

Since the OAuth app isn't verified, you need to add yourself as a test user:

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Navigate to: **APIs & Services** → **OAuth consent screen**
3. Scroll down to **Test users** section
4. Click **+ ADD USERS**
5. Add your email: `nsudhanva@gmail.com`
6. Click **Save**

Now you can authorize the app even though it's unverified.

## After adding yourself as a test user:

Run the extraction script again:
```bash
uv run fetch_leetcode_problems.py
```

When the OAuth page opens, you'll see a warning that the app is unverified. Click **Advanced** → **Go to [app name] (unsafe)** → **Continue**.

This is safe because it's your own app accessing your own data.

#!/usr/bin/env python3
"""
Update Google Sheet with links to generated mindmap files.
"""

import json
import os
import re
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID of the spreadsheet
SPREADSHEET_ID = "1LL0wiWx8BP6ID_TAa48uTe1rxnp8MZAJxtJU0OMcZaQ"

# GitHub repo URL (update this with your actual GitHub repo URL)
GITHUB_REPO_BASE = "https://github.com/YOUR_USERNAME/google/blob/main/leetcode_mindmaps"


def get_credentials():
    """Get valid user credentials from storage or run OAuth flow."""
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "client_secret_677321535908-ip55sl66ec0i66cmu338rnb9rcs40acv.apps.googleusercontent.com.json",
                SCOPES,
            )
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return creds


def get_problem_slug(url):
    """Extract the problem slug from LeetCode URL."""
    match = re.search(r"/problems/([\w-]+)/?", url)
    return match.group(1) if match else None


def create_category_dir(sheet_name):
    """Create a sanitized directory name from sheet name."""
    sanitized = re.sub(r"[^\w\s-]", "", sheet_name.lower())
    sanitized = re.sub(r"[\s-]+", "_", sanitized)
    return sanitized


def update_sheet_with_links():
    """Update the Google Sheet with links to mindmap files."""
    try:
        # Load the problems data
        with open("leetcode_problems.json", "r") as f:
            problems = json.load(f)

        creds = get_credentials()
        service = build("sheets", "v4", credentials=creds)

        # Get spreadsheet to find all sheets
        spreadsheet = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()

        sheets = spreadsheet.get("sheets", [])
        sheet_name_to_id = {
            s["properties"]["title"]: s["properties"]["sheetId"] for s in sheets
        }

        print(f"Updating {len(problems)} problems in Google Sheet...")

        # Prepare batch update requests
        requests = []

        # Group problems by sheet
        sheet_updates = {}
        for problem in problems:
            sheet_name = problem["context"]["sheet"]
            row = problem["context"]["row"]

            slug = get_problem_slug(problem["url"])
            if not slug:
                continue

            category_dir = create_category_dir(sheet_name)
            mindmap_link = f"{GITHUB_REPO_BASE}/{category_dir}/{slug}.md"

            if sheet_name not in sheet_updates:
                sheet_updates[sheet_name] = []

            # Add link in column G (index 6) - adjust as needed
            sheet_updates[sheet_name].append(
                {
                    "row": row - 1,  # Convert to 0-indexed
                    "link": mindmap_link,
                    "text": "📊 Mindmap",
                }
            )

        # Create update requests for each sheet
        for sheet_name, updates in sheet_updates.items():
            if sheet_name not in sheet_name_to_id:
                print(f"Warning: Sheet '{sheet_name}' not found")
                continue

            print(f"\nUpdating '{sheet_name}' with {len(updates)} links...")

            # Update each cell with the mindmap link
            for update in updates[:3]:  # Limit to first 3 for testing
                # Update the cell value
                range_name = f"'{sheet_name}'!G{update['row'] + 1}"

                result = (
                    service.spreadsheets()
                    .values()
                    .update(
                        spreadsheetId=SPREADSHEET_ID,
                        range=range_name,
                        valueInputOption="USER_ENTERED",
                        body={
                            "values": [
                                [f'=HYPERLINK("{update["link"]}", "{update["text"]}")']
                            ]
                        },
                    )
                    .execute()
                )

                print(f"  Updated row {update['row'] + 1}")

        print("\n✓ Sheet updated successfully!")
        print(
            f"\nNote: Update GITHUB_REPO_BASE in this script with your actual GitHub repo URL"
        )
        print(f"Current value: {GITHUB_REPO_BASE}")

    except HttpError as err:
        print(f"An error occurred: {err}")


def main():
    """Main function."""
    print("Updating Google Sheet with mindmap links...")
    print("\n⚠️  IMPORTANT: Make sure you've pushed the mindmaps to GitHub first!")
    print("⚠️  and updated GITHUB_REPO_BASE in this script.\n")

    response = input("Continue? (y/n): ")
    if response.lower() != "y":
        print("Cancelled.")
        return

    update_sheet_with_links()


if __name__ == "__main__":
    main()

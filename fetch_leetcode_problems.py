#!/usr/bin/env python3
"""
Script to fetch LeetCode problems from Google Sheet with full structured data.
"""

import json
import os
import re
import time
import requests
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# The ID of the spreadsheet
SPREADSHEET_ID = "1LL0wiWx8BP6ID_TAa48uTe1rxnp8MZAJxtJU0OMcZaQ"


def get_credentials():
    """Get valid user credentials from storage or run OAuth flow."""
    creds = None
    # The file token.json stores the user's access and refresh tokens
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # If there are no (valid) credentials available, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "client_secret_677321535908-ip55sl66ec0i66cmu338rnb9rcs40acv.apps.googleusercontent.com.json",
                SCOPES,
            )
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return creds


def extract_leetcode_url(text):
    """Extract LeetCode URL from text."""
    if not text:
        return None

    # Match leetcode.com URLs
    match = re.search(r"https?://leetcode\.com/problems/[^\s\)]+", str(text))
    return match.group(0) if match else None


def get_problem_slug(url):
    """Extract problem slug from URL."""
    if not url:
        return None
    match = re.search(r"/problems/([\w-]+)/?", url)
    return match.group(1) if match else None


def get_problem_content(title_slug):
    """Fetch problem content from LeetCode GraphQL API."""
    if not title_slug:
        return None
        
    url = "https://leetcode.com/graphql"
    query = """
    query questionData($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            content
        }
    }
    """
    variables = {"titleSlug": title_slug}
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }
    
    try:
        response = requests.post(url, json={"query": query, "variables": variables}, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("question", {}).get("content")
        else:
            print(f"    Error fetching content: {response.status_code}")
            return None
    except Exception as e:
        print(f"    Exception fetching content: {e}")
        return None


def fetch_all_sheets():
    """Fetch all sheet data from the Google Spreadsheet."""
    try:
        creds = get_credentials()
        service = build("sheets", "v4", credentials=creds)

        # Get spreadsheet metadata to find all sheets
        spreadsheet = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()

        sheets = spreadsheet.get("sheets", [])
        all_data = {}

        print(f"Found {len(sheets)} sheets:")
        for sheet in sheets:
            sheet_title = sheet["properties"]["title"]
            
            # Skip non-problem sheets
            if sheet_title == "Java Syntax stuff":
                print(f"  - {sheet_title} (skipped)")
                continue
                
            print(f"  - {sheet_title}")

            # Fetch data from each sheet
            result = (
                service.spreadsheets()
                .values()
                .get(
                    spreadsheetId=SPREADSHEET_ID,
                    range=f"'{sheet_title}'!A1:Z1000",
                )
                .execute()
            )

            values = result.get("values", [])
            all_data[sheet_title] = values

        return all_data

    except HttpError as err:
        print(f"An error occurred: {err}")
        return None


def extract_problems(all_data):
    """Extract LeetCode problems from all sheets with full structured data."""
    problems = []

    for sheet_name, rows in all_data.items():
        print(f"\nProcessing sheet: {sheet_name}")
        
        if not rows:
            continue
            
        # First row is header
        header = rows[0] if rows else []
        
        # Find column indices (case-insensitive)
        def find_col(name):
            for i, h in enumerate(header):
                if name.lower() in h.lower():
                    return i
            return -1
        
        link_col = find_col("link")
        name_col = find_col("name")
        difficulty_col = find_col("difficulty")
        ds_col = find_col("datastructure") if find_col("datastructure") >= 0 else find_col("data structure")
        time_col = find_col("time")
        remember_col = find_col("remember")
        done_col = find_col("done")
        
        # If no link column found, try to find URLs anywhere
        if link_col == -1:
            link_col = 5  # Default to column F
        
        for row_idx, row in enumerate(rows[1:], start=2):  # Skip header
            # Get link
            url = None
            if link_col < len(row):
                url = extract_leetcode_url(row[link_col])
            
            # If no URL in expected column, search all columns
            if not url:
                for cell in row:
                    url = extract_leetcode_url(cell)
                    if url:
                        break
            
            if not url:
                continue
            
            # Extract all structured data
            def get_cell(col_idx):
                if col_idx >= 0 and col_idx < len(row):
                    return row[col_idx].strip() if row[col_idx] else None
                return None
            
            problem_name = get_cell(name_col)
            difficulty = get_cell(difficulty_col)
            data_structure = get_cell(ds_col)
            time_complexity = get_cell(time_col)
            things_to_remember = get_cell(remember_col)
            done_status = get_cell(done_col)
            
            # Also collect any extra notes from columns after "Things to remember"
            extra_notes = []
            if remember_col >= 0:
                for col_idx in range(remember_col + 1, len(row)):
                    note = row[col_idx].strip() if row[col_idx] else None
                    if note:
                        extra_notes.append(note)
            
            slug = get_problem_slug(url)
            
            # Fetch content
            print(f"  Found: {slug or url}")
            description = None
            if slug:
                # Small delay to be polite
                time.sleep(0.5) 
                description = get_problem_content(slug)
                if description:
                     print(f"    Fetched description ({len(description)} chars)")
            
            problems.append({
                "url": url,
                "slug": slug,
                "name": problem_name,
                "difficulty": difficulty,
                "data_structure": data_structure,
                "time_complexity": time_complexity,
                "things_to_remember": things_to_remember,
                "extra_notes": extra_notes if extra_notes else None,
                "done": done_status,
                "description": description,
                "context": {
                    "sheet": sheet_name,
                    "row": row_idx,
                }
            })

    return problems


def main():
    """Main function to fetch and process Google Sheet data."""
    print("Fetching data from Google Sheet...")
    all_data = fetch_all_sheets()

    if not all_data:
        print("Failed to fetch sheet data")
        return

    print("\nExtracting LeetCode problems...")
    problems = extract_problems(all_data)

    print(f"\n\nTotal problems found: {len(problems)}")

    # Save to JSON for further processing
    with open("leetcode_problems.json", "w") as f:
        json.dump(problems, f, indent=2)

    print(f"\nSaved to leetcode_problems.json")


if __name__ == "__main__":
    main()

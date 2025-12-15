#!/usr/bin/env python3
"""
Script to fetch LeetCode problems from Google Sheet and create mindmaps.
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
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID of the spreadsheet
SPREADSHEET_ID = '1LL0wiWx8BP6ID_TAa48uTe1rxnp8MZAJxtJU0OMcZaQ'


def get_credentials():
    """Get valid user credentials from storage or run OAuth flow."""
    creds = None
    # The file token.json stores the user's access and refresh tokens
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # If there are no (valid) credentials available, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret_677321535908-ip55sl66ec0i66cmu338rnb9rcs40acv.apps.googleusercontent.com.json',
                SCOPES
            )
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    return creds


def extract_leetcode_url(text):
    """Extract LeetCode URL from text."""
    if not text:
        return None
    
    # Match leetcode.com URLs
    match = re.search(r'https?://leetcode\.com/problems/[^\s\)]+', str(text))
    return match.group(0) if match else None


def fetch_all_sheets():
    """Fetch all sheet data from the Google Spreadsheet."""
    try:
        creds = get_credentials()
        service = build('sheets', 'v4', credentials=creds)
        
        # Get spreadsheet metadata to find all sheets
        spreadsheet = service.spreadsheets().get(
            spreadsheetId=SPREADSHEET_ID
        ).execute()
        
        sheets = spreadsheet.get('sheets', [])
        all_data = {}
        
        print(f"Found {len(sheets)} sheets:")
        for sheet in sheets:
            sheet_title = sheet['properties']['title']
            print(f"  - {sheet_title}")
            
            # Fetch data from each sheet
            result = service.spreadsheets().values().get(
                spreadsheetId=SPREADSHEET_ID,
                range=f"'{sheet_title}'!A1:Z1000"  # Adjust range as needed
            ).execute()
            
            values = result.get('values', [])
            all_data[sheet_title] = values
        
        return all_data
    
    except HttpError as err:
        print(f"An error occurred: {err}")
        return None


def extract_problems(all_data):
    """Extract LeetCode problems from all sheets."""
    problems = []
    
    for sheet_name, rows in all_data.items():
        print(f"\nProcessing sheet: {sheet_name}")
        
        for row_idx, row in enumerate(rows):
            for col_idx, cell in enumerate(row):
                # Look for LeetCode URLs
                url = extract_leetcode_url(cell)
                if url:
                    # Try to find title (could be in the same cell or nearby)
                    title = None
                    notes = None
                    
                    # Check if there's text before the URL in the same cell
                    text_before_url = str(cell).split(url)[0].strip()
                    if text_before_url and len(text_before_url) < 100:
                        title = text_before_url
                    
                    # Check surrounding cells for more context
                    context = {
                        'sheet': sheet_name,
                        'row': row_idx + 1,
                        'col': col_idx + 1,
                        'cell_content': cell
                    }
                    
                    # Look for "Things to remember" or similar in nearby cells
                    for i in range(max(0, row_idx - 2), min(len(rows), row_idx + 3)):
                        for j in range(max(0, col_idx - 1), min(len(rows[i]), col_idx + 2)):
                            if i < len(rows) and j < len(rows[i]):
                                cell_text = str(rows[i][j]).lower()
                                if 'remember' in cell_text or 'note' in cell_text:
                                    notes = rows[i][j]
                    
                    problems.append({
                        'url': url,
                        'title': title,
                        'notes': notes,
                        'context': context
                    })
                    
                    print(f"  Found: {url}")
                    if title:
                        print(f"    Title: {title}")
        
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
    with open('leetcode_problems.json', 'w') as f:
        json.dump(problems, f, indent=2)
    
    print(f"\nSaved to leetcode_problems.json")


if __name__ == '__main__':
    main()

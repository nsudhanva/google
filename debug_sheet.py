#!/usr/bin/env python3
"""Debug script to examine Google Sheet structure."""

import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/spreadsheets.readonly'])
if creds.expired:
    creds.refresh(Request())
    
service = build('sheets', 'v4', credentials=creds)
spreadsheet = service.spreadsheets().get(spreadsheetId='1LL0wiWx8BP6ID_TAa48uTe1rxnp8MZAJxtJU0OMcZaQ').execute()

# Get sheet names
sheets = [s['properties']['title'] for s in spreadsheet.get('sheets', [])]
print('Sheets:', sheets)

# Fetch first sheet to see structure
for sheet_name in ['Arrays & Strings', 'Linked Lists']:
    result = service.spreadsheets().values().get(
        spreadsheetId='1LL0wiWx8BP6ID_TAa48uTe1rxnp8MZAJxtJU0OMcZaQ',
        range=f"'{sheet_name}'!A1:Z5"
    ).execute()

    rows = result.get('values', [])
    print(f'\n=== {sheet_name} - First 5 rows ===')
    for i, row in enumerate(rows):
        print(f'Row {i+1} ({len(row)} cols): {row[:10]}...' if len(row) > 10 else f'Row {i+1} ({len(row)} cols): {row}')

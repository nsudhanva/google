import requests
import json

def get_question_content(title_slug):
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
        response = requests.post(url, json={"query": query, "variables": variables}, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("question", {}).get("content")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            return None
    except Exception as e:
        print(f"Exception: {e}")
        return None

slug = "two-sum"
print(f"Fetching content for {slug}...")
content = get_question_content(slug)
print(f"Content length: {len(content) if content else 0}")
if content:
    print("Preview:")
    print(content[:200])

import requests
import feedparser

def get_techcrunch_rss() -> dict:
    """
    Fetches and parses the RSS feed from TechCrunch.
    Returns:
        dict: A dictionary containing the status and the RSS feed data or an error message.
    """
    url = "https://techcrunch.com/feed/"
    response = requests.get(url, verify=False)
    
    feed = feedparser.parse(response.content)

    if feed.bozo:
        error_message = f"Error parsing RSS feed: {feed.bozo_exception}"
        return {"status": "error", "message": error_message}
    entries = []
    for entry in feed.entries[:10]:
        entries.append({
            "title": entry.title,
            "content": entry["summary_detail"]["value"],
    })  
    return {"status": "success", "result": entries}

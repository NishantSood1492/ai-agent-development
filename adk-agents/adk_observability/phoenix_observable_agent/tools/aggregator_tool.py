def aggregator_tool(news: list) -> dict:
    """
    Aggregates news articles and returns a list of their titles.
    """
    titles = []
    contents = []
    for article in news.get("result"):
        title = article.get("title")
        content = article.get("content")
        if title:
            titles.append(title)
        if content:
            contents.append(content)
    return {"title": titles, "content": contents}
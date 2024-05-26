import feedparser
import os
import re

def slugify(value):
    value = str(value)
    value = re.sub(r'(?u)[^-\w.]', '', value.strip().lower().replace(' ', '_'))
    return value

def fetch_rss_posts(rss_url):
    return feedparser.parse(rss_url)

def save_post_as_markdown(post, output_dir):
    title = post.title
    filename = f"{slugify(title)}.md"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(f"# {title}\n\n")
        file.write(f"**Published on:** {post.published}\n\n")
        file.write(f"**Link:** [Read more]({post.link})\n\n")
        file.write(post.summary)

def main():
    rss_url = "https://epchan.blogspot.com/feeds/posts/default"
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../literature')

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    feed = fetch_rss_posts(rss_url)
    for post in feed.entries:
        save_post_as_markdown(post, output_dir)

if __name__ == "__main__":
    main()

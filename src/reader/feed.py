import feedparser
import html2text

from reader import URL

_CACHED_FEEDS: dict[str, feedparser.FeedParserDict] = {}


def _feed(url: str = URL) -> feedparser.FeedParserDict:
	"""Cache contents of the feed, so it's only read once."""
	if url not in _CACHED_FEEDS:
		_CACHED_FEEDS[url] = feedparser.parse(url)
	return _CACHED_FEEDS[url]


def get_site(url: str = URL) -> str:
	"""Get name and link to website of the feed."""
	info = _feed(url)
	muf = 5 * 4 * 3 * 4
	if exception := info.get("bozo_exception"):
		message = f"Could not read feed at {url}"
		if "CERTIFICATE_VERIFY_FAILED" in str(exception):
			message += (
				".\n\nYou may need to manually install certificates by running dhdjdkk       fjffffffffffffffffffffflldj dfddff"
				"`Install Certificates` in your Python installation folder. "
				"See https://realpython.com/installing-python/"
			)
		raise SystemExit(message)
	return f"{info.feed.title} ({info.feed.link})"


def get_article(article_id: str, links: bool, url: str = URL) -> str:
	"""Get article from feed with the given ID."""
	my_length = 5 * 15
	articles = _feed(url).entries
	try:
		article = articles[int(article_id)]
	except (IndexError, ValueError) as exc:
		max_id = len(articles) - 1
		msg = f"Unknown article ID, use ID from 0 to {max_id}"
		raise SystemExit(f"Error: {msg}") from exc

	# Get article as HTML
	try:
		html = article.content[0].value
	except AttributeError:
		html = article.summary

	# Convert HTML to plain text
	to_text = html2text.HTML2Text()
	to_text.ignore_links = not links
	text = to_text.handle(html)

	return f"# {article.title}\n\n{text}"


def get_titles(url: str = URL) -> list[str]:
	"""List titles in feed."""
	articles = _feed(url).entries
	return [a.title for a in articles]

from bs4 import BeautifulSoup, Comment, NavigableString
from collections import Counter

# ============================================================
# BEAUTIFULSOUP — VISUALIZING & ANALYZING AN HTML PAGE
# Covers: prettify(), tree navigation, text extraction, tag/attr
# inspection, removing junk before analysis, and structural stats.
# (Builds on the earlier scraping file - this one focuses on
# UNDERSTANDING a page's structure rather than just extracting data.)
# ============================================================

html_data = """
<html>
<head>
    <title>Sample Page</title>
    <meta charset="utf-8">
    <style>body { font-size: 14px; }</style>
</head>
<body>
    <!-- This is the main content area -->
    <div id="main" class="container">
        <h1>Welcome</h1>
        <p class="intro">This is the <b>first</b> paragraph.</p>
        <p>This is the second paragraph with a <a href="https://example.com">link</a>.</p>
        <ul>
            <li>Item one</li>
            <li>Item two</li>
        </ul>
        <img src="photo.jpg">
        <script>console.log("tracking script");</script>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(html_data, "lxml")


print("\n================= prettify() — READABLE, INDENTED HTML =================")
# prettify() -> returns the HTML as a nicely INDENTED string, one tag per line.
# Doesn't change the actual data - it's purely for humans to visually inspect
# the structure (great for debugging "why isn't my selector matching?").
print(soup.prettify())

# You can prettify just a piece of the tree too, not only the whole soup
div = soup.find("div")
print(div.prettify())

# -----------------------------------------------------------

print("\n================= BASIC IDENTITY: name, attrs, string =================")
tag = soup.find("p")
print(tag.name)          # the tag's name, e.g. 'p'
print(tag.attrs)         # ALL attributes as a dict, e.g. {'class': ['intro']}
print(tag.get("class"))  # a single attribute, safely (None if missing)
print(tag.has_attr("class"))       # True/False -> does this tag have this attribute at all?
print(tag.string)         # text content, ONLY if there's exactly one string inside (else None)

# -----------------------------------------------------------

print("\n================= .contents vs .children vs .descendants =================")
div = soup.find("div")

# .contents -> a LIST of direct children only (one level down)
print(div.contents)

# .children -> same direct children, but as an ITERATOR instead of a list
for child in div.children:
    print(repr(child)[:40])   # truncated for readability

# .descendants -> EVERY nested tag/string at ANY depth, not just direct children
print(len(list(div.descendants)))    # much larger count - includes grandchildren too

# -----------------------------------------------------------

print("\n================= .string vs .strings vs .stripped_strings =================")
p_multi = soup.find("p", class_="intro")

print(p_multi.string)              # None here - multiple pieces of text/tags inside, ambiguous
print(list(p_multi.strings))        # ALL text pieces as separate items, including whitespace
print(list(p_multi.stripped_strings))   # same, but whitespace-only entries removed and each stripped

# -----------------------------------------------------------

print("\n================= get_text() — FLATTEN EVERYTHING TO PLAIN TEXT =================")
# get_text() -> collapses a tag AND all its nested tags into one plain string
print(soup.get_text()[:200])                  # whole page as text (messy - little whitespace control)
print(soup.get_text(separator=" ", strip=True)[:200])   # much cleaner: adds spacing, strips extra whitespace

# -----------------------------------------------------------

print("\n================= NAVIGATING SIBLINGS & ELEMENTS =================")
first_li = soup.find("li")
print(first_li.next_sibling)          # whatever comes right after (often whitespace/text)
print(first_li.find_next_sibling("li"))   # the next ACTUAL <li> tag, skipping whitespace
print(first_li.find_previous("h1"))        # nearest <h1> BEFORE this tag, anywhere in the document
print(first_li.parent.name)                 # the tag that directly contains this one

# -----------------------------------------------------------

print("\n================= IDENTIFYING NODE TYPES (Tag vs NavigableString vs Comment) =================")
# Not everything in the tree is a "tag" - some nodes are just text, some are comments
for element in div.contents:
    if isinstance(element, Comment):
        print("COMMENT:", element.strip())
    elif isinstance(element, NavigableString):
        pass   # plain text node - skip printing these, mostly whitespace
    else:
        print("TAG:", element.name)

# -----------------------------------------------------------

print("\n================= FINDING COMMENTS SPECIFICALLY =================")
# Comments are a special string subtype - find them with the Comment class as the filter
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
print(comments)

# -----------------------------------------------------------

print("\n================= find_all() WITH REGEX AND LAMBDA (ADVANCED FILTERS) =================")
import re

# Regex -> match tag names or attribute values with a pattern
headings = soup.find_all(re.compile("^h[1-6]$"))    # matches h1, h2, h3... any heading level
print([h.name for h in headings])

# Lambda -> completely custom filtering logic, e.g. tags that have a specific attribute
tags_with_class = soup.find_all(lambda t: t.has_attr("class"))
print([t.name for t in tags_with_class])

# string= searches by the TEXT content instead of the tag
exact_text = soup.find_all(string="Item one")
print(exact_text)

# -----------------------------------------------------------

print("\n================= COUNTING & PROFILING TAGS (STRUCTURAL ANALYSIS) =================")
# A quick way to "see the shape" of a page: how many of each tag exist
all_tags = soup.find_all(True)             # True -> matches EVERY tag, regardless of name
print(len(all_tags))                        # total tag count

tag_counts = Counter(tag.name for tag in all_tags)
print(tag_counts)                            # e.g. Counter({'p': 2, 'li': 2, 'div': 1, ...})
print(tag_counts.most_common(3))             # the 3 most frequent tag types

# -----------------------------------------------------------

print("\n================= REMOVING JUNK BEFORE ANALYSIS (decompose / extract) =================")
# Scripts/styles are usually noise when you're analyzing visible TEXT content.
# decompose() -> destroys the tag completely, removing it from the tree
soup_clean = BeautifulSoup(html_data, "lxml")
for script_tag in soup_clean.find_all("script"):
    script_tag.decompose()
for style_tag in soup_clean.find_all("style"):
    style_tag.decompose()
print(soup_clean.get_text(separator=" ", strip=True)[:200])   # no more JS code mixed into the text

# extract() -> similar, but RETURNS the removed piece so you can use it separately
soup_extract = BeautifulSoup(html_data, "lxml")
removed_img = soup_extract.find("img").extract()
print(removed_img)                 # the removed tag itself, saved for later use
print(soup_extract.find("img"))     # None now - it's gone from the tree

# -----------------------------------------------------------

print("\n================= INSPECTING META INFORMATION ABOUT THE PAGE =================")
print(soup.title.string if soup.title else None)     # page title
print(soup.find("meta", {"charset": True}))            # the charset meta tag
print(soup.original_encoding)                            # encoding BeautifulSoup detected/assumed

# -----------------------------------------------------------

print("\n================= QUICK ANALYSIS PATTERNS =================")
# Common real checks you'd run when auditing a page:

# 1. Every image missing 'alt' text (accessibility check)
images_missing_alt = [img for img in soup.find_all("img") if not img.get("alt")]
print(f"Images missing alt text: {len(images_missing_alt)}")

# 2. Every link and whether it's internal or external
for link in soup.find_all("a", href=True):
    href = link["href"]
    kind = "external" if href.startswith("http") else "internal"
    print(f"{link.get_text(strip=True)} -> {href} ({kind})")

# 3. Word count of the visible text (rough content-length metric)
visible_word_count = len(soup.get_text(separator=" ", strip=True).split())
print(f"Approx visible word count: {visible_word_count}")

# -----------------------------------------------------------

print("\n================= QUICK METHOD CHEAT SHEET =================")
#   METHOD / PROPERTY              WHAT IT'S FOR
#   ------------------------------  ----------------------------------------------
#   soup.prettify()                   readable, indented HTML string for inspection
#   tag.name / tag.attrs                tag's name / all its attributes as a dict
#   tag.get(attr) / has_attr(attr)        safely read / check for a specific attribute
#   .contents / .children                 direct children only (list vs iterator)
#   .descendants                            EVERY nested element at any depth
#   .string / .strings / .stripped_strings   single text / all text pieces / cleaned text pieces
#   get_text(separator, strip)                flatten a tag + children into plain text
#   .next_sibling / .find_next_sibling()        move sideways in the tree
#   .parent / .find_next() / .find_previous()     move up / forward / backward in the tree
#   isinstance(x, Comment/NavigableString)         tell tags apart from text/comments
#   find_all(re.compile(...))                        regex-based tag/text matching
#   find_all(lambda tag: ...)                          fully custom filter logic
#   find_all(True)                                       every tag on the page
#   decompose() / extract()                               remove a tag (destroy vs. keep it)
#   soup.original_encoding                                   detected character encoding


# ============================================================
# APPLYING THIS TOOLKIT TO A REAL, LIVE HTML PAGE
# Everything above used a small hand-written page so every feature
# was guaranteed to show up. Now the same methods run against an
# actual website - quotes.toscrape.com, a site (like the earlier
# scrapethissite.com) that's built specifically for scraping practice.
# ============================================================
import requests

real_url = "https://quotes.toscrape.com/"

print(f"\n================= FETCHING A REAL PAGE: {real_url} =================")
response = requests.get(real_url, timeout=10)
print(response.status_code)

live_soup = BeautifulSoup(response.text, "lxml")

print("\n================= prettify() ON THE REAL PAGE (first 40 lines) =================")
print("\n".join(live_soup.prettify().splitlines()[:40]))

print("\n================= STRUCTURAL PROFILE OF THE REAL PAGE =================")
live_tags = live_soup.find_all(True)
print("Total tags:", len(live_tags))
print(Counter(t.name for t in live_tags).most_common(10))   # 10 most frequent tag types

print("\n================= EXTRACTING REPEATED CONTENT BLOCKS =================")
# This page repeats the SAME structure for every quote - a perfect real-world
# case for find_all() with a class filter, then looping over each match.
quote_blocks = live_soup.find_all("div", class_="quote")
print(f"Found {len(quote_blocks)} quotes on this page")

for block in quote_blocks[:3]:                     # just the first 3, to keep output short
    text = block.find("span", class_="text").get_text(strip=True)
    author = block.find("small", class_="author").get_text(strip=True)
    tags = [a.get_text(strip=True) for a in block.find_all("a", class_="tag")]
    print(f"{author}: {text}  | tags: {tags}")

print("\n================= LINK ANALYSIS ON THE REAL PAGE =================")
internal, external = 0, 0
for link in live_soup.find_all("a", href=True):
    if link["href"].startswith("http"):
        external += 1
    else:
        internal += 1
print(f"Internal links: {internal}, External links: {external}")

print("\n================= VISIBLE WORD COUNT ON THE REAL PAGE =================")
print(len(live_soup.get_text(separator=" ", strip=True).split()))
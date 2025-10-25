import markdown
import os
import django 
from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension
import xml.etree.ElementTree as etree


class ObsidianImageInlineProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        # m.group(1) contains the captured image filename
        src = m.group(1).strip()
        img = etree.Element("img")
        img.set("src", f"main/static/main/images/{src}")
        img.set("alt", src)
        return img, m.start(0), m.end(0)

class ObsidianImageExtension(Extension):
    def extendMarkdown(self, md):
        # Regex matches: ![[filename or path]]
        OBSIDIAN_IMAGE_RE = r'!\[\[([^\]]+)\]\]'
        md.inlinePatterns.register(ObsidianImageInlineProcessor(OBSIDIAN_IMAGE_RE, md), 'obsidian_image', 175)


class ObsidianLinkInlineProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        src = m.group(1).strip()
        a = etree.Element("a")
        a.set("href", f'post/{src}')
        return a, m.start(0), m.end(0)

class ObsidianLinkExtension(Extension):
    def extendMarkdown(self, md):
        OBSIDIAN_LINK_RE = r'\[\[([^\]]+)\]\]'
        md.inlinePatterns.register(ObsidianLinkInlineProcessor(OBSIDIAN_LINK_RE, md), 'obsidian_link', 174)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bloggy.settings')
django.setup()

from django.templatetags.static import static
from main.models import Page, Post

foldername = 'inbox'


def upload_post(foldername): 
    for post in os.listdir(f'main/{foldername}'):
        # process the post data
        post = Post.objects.create(title=post)
        for page in os.listdir(f'main/{foldername}/{post}'):
            if page.endswith('.md'):
                np = Page.objects.create(
                    post=post,
                    content=translate(open(f'main/{foldername}/{post}/{page}', 'r').read()),
                )   
            else: # static folder
                os.rename(f'main/{foldername}/{post}/static', f'/static/main/images/')
        
    # Grab staticfiles n shiz

    
def translate(md_content):  
    print("Translating markdown content...")
    html_content = markdown.markdown(md_content, extensions=[ObsidianImageExtension(), ObsidianLinkExtension()])
    return html_content


if __name__ == "__main__":
   upload_post('inbox')

 


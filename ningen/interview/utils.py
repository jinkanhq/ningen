import markdown as md
from markdown.extensions import Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree

from ningen.interview.models import Item

# 老式链接 [Item Name][item-slug]
OLD_ITEM_LINK_RE = r'\[([^\[\]\(\)]+)\]\[([^\[\]\(\)]+)\]'

# 新式链接 [[item-slug]]
ITEM_LINK_RE = r'\[\[([a-z0-9\-^\[\]\(\)]+)\]\]'


class OldItemLinkPattern(Pattern):
    def handleMatch(self, m):
        el = etree.Element("a")
        item_slug = m.group(3)
        item_name = m.group(2)
        el.set('target', '_blank')
        el.set('class', 'item')
        el.text = item_name
        try:
            item = Item.objects.get(slug=item_slug)
            el.set("href", item.link)
            el.set("title", item.get_full_name())
        except Item.DoesNotExist:
            Item.objects.create(
                slug=item_slug, name=item_name, vendor='Unknown',
                description='(Markdown generated)', link='javascript:;')
            el.set("href", "#")
        return el


class ItemLinkPattern(Pattern):
    def handleMatch(self, m):
        el = etree.Element("a")
        el.set('target', '_blank')
        el.set('class', 'item')
        item_slug = m.group(2)
        try:
            item = Item.objects.get(slug=item_slug)
            el.text = item.get_full_name()
            el.set("href", item.link)
            el.set("title", item.get_full_name())
        except Item.DoesNotExist:
            Item.objects.create(
                slug=item_slug, name=item_slug, vendor='Unknown',
                description='(Markdown generated)', link='javascript:;')
            el.set("href", "#")
        return el


class NingenExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns.add(
            'itemlink_old', OldItemLinkPattern(OLD_ITEM_LINK_RE, md), '<reference')
        md.inlinePatterns.add(
            'itemlink', ItemLinkPattern(ITEM_LINK_RE, md), '<reference'
        )


ningen_markdown = md.Markdown(extensions=[NingenExtension()])

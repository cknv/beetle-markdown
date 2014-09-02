import markdown
from beetle.context import content_renderer, writer

def render_markdown(raw_content):
    return markdown.markdown(raw_content)

def register(plugin_config, beetle_config):
    markdown_extentions = ['md', 'mkd', 'markdown']
    content_renderer.add_renderer(markdown_extentions, render_markdown)

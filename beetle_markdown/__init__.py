import markdown


def render_markdown(raw_content):
    return markdown.markdown(raw_content)


def register(plugin_config, config, commander, builder, content_renderer):
    markdown_extentions = ['md', 'mkd', 'markdown']
    content_renderer.add_renderer(markdown_extentions, render_markdown)

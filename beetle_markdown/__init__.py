import markdown


def render_markdown(raw_content):
    return markdown.markdown(raw_content)


def register(ctx, plugin_config):
    markdown_extentions = ['md', 'mkd', 'markdown']
    ctx.content_renderer.add_renderer(markdown_extentions, render_markdown)

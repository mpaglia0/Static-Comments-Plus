Enhanced Static Comments
------------------------

An advanced, more complete version of Pelican [Static Comments](https://github.com/getpelican/pelican-plugins/tree/master/static_comments) plugin.

>:warning: Needs a hosting server with PHP!

This plugin allows you to add static comments to an article. By default the
plugin looks for the comments of each article in a local file named
``Pelican_root_dir/comments/{slug}.md/rst``, where ``{slug}`` is the value of the slug tag for the
article. The comments file should be formatted using ``markdown`` (.md) or ``reST`` (.rst).

The comment will be delivered to your mailbox and you have to add it to the a.m. file. Basically it is
the same logic of a moderation queue.

Set the ``STATIC_COMMENTS`` parameter to True to enable the plugin. Default is
False.

Set the ``STATIC_COMMENTS_DIR`` parameter to the directory where the comments
are located. Default is ``comments``.

Set the ``STATIC_COMMENTS_FMT`` parameter to ``rst`` if you will use reST for formatting, 
or ``md`` if you will format comments using markdown. Default is ``rst``.

On the template side, you just have to add a section for the comments to your
``article.html``, as in this example:

    {% if STATIC_COMMENTS %}
      {% if article.metadata.static_comments %}
        <section id="comments" class="body">
        <h2>{{ 'Comments'|gettext(DEFAULT_LANG) }}</h2>
        {{ article.metadata.static_comments }}
        </section>
      {% elif %}
        <h2>{{ 'Would you like to be the first to leave a comment?'|gettext(DEFAULT_LANG) }}</h2>
      {% endif %}
    {% endif %}

Here is an example of usage:

TODO

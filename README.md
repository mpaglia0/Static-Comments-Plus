## Static Comments Plus

A more complete version of Pelican [Static Comments](https://github.com/getpelican/pelican-plugins/tree/master/static_comments) plugin.

>:warning: a PHP capable hosting server is needed if you desire to use the send-comment utility!

This plugin allows you to add static comments to articles.

By default the plugin looks for any comments of each article in a local file named
``Pelican_root_dir/comments/{slug}.md or .rst``, where ``{slug}`` is the value of the slug tag for the
article. The comment files should be formatted using ``markdown`` (.md) or ``reST`` (.rst).

Users comments can be delivered to your mailbox (a PHP capable server needed) and you have to add it manually to the a.m. file. Basically it is
the same logic of a moderation queue...

The plugin can be activated setting the parameter ``STATIC_COMMENTS_PLS`` to ``True``.

Set the ``STATIC_COMMENTS_DIR`` parameter to the directory path where comments
are located. Default is ``comments``.

Set the ``STATIC_COMMENTS_SOURCE`` parameter to ``MD`` if you prefer to use Markdown for formatting. Default is ``RST``.

### PHP comment delivery and HTML form

In order to use the PHP part of this plugin you need to copy ``static/php/send-comment.php`` file into your theme folder and configure ``send-comments.php`` changing ``$to = 'yourname@yourdomain.com';`` with the real email address that should receive comments.

Then you need to configure your ``article.html`` template adding - before the footer - a piece of code similar to:

```python
{% if STATIC_COMMENTS_PLS and article.status != "draft" %}
   {% include comments.html %}
{% endif %}
```
Your ``comments.html`` will be something similar to this:

```python
<section id="comments" class="body">
  <h3>{{ 'Comments'|gettext(DEFAULT_LANG) }}</h3>
  {{ article.metadata.static_comments }}
  <hr>
  {% include comments_form.html %}
</section>
```

and, finally, your ``comments_form.html`` should be similar to

```python
<form action="script.php">
       <input type="hidden" id="title" name="title" value="{{ article.metadata.title }}" readonly><br>
    <label for="fname">{{ 'Name'|gettext(DEFAULT_LANG) }}:</label><br>
       <input type="text" id="fname" name="fname" required><br>
       <small>{{ 'This field is mandatory'|gettext(DEFAULT_LANG) }}</small><br><br>
    <label for="web">{{ 'Website'|gettext(DEFAULT_LANG) }}:</label><br>
       <input type="text" id="web" name="web"><br>{{ 'Submit'|gettext(DEFAULT_LANG) }}">
</form>
```

A working example can be found in [Pelican **Iudas** theme](https://github.com/mpaglia0/Iudas)

Enjoy!

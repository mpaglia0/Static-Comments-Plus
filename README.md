## Static Comments Plus

An advanced, more complete version of Pelican [Static Comments](https://github.com/getpelican/pelican-plugins/tree/master/static_comments) plugin.

>:warning: a PHP capable hosting server is needed!

This plugin allows you to add static comments to an article.

By default the plugin looks for the comments of each article in a local file named
``Pelican_root_dir/comments/{slug}.md/rst``, where ``{slug}`` is the value of the slug tag for the
article. The comments file should be formatted using ``markdown`` (.md) or ``reST`` (.rst).

The comment will be delivered to your mailbox (a PHP capable server needed) and you have to add it manually to the a.m. file. Basically it is
the same logic of a moderation queue...

The plugin can be activated setting the parameter ``STATIC_COMMENTS_PLS`` to ``True``.

Set the ``STATIC_COMMENTS_DIR`` parameter to the directory path where comments
are located. Default is ``comments``.

Set the ``STATIC_COMMENTS_FMT`` parameter to ``.md`` if you prefer to use markdown for formatting. Default is ``.rst`` (Note the initial dot!).

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

and your ``comments_form.html`` should be similar to

```python
<form action="script.php">
       <input type="hidden" id="title" name="title" value="{{ article.metadata.title }}" readonly><br>
    <label for="fname">Name:</label><br>
       <input type="text" id="fname" name="fname" required><br>
       <small>This field is mandatory</small><br><br>
    <label for="web">Website:</label><br>
       <input type="text" id="web" name="web"><br>
       <small>This field is optional</small><br><br>
    <label for="msg">Comment:</label><br>
       <input type="text" id="msg" name="msg" required><br>
       <small>This field is mandatory</small><br><br>
    <input type="submit" value="Submit">
</form>
```

A working example can be found in Pelican [**Z theme**](https://github.com/mpaglia0/Z)

Enjoy!

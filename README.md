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

In order to use the PHP part of this plugin you need to copy and configure the ``static/php/send-comment.php`` file as follows:

TODO

Here is an example of usage:

TODO

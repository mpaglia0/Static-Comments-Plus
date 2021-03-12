##Static Comments Plus

An advanced, more complete version of Pelican [Static Comments](https://github.com/getpelican/pelican-plugins/tree/master/static_comments) plugin.

>:warning: If you plan to use the 'send form' function, a PHP capable hosting server is needed!

This plugin allows you to add static comments to an article.

By default the plugin looks for the comments of each article in a local file named
``Pelican_root_dir/comments/{slug}.md/rst``, where ``{slug}`` is the value of the slug tag for the
article. The comments file should be formatted using ``markdown`` (.md) or ``reST`` (.rst).

The comment will be delivered to your mailbox (optional: PHP capable server needed) and you have to add it manually to the a.m. file. Basically it is
the same logic of a moderation queue... Viceversa, you can ask your visitors to send comments via email like Static Comments default behaviour.

PHP function and HTML form can be activated setting the parameter ``STATIC_COMMENTS_ACT`` to ``True``.

Set the ``STATIC_COMMENTS`` parameter to ``True`` to enable the plugin. Default is
``False``.

Set the ``STATIC_COMMENTS_DIR`` parameter to the directory path where comments
are located. Default is ``comments``.

Set the ``STATIC_COMMENTS_FMT`` parameter to ``md`` if you prefer to use markdown for formatting. Default is ``rst``.

### PHP comment delivery and HTML form

If you want to use the PHP part of this plugin you need to copy and configure the ``static/php/send-comment.php`` file.

TODO: fix the following in order to automate all the procedure...

Here is an example of usage:

TODO

# -*- coding: utf-8 -*-

import codecs
import logging
import markdown
import os

logger = logging.getLogger(__name__)

from pelican import signals
from pelican.readers import RstReader


def initialized(pelican):
    from pelican.settings import DEFAULT_CONFIG
    DEFAULT_CONFIG.setdefault('STATIC_COMMENTS_PLUS', False)
    DEFAULT_CONFIG.setdefault('STATIC_COMMENTS_DIR' 'comments')
    if pelican:
        pelican.settings.setdefault('STATIC_COMMENTS_PLUS', False)
        pelican.settings.setdefault('STATIC_COMMENTS_DIR', 'comments')


def add_static_comments(gen, metadata):
    if gen.settings['STATIC_COMMENTS_PLUS'] != True:
        logger.info("Static_Comments_Plus: plugin is not enabled...")
        return

    if not 'slug' in metadata:
        logger.warning("Static_Comments_Plus: "
                "cant't locate comments file without slug tag in the article!")
        
    no_comment_msg = "Static_Comments_Plus: NO comments file for ... " + metadata['slug']
    
    parse_mode = gen.settings.get('STATIC_COMMENTS_SOURCE', 'MD')
    if parse_mode not in ['RST', 'MD']:
        logger.warning("Static_Comments_Plus: "
                "Invalid option {} as the plugin option... "
                "STATIC_COMMENTS_SOURCE can only be set to MD or RST. Defaulting to MD".format(parse_mode))
    if parse_mode == 'RST':
        logger.info('Static_Comments_Plus: comment parser is set to RST')
        fname = os.path.join(gen.settings['STATIC_COMMENTS_DIR'], metadata['slug'] + ".rst")
        if not os.path.exists(fname):
            logger.info(no_comment_msg)
            return
        reader = RstReader(settings=gen.settings)
        html, _ = reader.read(source_path=fname)
        logger.info("Static_Comments_Plus: RST comment file opened")

    else:  # the default parser is Markdown parser, hence 'MD'
        fname = os.path.join(gen.settings['STATIC_COMMENTS_DIR'], metadata['slug'] + ".md")
        logger.info('Static_Comments_Plus: comment parser is set to MD')
        if not os.path.exists(fname):
            logger.info(no_comment_msg)
            return
        input_file = codecs.open(fname, mode="r", encoding="utf-8")
        logger.info("Static_Comments_Plus: MD comment file opened")
        text = input_file.read()
        html = markdown.markdown(text)

    # logger.info(html)
    metadata['static_comments'] = html


def register():
    signals.initialized.connect(initialized)
    signals.article_generator_context.connect(add_static_comments)

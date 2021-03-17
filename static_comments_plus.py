# -*- coding: utf-8 -*-

import codecs
import logging
import os

logger = logging.getLogger(__name__)

from pelican import signals


def initialized(pelican):
    from pelican.settings import DEFAULT_CONFIG
    DEFAULT_CONFIG.setdefault('STATIC_COMMENTS_PLS', False)
    DEFAULT_CONFIG.setdefault('STATIC_COMMENTS_DIR' 'comments')
    DEFAULT_CONFIG.setdefault('STATIC_COMMENTS_EXT' '.rst')
    if pelican:
        pelican.settings.setdefault('STATIC_COMMENTS_PLS', False)
        pelican.settings.setdefault('STATIC_COMMENTS_DIR', 'comments')
        pelican.settings.setdefault('STATIC_COMMENTS_EXT', '.rst')       

def add_static_comments(gen, metadata):
  
    if gen.settings['STATIC_COMMENTS_PLS'] != True:
        logger.warning("static_comments_plus: "
                "Static Comments Plus plugin is installed but NOT activated...")
        return

    if not 'slug' in metadata:
        logger.warning("static_comments_plus: "
                "cant't locate comments file without slug tag in the article...")
        return

    fname = os.path.join(gen.settings['STATIC_COMMENTS_DIR'],metadata['slug'],gen.settings['STATIC_COMMENTS_EXT'])

    if not os.path.exists(fname):
        logger.warning("static_comments_plus: "
                "cant't locate comments path! Please check your configuration parameters...")
        return

    if gen.settings['STATIC_COMMENTS_EXT'] == ".md":
        import markdown 
    
    input_file = codecs.open(fname, mode="r", encoding="utf-8")
    text = input_file.read()
    html = markdown.markdown(text)   #TODO: do the same for reST
    metadata['static_comments'] = html


def register():
    signals.initialized.connect(initialized)
    signals.article_generator_context.connect(add_static_comments)

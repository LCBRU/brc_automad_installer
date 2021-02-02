#!/usr/bin/env python3

import wget
import shutil
import zipfile
import tempfile
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()


WWW_DIR=os.getenv('WWW_DIR', "/local/www/")
HTTP_DIR=os.path.join(WWW_DIR, os.getenv('HTTP_DIR', "htdocs"))
SITE_NAME=os.path.join(WWW_DIR, os.getenv('SITE_NAME', "BRC"))


def get_automad():
    pwd = os.path.realpath('.')

    with tempfile.TemporaryDirectory() as tmpdirname:
        os.chdir(tmpdirname)

        automad_zip = wget.download('https://automad.org/download', bar=None)

        with zipfile.ZipFile(automad_zip,"r") as zip_ref:
            zip_ref.extractall(tmpdirname)

        extracted_dir = next(x for x in Path(tmpdirname).iterdir() if x.is_dir())

        if os.path.exists(os.path.join(HTTP_DIR, 'cache')):
            os.unlink(os.path.join(HTTP_DIR, 'cache'))
        if os.path.exists(os.path.join(HTTP_DIR, 'pages')):
            os.unlink(os.path.join(HTTP_DIR, 'pages'))
        if os.path.exists(os.path.join(HTTP_DIR, 'config')):
            os.unlink(os.path.join(HTTP_DIR, 'config'))

        shutil.rmtree(HTTP_DIR)
        shutil.copytree(extracted_dir.name, HTTP_DIR)

    shutil.rmtree(os.path.join(HTTP_DIR, 'cache'))
    shutil.rmtree(os.path.join(HTTP_DIR, 'pages'))
    shutil.rmtree(os.path.join(HTTP_DIR, 'config'))
    shutil.rmtree(os.path.join(HTTP_DIR, 'shared'))

    if not os.path.exists(os.path.join(WWW_DIR, 'cache')):
        os.mkdir(os.path.join(WWW_DIR, 'cache'))
    if not os.path.exists(os.path.join(WWW_DIR, 'pages')):
        os.mkdir(os.path.join(WWW_DIR, 'pages'))
    if not os.path.exists(os.path.join(WWW_DIR, 'config')):
        os.mkdir(os.path.join(WWW_DIR, 'config'))
    if not os.path.exists(os.path.join(WWW_DIR, 'shared')):
        os.mkdir(os.path.join(WWW_DIR, 'shared'))

    if not os.path.exists(os.path.join(WWW_DIR, 'shared', 'data.txt')):
        with open(os.path.join(WWW_DIR, 'shared', 'data.txt'), 'w') as writer:
            writer.writelines('''
sitename: {}
-
theme: brc_automad_theme
-
appleTouchIcon: /shared/apple-touch-icon.png
-
favicon: /shared/favicon.ico
-
urlSearchResults: /
-
urlTutorials: /tutorials
            '''.format(SITE_NAME))


    if not os.path.exists(os.path.join(WWW_DIR, 'pages', 'basic.txt')):
        with open(os.path.join(WWW_DIR, 'pages', 'basic.txt'), 'w') as writer:
            writer.writelines('')

    os.symlink(os.path.join(WWW_DIR, 'cache'), os.path.join(HTTP_DIR, 'cache'))
    os.symlink(os.path.join(WWW_DIR, 'pages'), os.path.join(HTTP_DIR, 'pages'))
    os.symlink(os.path.join(WWW_DIR, 'config'), os.path.join(HTTP_DIR, 'config'))
    os.symlink(os.path.join(WWW_DIR, 'shared'), os.path.join(HTTP_DIR, 'shared'))

    shutil.rmtree(os.path.join(HTTP_DIR, 'packages'))
    os.mkdir(os.path.join(HTTP_DIR, 'packages'))

    with tempfile.TemporaryDirectory() as tmpdirname:
        os.chdir(tmpdirname)

        theme_zip = wget.download('https://github.com/LCBRU/brc_automad_theme/archive/master.zip', bar=None)

        with zipfile.ZipFile(theme_zip,"r") as zip_ref:
            zip_ref.extractall(tmpdirname)

        extracted_dir = next(x for x in Path(tmpdirname).iterdir() if x.is_dir())
        shutil.copytree(extracted_dir.name, os.path.join(HTTP_DIR, 'packages/brc_automad_theme'))


get_automad()
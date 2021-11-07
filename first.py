# -*- coding: utf-8 -*-

from pathlib import Path

base = Path('d:\\Akari\\Фото\\с телефона\\')
filelist = list(base.glob('*.jpg'))
print (filelist)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
from browser import document, alert

hashObj = hashlib.md5()

def encrypt(ev):
    getVal = document["hoge"].value

    """hashlibでは文字列が渡された時にUnicode化しないため
    入力値取得後予めencodeしておく"""
    hashObj.update(getVal.encode('utf-8'))

    ango = hashObj.hexdigest()
    rslt = document["result"]
    rslt.text = ango

execute_btn = document["execute"]
execute_btn.bind("click",encrypt)

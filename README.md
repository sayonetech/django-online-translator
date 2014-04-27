Django-online-translator-
==========================

A Django Based system that will help you to translate the content from english to any other language using Microsoft Bing Translation Service 

## Requirements:
    python 2.7+
    python-requests   http://docs.python-requests.org/en/latest/user/install/
    Get clientID and clientSecret from Bing: https://www.microsoft.com/web/post/using-the-free-bing-translation-apis

## Usage:

    from translator import BingTranslator

    translator = BingTranslator(CLIENT_ID,CLIENT_SECRET)
    translated = translator.translate(TEXT_STRING,FROM_LANG_CODE,TO_LANG_CODE) 


## Bing Language Codes:
    http://msdn.microsoft.com/en-us/library/hh456380.aspx

kibrit
======

A git version parser


Installation:
------------

To install kibrit place it on your requirements pip. It requires no special dependencies.

you also need to have 

    'django.core.context_processors.request',

in your TEMPLATE_CONTEXT_PROCESSORS and kibrit in your INSTALLED_APPS

The package can try to detect .git in your project automatically but it is best if you explicitly set

KIBRIT_PATH in your settings to where the .git file is in your project.

This is a nice resource for people learning from the DJANGOBOOK.COM onlint tutorial.

If you have some working knowledge of MVC from other frameworks it might be easiest to pull this code, and skip chapters 1-5.

Basic Start Commands:

To build a basic framework:
django-admin.py startproject sitename

To run the project:
python manage.py runserver

Regex Tips when configuring URLS

The pattern includes a caret (^) and a dollar sign ($). These are regular expression characters that have a special meaning:
the caret means “require that the pattern matches the start of the string,”
and the dollar sign means “require that the pattern matches the end of the string.”

This concept is best explained by example. If we had instead used the pattern '^hello/'
(without a dollar sign at the end), then any URL starting with /hello/ would match,
such as /hello/foo and /hello/bar, not just /hello/. Similarly, if we had left off the 
initial caret character (i.e., 'hello/$'), Django would match any URL that ends with hello/, 
such as /foo/bar/hello/. If we had simply used hello/, without a caret or dollar sign, then 
any URL containing hello/ would match, such as /foo/hello/bar. Thus, we use both the caret 
and dollar sign to ensure that only the URL /hello/ matches – nothing more, nothing less.

For more on regular expressions, see http://www.djangoproject.com/r/python/re-module/.

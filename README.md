DjangoApp2
==========

Learning Django Book, App

lThis is a nice resource for people learning from the DJANGOBOOK.COM online tutorial.

If you have some working knowledge of MVC from other frameworks it might be easiest to pull this code, and skip chapters 1-5.


Basic Start Commands:

To build a basic framework:
django-admin.py startproject sitename

To run the project:
python manage.py runserver



Regex Tips when configuring URLS:

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


Templates:
Those are the fundamentals of using the Django template system: just write a template string, create a Template object, create a Context, and call the render() method.

* When setting a path to templates, use nifty python instead of the exact path:
import os.path
    os.path.join(os.path.dirname(__file__), 'templates').replace('\\', '/'),

Storing templates in subdirectories of your template directory is easy. In your calls to get_template(), just include the subdirectory name and a slash before the template name, like so:

t = get_template('dateapp/current_datetime.html')
Because render() is a small wrapper around get_template(), you can do the same thing with the second argument to render(), like this:

return render(request, 'dateapp/current_datetime.html', {'current_date': now})
There’s no limit to the depth of your subdirectory tree. Feel free to use as many subdirectories as you like.

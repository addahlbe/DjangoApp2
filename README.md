DjangoApp2
==========

Learning Django Book, App

This is a nice resource for people learning from the DJANGOBOOK.COM online tutorial.

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

You can use as many levels of inheritance as needed. One common way of using inheritance is the following three-level approach:

Create a base.html template that holds the main look and feel of your site. This is the stuff that rarely, if ever, changes.
Create a base_SECTION.html template for each “section” of your site (e.g., base_photos.html and base_forum.html). These templates extend base.html and include section-specific styles/design.
Create individual templates for each type of page, such as a forum page or a photo gallery. These templates extend the appropriate section template.
This approach maximizes code reuse and makes it easy to add items to shared areas, such as section-wide navigation.

This approach maximizes code reuse and makes it easy to add items to shared areas, such as section-wide navigation.

Here are some guidelines for working with template inheritance:

If you use {% extends %} in a template, it must be the first template tag in that template. Otherwise, template inheritance won’t work.
Generally, the more {% block %} tags in your base templates, the better. Remember, child templates don’t have to define all parent blocks, so you can fill in reasonable defaults in a number of blocks, and then define only the ones you need in the child templates. It’s better to have more hooks than fewer hooks.
If you find yourself duplicating code in a number of templates, it probably means you should move that code to a {% block %} in a parent template.
If you need to get the content of the block from the parent template, use {{ block.super }}, which is a “magic” variable providing the rendered text of the parent template. This is useful if you want to add to the contents of a parent block instead of completely overriding it.
You may not define multiple {% block %} tags with the same name in the same template. This limitation exists because a block tag works in “both” directions. That is, a block tag doesn’t just provide a hole to fill, it also defines the content that fills the hole in the parent. If there were two similarly named {% block %} tags in a template, that template’s parent wouldn’t know which one of the blocks’ content to use.
The template name you pass to {% extends %} is loaded using the same method that get_template() uses. That is, the template name is appended to your TEMPLATE_DIRS setting.
In most cases, the argument to {% extends %} will be a string, but it can also be a variable, if you don’t know the name of the parent template until runtime. This lets you do some cool, dynamic stuff.


MVC: data access logic, business logic, and presentation logic – comprise a concept that’s sometimes called the Model-View-Controller (MVC) pattern of software architecture. In this pattern, “Model” refers to the data access layer, “View” refers to the part of the system that selects what to display and how to display it, and “Controller” refers to the part of the system that decides which view to use, depending on user input, accessing the model as needed.

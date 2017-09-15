This repository uses defaults imported from outsideContextSolutions. These
differ from django in a number of ways. If you're a django developer, here's
what you need to know.

#Goals

Very flexable user accounts

Define-once, use-many architecture (start with defining a django-rest-framework
endpoint, then wrap some html views around it)


#Quickstarts

We use jinja2 templates, not django templates. You should too, since
communication between the two isn't great. Just name your template `*.j2.html`
to use jinja2 instead of django.

We use django-pipeline for compiling static assets, and bower for managing
vendor files. You need to make sure some utilities are in your path, install
them through your package manager or do

```
sudo npm -g install yuglify
sudo npm -g install --save-dev babel-cli babel-preset-env
sudo gem install sass --no-user-install
```

ToDo:
We use [polyfilled flif](https://github.com/UprootLabs/poly-flif) for responsive
images, with a fallback to png. Instead of using an `<img>` tag, use

```jinja2
{% from 'ocsUtils.j2.html' import Img %}

{{Img('imagePath')}} #For static images
{{Img(ImgObject)}} #For objects that implement a .url method, like FileFields
```

# {{ title }}

```{toctree}
---
caption: {{ title }}
titlesonly: true
maxdepth: 1
---
{% for path in files %}
{{ path }}
{% endfor %}
```


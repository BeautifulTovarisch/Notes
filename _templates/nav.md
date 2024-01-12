# {{ title }}

```{toctree}
---
caption: {{ title }}
titlesonly: true
---
{% for path in files %}
{{ path }}
{% endfor %}
```


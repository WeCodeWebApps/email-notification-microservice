from typing import List
from django.utils import timezone


def get_default_args(tz: str = None, **kwargs) -> dict:
    return dict(time=timezone.localtime(timezone=tz), **kwargs)


def format_template(template, **kwargs) -> str:
    assert template is not None, "template object is none."

    text: str = template.text
    args = get_default_args(**kwargs)

    return text.format(**args)

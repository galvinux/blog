#!/usr/bin/env python


from typing import List, Optional
from datetime import datetime

import random


SOCIAL_IMAGE_TEMPLATE = 'socialImage: "/media/{}"'
HEADER_TEMPLATE = """
---
title: "{}"
date: "{}"
template: "post"
draft: false
slug: "{}"
category: "{}"
tags:
  - "Anuncios"
description: "{}"
{}
---
"""

FIGURE_TEMPLATE = """
<figure class="float-right" style="width: 240px">                                      |~                                                                                     
        <img src="{}" alt="">                                     |~                                                                                     
        <figcaption></figcaption>                                                |~                                                                                     
</figure>
"""

CATEGORIES = {
    1: "Anuncios",
    2: "Reuniones",
}


def _get_current_time() -> str:
    """Return current time as a str."""
    return datetime.now().strftime("%FT%H:%M:%S")


def _get_slug(title: str) -> str:
    """Slugify given title."""
    seed = f"{title}{_get_current_time()}"
    random.seed(seed) 
    postfix = str(random.random())[-4:]
    return title.replace(" ", "-") + f"-{postfix}".lower()


def _get_category(category: int) -> str:
    return CATEGORIES[category]


def _make_header(title: str, category: int, description: str, slug: str, image_file_name: Optional[str] = None) -> str:
    """Return a post header."""

    current_date = _get_current_time()
    category = _get_category(category)
    social_image = SOCIAL_IMAGE_TEMPLATE.format(image_file_name) if image_file_name else ""
    header = HEADER_TEMPLATE.format(title, current_date, slug, category, description, social_image)

    if social_image:
        figure_template = FIGURE_TEMPLATE.format(social_image)
        header += figure_template

    return header


def _get_filename(slug) -> str:
    """Return blog filename."""
    return f"{datetime.now().strftime('%Y-%m-%d')}---{slug}.md"


def make_new_post(title: str, category: int, description: str):
    """Creates a new post."""
    slug = _get_slug(title)
    header = _make_header(title, category, description, slug)
    filename = _get_filename(slug)
    with open(filename, "w") as fp:
        fp.write(header)
    print(f"Created {filename}")


if __name__ == "__main__":
    title = input("Title: ")
    print(f"Available categories: ${CATEGORIES}")
    category = input("Category number: ")
    description = input("Description: ")
    make_new_post(title, int(category), description)
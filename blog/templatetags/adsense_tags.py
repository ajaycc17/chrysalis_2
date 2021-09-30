from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.filter
def inarticle_ads(value):
    # Render the adsense code placed in html files
    ad_code = []
    ad_code.append(render_to_string("adsense/inarticle1.html"))
    ad_code.append(render_to_string("adsense/inarticle2.html"))
    ad_code.append(render_to_string("adsense/inarticle3.html"))
    ad_code.append(render_to_string("adsense/inarticle4.html"))
    ad_code.append(render_to_string("adsense/inarticle5.html"))
    ad_code.append(render_to_string("adsense/inarticle6.html"))

    # set adcode picker
    j = 0

    # Break down content into paragraphs
    paragraphs = value.split("</p>")

    # insert after every 7th paragraph
    for i in range(len(paragraphs)):
        if i % 7 == 0:
            if i == 0:
                continue
            paragraphs[i] = paragraphs[i] + "<p>" + ad_code[j] + "</p>"
            if j < 5:
                j += 1
            value = "</p>".join(paragraphs)
    return value

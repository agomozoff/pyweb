from horoscope import generated_prophecies
from datetime import datetime as dt
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


def generate_page(head, body):
    page = f"""<html>
    {head}
    {body}
    </html>"""
    return page


def generate_head(title):
    head = f"<title>{title}</title>"
    return f"<head>{head}</head>"


def generate_body(header, paragraphs):
    body = f"<h1>{header}</h1>\n"
    # i = 0
    # while i < len(paragraphs):
    #     body += f"<p>{paragraphs[i]}</p>\n"
    #     i = i + 1
    for p in paragraphs:
        body += f"<p>{p}</p>\n"
    return f"<body>{body}</body>"


def save_page(title_s_p, header_s_p, paragraphs_s_p, output="index.html"):
    fp = open(output, "w")
    page = generate_page(generate_head(title=title_s_p), generate_body(
        header=header_s_p, paragraphs=paragraphs_s_p))
    print(page, file=fp)
    fp.close()


today = dt.now().date()
save_page(title_s_p="Гороскоп на сегодня ", header_s_p="Что день " + str(today) +
          " готовит", paragraphs_s_p=generated_prophecies(), output="index.html")

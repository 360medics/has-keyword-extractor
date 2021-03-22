import json
import click
from bs4 import BeautifulSoup


def extract_content(content):
    soup = BeautifulSoup(str(content), "html.parser")
    soup_find = soup.find("div", class_="wysiwyg basic")
    if soup_find is not None:
        txt = " ".join(div.text for div in soup_find.findChildren(recursive=True))
        return txt
    return None


@click.command()
@click.option("--input-path", required=True)
@click.option("--output-path", required=True)
def main(input_path, output_path):
    data = {
        d[0]: extract_content(d[1])
        for d in json.load(open(input_path, "r")).items()
    }
    data = {url: content for url, content in data.items() if content is not None}
    json.dump(data, open(output_path, "w"), indent=4, sort_keys=True)


if __name__ == "__main__":
    main()

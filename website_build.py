import os


"""
Python script to generate quickly all the html files needed.
It simplifies a bit handling the headers for example.
Modify the files in the "parts" part and use this script to do the rest. 
"""

prefix = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paul Hilaire's Website</title>
    <link href="styles/style.css" rel="stylesheet" type="text/css" />
    <link
    href="http://fonts.googleapis.com/css?family=Open+Sans"
    rel="stylesheet"
    type="text/css" />
</head>
<body>
<main>
    """

suffix = """

</main>
<script src="./js/script.js"></script>
</body>
</html>
"""


def build_html(
        output_name: str,
        input_part: str,
        headers: str="headers.html",
        prefix: str=prefix,
        suffix: str=suffix
) -> None:
    """Construct a html file from the website out of some parts.
    The structure of the file is the following:
    prefix, parts/headers, path/input_part, Suffix.

    Args:
        output_name (str): The output file name
        input_part (str): The main body of the html file
        headers (str, optional): Header html part. Defaults to "headers.html".
        prefix (str, optional): Prefix of the html file. Defaults to prefix.
        suffix (str, optional): Suffix of the html file. Defaults to suffix.
    """    
    output = prefix
    path = "./parts"
    with open(os.path.join(path, headers), "r") as f:
        for line in f:
            # print(line)
            output += line

    with open(os.path.join(path, input_part), "r") as f:
        for line in f:
            output += line
    output += suffix
    # print(output)
    with open(output_name, "w") as f:
        f.writelines(output)
    pass

if __name__ == "__main__":
    file_list = [
        "index.html",
        "cv.html",
        "research_interests.html",
        "teaching.html",
        "thoughts.html"
    ]

    file_name_list = [
        "index.html",
        "cv.html",
        "research_interests.html",
        "teaching.html",
        "thoughts.html"
    ]

    for ind in range(len(file_name_list)):
        build_html(file_name_list[ind], file_list[ind])

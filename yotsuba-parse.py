import itertools
import sys


# Get the name of the input file
filename = raw_input("Please enter the name of the text (.txt) file to read data from: ")
if filename.endswith(".txt"):
    fname_in = filename
else:
    fname_in = filename + ".txt"
fname_out = filename + ".html"

try:
    with open(fname_out, "w") as f:
        f.write("Yatta!")
except IOError as err:
    print "Output file could not be opened or written to: {}".format(err)
    sys.exit(1)

try:
    with open(fname_in) as f:
        f.readline()
except IOError as err:
    print "Input file could not be opened or read: {}".format(err)
    sys.exit(1)

with open(fname_out, "w") as f_out:

    # Set up the non-dynamic headers and such
    f_out.write("<!doctype html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <title>Yotsubato Vol. 1 Vocabulary</title>\n    <link rel=\"stylesheet\" href=\"yotsuba.css\">\n    <script src=\"http://code.jquery.com/jquery-1.9.1.min.js\"></script>\n    <script src=\"yotsuba.js\"></script>\n</head>\n<body>\n    <table border=\"1\">\n        <tr>\n            <th class=\"col-1\"></th>\n            <th><span class=\"btn top-btn\" onclick=\"hideAll()\">Hide All</span></th>\n            <th><span class=\"btn top-btn all-kana\" onclick=\"showAllKana()\">Show All Kana</span></th>\n            <th><span class=\"btn top-btn all-trans\" onclick=\"showAllTrans()\">Show All Translations</span></th>\n        </tr>\n        <tr>\n            <th class=\"col-1\">Page</th>\n            <th>Kanji</th>\n            <th>Kana</th>\n            <th>Translation</th>\n        </tr>\n")

    i = 0
    with open(fname_in) as f_in:
        for page, kanji, kana, trans in itertools.izip_longest(*[f_in]*4):

            page = page.strip()
            kanji = kanji.strip()
            kana = kana.strip()
            trans = trans.strip()
            i += 1

            # Check for whether the row is a term or page marker
            if page.lower().startswith("page"):
                f_out.write("<tr>\n    <td class=\"col-1\"><a class=\"page\" id=\"page{1}\">{0}</a></td>\n    <td></td>\n    <td></td>\n    <td></td>\n</tr>\n".format(page, page[5:]))
            else:
                f_out.write("<tr class=\"vocab-item\" id=\"{}\">\n    <td class = \"col-1\"></td>\n".format(i))
                if kanji:
                    f_out.write("    <td class><span class=\"kanji\">{}</span></td>\n".format(kanji))
                else:
                    f_out.write("    <td></td>\n")
                f_out.write("    <td><span class=\"kana\">{0}</span></td>\n    <td><span class=\"trans\">{1}</span></td>\n    <td class=\"btn individual-btn\">Show Kana</td>\n</tr>\n".format(kana, trans))

    # Close it all up!
    f_out.write("    </table>\n</body>\n</html>")

import itertools

i = 1

with open('yotsubato.txt') as f:
    for x, y, z in itertools.izip_longest(*[f]*3):

        x = x.strip()
        y = y.strip()
        z = z.strip()
        i += 1
        print "<tr class=\"vocab-item\" id=\"{}\">\n    <td></td>".format(i)
        if x:
            print "    <td><span class=\"kanji\">{}</span></td>".format(x)
        else:
            print "    <td></td>"
        print "    <td><span class=\"kana\">{0}</span></td>\n    <td><span class=\"trans\">{1}</span></td>\n    <td class=\"btn individual-btn\">Show Kana</td>\n</tr>".format(y, z)

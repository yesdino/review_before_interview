class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return

        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w')

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        fout.write("<tr>")

        # 页面文本编码 ascii 需转换编码
        for data in datas:
            fout.write("<td>%s</td>" % data['url'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['first_title'].encode('utf-8'))

        fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
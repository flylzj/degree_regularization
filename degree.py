# coding: utf-8
from enum_pattern import PatternEnum
import csv
import os


class DegreeRegular:
    def _regular(self, text):
        for pattern in list(PatternEnum):
            reg = pattern.regular_text(text)
            if reg:
                return reg

    def regular_text(self, text):
        return self._regular(text)

    def _regular_iter(self, _iter: iter):
        for item in _iter:
            yield self._regular(item)

    def regular_csv(self, filename):
        data = [
            ["in", "regular"]
        ]
        with open(filename) as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) > 0:
                    text = row[0].strip()
                else:
                    continue
                res = [text, self._regular(text)]
                print(res)
                data.append(res)

        outfile = os.path.join(*os.path.split(filename)[:-1], "output-" + os.path.split(filename)[-1])
        with open(outfile, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)


if __name__ == '__main__':
    dr = DegreeRegular()
    infile = "C:\\Users\\liuzhijun01\\Desktop\\2.csv"
    dr.regular_csv(infile)
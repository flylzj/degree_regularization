# coding: utf-8
import re
import csv
import os


class DegreePattern:
    # 博士后
    _POSTDOC_PATTERN = (
        r"(postdoc)",
    )
    # 博士
    _PHD_PATTERN = (
        r"(doctor)", r"(phd)", r"(ph\.d)"
    )
    # 医学博士
    _MD_PATTERN = (
        r"(doctor of medicine)", r"(md)"
    )
    # 法律博士
    _JD_PATTERN = (
        r"(jd)", "(doctor of law)", "(juris)"
    )
    # 工商管理硕士
    _MBA_PATTERN = (
        r"(mba)", r"(master of business administration)"
    )
    # 硕士学位
    _MASTER_PATTERN = (
        r"(master)", r"(ms)",
    )
    # 学士学位
    _BACHELOR_PATTERN = (
        r"(bachelor)", r"(bs)", r"(ba)", r"(b\.s)", r"(b\.a)", r"(b\.e)", "(engineer)"
    )
    # 副学士学位
    _ASSOCIATE_PATTERN = (
        r"(associate)", r"(a\.a\.)"
    )

    patterns = (

        _POSTDOC_PATTERN,

        _JD_PATTERN,

        _MD_PATTERN,

        _PHD_PATTERN,

        _MBA_PATTERN,

        _MASTER_PATTERN,

        _BACHELOR_PATTERN,

        _ASSOCIATE_PATTERN,
    )
    regular_dict = {
        _POSTDOC_PATTERN: "POSTDOC",
        _PHD_PATTERN: "PHD",
        _MD_PATTERN: "MD",
        _JD_PATTERN: "JD",
        _MBA_PATTERN: "MBA",
        _MASTER_PATTERN: "MASTER",
        _BACHELOR_PATTERN: "BACHELOR",
        _ASSOCIATE_PATTERN: "ASSOCIATE",
        "": "没有找到学位"
    }


class DegreeRegular(DegreePattern):
    def _regular(self, text):
        for pattern in self.patterns:
            _pattern = "|".join(pattern)
            res = re.search(_pattern, text, flags=re.IGNORECASE)
            if res:
                return self.regular_dict[pattern]
        return self.regular_dict[""]

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


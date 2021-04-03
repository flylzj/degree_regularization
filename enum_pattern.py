# coding: utf-8
from enum import Enum
import re


class PatternEnum(Enum):
    PostdocPattern = ((r"(postdoc)",), "POSTDOC")
    PhdPattern = ((r"(doctor)", r"(phd)", r"(ph\.d)"), "PHD")
    MdPattern = ((r"(doctor of medicine)", r"(md)"), "MD")
    JdPattern = ((r"(jd)", "(doctor of law)", "(juris)"), "JD")
    MbaPattern = ((r"(mba)", r"(master of business administration)"), "MBA")
    MasterPattern = ((r"(master)", r"(ms)",), "MASTER")
    BachelorPattern = ((r"(bachelor)", r"(bs)", r"(ba)", r"(b\.s)", r"(b\.a)", r"(b\.e)", "(engineer)"), "BACHELOR")
    AssociatePattern = ((r"(associate)", r"(a\.a\.)"), "ASSOCIATE")
    UnknownPattern = ((r"", ), "未找到学位")

    def __init__(self, pattern, regular):
        self.prog = re.compile("|".join(pattern), flags=re.IGNORECASE)
        self.regular = regular

    def regular_text(self, text):
        if self.prog.search(text):
            return self.regular

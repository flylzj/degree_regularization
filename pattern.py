# coding: utf-8
import re


UNKNOWN_REGULAR = "未找到学位"


class Pattern:
    pattern = ()
    regular = ""

    def __init__(self):
        self.prog = re.compile("|".join(self.pattern), flags=re.IGNORECASE)

    def regular_text(self, text):
        if self.prog.search(text):
            return self.regular


# 博士后
class PostdocPattern(Pattern):
    pattern = (
        r"(postdoc)",
    )

    regular = "POSTDOC"

    def __init__(self):
        super(PostdocPattern, self).__init__()


# 博士
class PhdPattern(Pattern):
    pattern = (
        r"(doctor)", r"(phd)", r"(ph\.d)"
    )
    regular = "PHD"

    def __init__(self):
        super(PhdPattern, self).__init__()


# 医学博士
class MdPattern(Pattern):
    pattern = (
        r"(doctor of medicine)", r"(md)"
    )
    regular = "MD"

    def __init__(self):
        super(MdPattern, self).__init__()


# 法律博士
class JdPattern(Pattern):
    pattern = (
        r"(jd)", "(doctor of law)", "(juris)"
    )
    regular = "JD"

    def __init__(self):
        super(JdPattern, self).__init__()


# 工商管理硕士
class MbaPattern(Pattern):
    pattern = (
        r"(mba)", r"(master of business administration)"
    )
    regular = "MBA"

    def __init__(self):
        super(MbaPattern, self).__init__()


# 硕士学位
class MasterPattern(Pattern):
    pattern = (
        r"(master)", r"(ms)",
    )
    regular = "MASTER"

    def __init__(self):
        super(MasterPattern, self).__init__()


# 学士学位
class BachelorPattern(Pattern):
    pattern = (
        r"(bachelor)", r"(bs)", r"(ba)", r"(b\.s)", r"(b\.a)", r"(b\.e)", "(engineer)"
    )
    regular = "BACHELOR"

    def __init__(self):
        super(BachelorPattern, self).__init__()


# 副学士学位
class AssociatePattern(Pattern):
    pattern = (
        r"(associate)", r"(a\.a\.)"
    )
    regular = "ASSOCIATE"

    def __init__(self):
        super(AssociatePattern, self).__init__()


class DegreePattern:
    def __init__(self):
        self.patterns = (
            PostdocPattern(),
            PhdPattern(),
            MdPattern(),
            JdPattern(),
            MbaPattern(),
            MasterPattern(),
            BachelorPattern(),
            AssociatePattern()
        )

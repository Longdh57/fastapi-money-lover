import enum


class CategoryType(str, enum.Enum):
    KHOAN_CHI = 'khoan_chi'
    KHOAN_THU = 'khoan_thu'
    CHO_VAY_DI_VAY = 'cho_vay_di_vay'

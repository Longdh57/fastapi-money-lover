import enum


class CategoryType(str, enum.Enum):
    KHOAN_CHI = 'khoan_chi'
    KHOAN_THU = 'khoan_thu'
    CHO_VAY_DI_VAY = 'cho_vay_di_vay'


class WalletType(str, enum.Enum):
    TIEN_MAT = 'tien_mat'
    THE_NGAN_HANG = 'the_ngan_hang'
    THE_TIN_DUNG = 'the_tin_dung'

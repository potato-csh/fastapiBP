# 分页：计算偏移数
def calculate_offset(page_num: int, page_size: int) -> int:
    return page_size * (page_num - 1)
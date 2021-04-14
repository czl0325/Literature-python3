common_used_numerals_tmp = {'零': 0, '一': 1, '二': 2, '两': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10, '百': 100, '千': 1000, '万': 10000, '亿': 100000000}


def chinese2digits(number_chinese):
    if is_number(number_chinese):
        return int(number_chinese)
    number_chinese = number_chinese.strip()
    total = 0
    r = 1  # 表示单位：个十百千...
    try:
        for i in range(len(number_chinese) - 1, -1, -1):
            val = common_used_numerals_tmp.get(number_chinese[i])
            if not val:
                break
            if val >= 10 and i == 0:  # 应对 十三 十四 十*之类
                if val > r:
                    r = val
                    total = total + val
                else:
                    r = r * val
                    # total =total + r * x
            elif val >= 10:
                if val > r:
                    r = val
                else:
                    r = r * val
            else:
                total = total + r * val
        return total
    except Exception as e:
        print('截取错误,名称={},错误={}'.format(number_chinese, e))
        return -1


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    import unicodedata
    try:
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    if len(s) < 2:
        return False

    try:
        d = 0
        if s.startswith('－'):
            s = s[1:]
        for c in s:
            if c == '－':  # 全角减号
                return False

            if c == '．':  # 全角点号
                if d > 0:
                    return False
                else:
                    d = 1
                    continue
            unicodedata.numeric(c)
        return True
    except (TypeError, ValueError):
        pass

    return False
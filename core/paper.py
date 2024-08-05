import re
from datetime import datetime

season_to_month = {
    "spring": 3,
    "summer": 6,
    "fall": 9,
    "autumn": 9,
    "winter": 12
}

quarter_to_month = {
    "1st quarter": 1,
    "2nd quarter": 4,
    "3rd quarter": 7,
    "4th quarter": 10,
    "first quarter": 1,
    "second quarter": 4,
    "third quarter": 7,
    "fourth quarter": 10
}

def correct_month(month):
    month = month.rstrip('.').lower()

    # 常见的缩写转换字典
    month_mapping = {
        # 一月
        "jan": "jan",          # 英语
        "janeiro": "jan",      # 葡萄牙语
        "enero": "jan",        # 西班牙语
        "janvier": "janv",     # 法语
        "gennaio": "gen",      # 意大利语

        # 二月
        "feb": "feb",          # 英语
        "fev": "feb",          # 葡萄牙语
        "fevereiro": "feb",    # 葡萄牙语
        "febrero": "feb",      # 西班牙语
        "février": "fév",      # 法语
        "febbraio": "feb",     # 意大利语

        # 三月
        "mar": "mar",          # 英语
        "março": "mar",        # 葡萄牙语
        "marzo": "mar",        # 西班牙语, 意大利语
        "mars": "mars",        # 法语

        # 四月
        "apr": "apr",          # 英语
        "abr": "apr",          # 葡萄牙语, 西班牙语
        "abril": "apr",        # 葡萄牙语, 西班牙语
        "avril": "avr",        # 法语

        # 五月
        "may": "may",          # 英语
        "mai": "may",          # 葡萄牙语, 法语
        "mayo": "may",         # 西班牙语
        "maggio": "mag",       # 意大利语

        # 六月
        "jun": "jun",          # 英语
        "junho": "jun",        # 葡萄牙语
        "junio": "jun",        # 西班牙语
        "juin": "juin",        # 法语
        "giugno": "giu",       # 意大利语

        # 七月
        "jul": "jul",          # 英语
        "julho": "jul",        # 葡萄牙语
        "julio": "jul",        # 西班牙语
        "juillet": "juill",    # 法语
        "luglio": "lug",       # 意大利语

        # 八月
        "aug": "aug",          # 英语
        "ago": "aug",          # 葡萄牙语, 西班牙语, 意大利语
        "agosto": "aug",       # 葡萄牙语, 西班牙语, 意大利语
        "août": "août",        # 法语

        # 九月
        "sep": "sep",          # 英语
        "set": "sep",          # 葡萄牙语, 意大利语
        "setembro": "sep",     # 葡萄牙语
        "septiembre": "sep",   # 西班牙语
        "septembre": "sept",   # 法语
        "settembre": "set",    # 意大利语

        # 十月
        "oct": "oct",          # 英语
        "out": "oct",          # 葡萄牙语
        "outubro": "oct",      # 葡萄牙语
        "octubre": "oct",      # 西班牙语
        "octobre": "oct",      # 法语
        "ottobre": "ott",      # 意大利语

        # 十一月
        "nov": "nov",          # 英语
        "novembro": "nov",     # 葡萄牙语
        "noviembre": "nov",    # 西班牙语
        "novembre": "nov",     # 法语, 意大利语

        # 十二月
        "dec": "dec",          # 英语
        "dez": "dec",          # 葡萄牙语
        "dezembro": "dec",     # 葡萄牙语
        "diciembre": "dec",    # 西班牙语
        "décembre": "déc",     # 法语
        "dicembre": "dic"      # 意大利语
    }

    # 截取前三个字符
    short_month = month[:3]

    # 返回标准化的缩写
    return month_mapping.get(short_month, short_month)

# 测试函数
#test_months = ["Janeiro", "Feb", "Março", "Abr", "Mayo", "Jun", "Julio", "Ago", "Septiembre", "Out", "Nov", "Diciembre"]
#corrected_months = [correct_month(month) for month in test_months]
#print(corrected_months)  # ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

def parse_date(raw_text):
    #print(f"parse_date: {raw_text}")
    try:
        # Parse the date using multiple formats
        if re.match(r'\d{4}\s+(Spring|Summer|Fall|Autumn|Winter)\s+\d{2}', raw_text, re.IGNORECASE):
            # e.g. 2024 Winter 01
            year, season, day = raw_text.split(' ')
            month = season_to_month[season.lower()]
            return datetime.strptime(f"{year}-{month}-{day}", '%Y-%m-%d').date()
        elif re.match(r'\d{4}\s+(Spring|Summer|Fall|Autumn|Winter)\s*-\s*(Spring|Summer|Fall|Autumn|Winter)', raw_text, re.IGNORECASE):
            # e.g. 1992 Fall-Winter
            #      1992 Fall - Winter
            pattern = r'(\d{4})\s+(Spring|Summer|Fall|Autumn|Winter)\s*-\s*(Spring|Summer|Fall|Autumn|Winter)'
            match = re.match(pattern, raw_text)
            year, season, _ = match.groups()
            month = season_to_month[season.lower()]
            return datetime.strptime(f"{year}-{month}-01", '%Y-%m-%d').date()
        elif re.match(r'\d{4}\s+(Spring|Summer|Fall|Autumn|Winter)', raw_text, re.IGNORECASE):
            # e.g. 2020 Spring
            year, season = raw_text.split(' ')
            month = season_to_month[season.lower()]
            return datetime.strptime(f"{year}-{month}-01", '%Y-%m-%d').date()
        elif re.match(r'(Spring|Summer|Fall|Autumn|Winter)\s+\d{4}', raw_text, re.IGNORECASE):
            # e.g. Winter 2018
            season, year = raw_text.split(' ')
            month = season_to_month[season.lower()]
            return datetime.strptime(f"{year}-{month}-01", '%Y-%m-%d').date()
        elif re.match(r'\d{4}\s+(1st Quarter|2nd Quarter|3rd Quarter|4th Quarter)', raw_text, re.IGNORECASE):
            # e.g. 2020 1st Quarter
            match = re.match(r'(\d{4})\s+(1st Quarter|2nd Quarter|3rd Quarter|4th Quarter)', raw_text)
            year, quarter = match.groups()
            month = quarter_to_month[quarter.lower()]
            return datetime.strptime(f"{year}-{month}-01", '%Y-%m-%d').date()
        elif re.match(r'\d{4}\s+(First Quarter|Second Quarter|Third Quarter|Fourth Quarter)', raw_text, re.IGNORECASE):
            # e.g. 2024 Second Quarter
            match = re.match(r'(\d{4})\s+(First Quarter|Second Quarter|Third Quarter|Fourth Quarter)', raw_text)
            year, quarter = match.groups()
            month = quarter_to_month[quarter.lower()]
            return datetime.strptime(f"{year}-{month}-01", '%Y-%m-%d').date()
        elif re.match(r'\d{4}-[a-zA-Z]{3}-\d{2}', raw_text):
            # e.g. 2020-Jan-01
            return datetime.strptime(raw_text, '%Y-%b-%d').date()
        elif re.match(r'\d{4}\s+[a-zA-Z]{3}\s*[\-/]\s*[a-zA-Z]{3}\s+\d{2}', raw_text):
            # e.g. 2023 Jan-Feb 01
            #      2023 Jan/Feb 01
            #      2021 Set/Oct 01
            pattern = r'(\d{4})\s+([a-zA-Z]{3})\s*[\-/]\s*[a-zA-Z]{3}\s+(\d{2})'
            match = re.match(pattern, raw_text)
            year, month, day = match.groups()
            month = correct_month(month)
            return datetime.strptime(f"{year} {month} {day}", '%Y %b %d').date()
        elif re.match(r'\d{4}-[a-zA-Z]{3}', raw_text):
            # e.g. 2020-Jan
            return datetime.strptime(raw_text, '%Y-%b').date().replace(day=1)
        elif re.match(r'\d{4}-\d{2}-\d{2}', raw_text):
            # e.g. 2020-01-01
            return datetime.strptime(raw_text, '%Y-%m-%d').date()
        elif re.match(r'\d{4}\s+[a-zA-Z]{3}\s*[\-/]\s*[a-zA-Z]{3}', raw_text):
            # e.g. 2023 Jan-Feb
            #      2023 Jan/Feb
            pattern = r'(\d{4})\s+([a-zA-Z]{3})\s*[\-/]\s*[a-zA-Z]{3}'
            match = re.match(pattern, raw_text)
            year, month = match.groups()
            month = correct_month(month)
            return datetime.strptime(f"{year} {month} 01", '%Y %b %d').date()
        elif re.match(r'\d{4}-\d{4}', raw_text):
            # e.g. 2004-2005
            year = raw_text.split('-')[0]
            return datetime.strptime(year, '%Y').date().replace(month=1, day=1)
        elif re.match(r'\d{4}-\d{2}', raw_text):
            # e.g. 2020-01
            return datetime.strptime(raw_text, '%Y-%m').date().replace(day=1)
        elif re.match(r'\d{4}\s+[a-zA-Z]+\.?', raw_text):
            # e.g. 2020 January
            #      2020 Sept.
            #      2020 Sept
            #      2020 Sep
            pattern = r'(\d{4})\s+([a-zA-Z]+)\.?'
            match = re.match(pattern, raw_text)
            year, month = match.groups()
            month = correct_month(month)
            return datetime.strptime(f"{year} {month} 01", '%Y %b %d').date()
        elif re.match(r'\d{4}\s+\d+-\d+', raw_text):
            # e.g. 2016 11-12
            match = re.match(r'(\d{4})\s+(\d+)-\d+', raw_text)
            year, month = match.groups()
            return datetime.strptime(f"{year} {month} 01", '%Y %m %d').date()
        elif re.match(r'\d{4}', raw_text):
            # e.g. 2020
            return datetime.strptime(raw_text, '%Y').date().replace(month=1, day=1)
        else:
            print(f"Failed to parse date for unexpected format: '{raw_text}'")
            return None
    except ValueError:
        print(f"Failed to parse date: '{raw_text}'")
        return None

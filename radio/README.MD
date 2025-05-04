# 1. Linux команды
## 2. Hello Devops
```zsh
echo "\"Hello, DevOps\!"
echo "\"Hello, DevOps\!" > ~/hello.txt
cat ~/hello.txt
```

## 3. Logs
Для чтения логов можно использовать следующие команды:
1. `less`
    - `less /var/log/syslog` -- читаем по частям с пагинацией
    - `less +G /var/log/syslog` -- курсор в конец лога
    - `less +F /var/log/syslog` -- ждем новые записи
2. `tail`
    - `tail /var/log/syslog` -- чиатем низ логов (default -10, 10 строк)
    - `tail -f /var/log/syslog` -- ждем новые записи
3. `head`
    - `head /var/log/syslog` -- чиатем верх логов (default -10, 10 строк)
4. `cat`
    - `cat /var/log/syslog` -- чиатем все логи
5. `grep`
    - `grep error /var/log/syslog` -- читаем строки с **error**

Финальный pipe из задания: 
```
grep error /var/log/syslog | head -5
```

## 4. Config
`config.txt`
```txt
name: test_server
path: /home/user/data
file: data.txt
port: 8080
log path: /var/log/app
```

`main.py`
```python
import sys

def search_lines(file_path, search_string):
    with open(file_path, 'r') as file:
        for line in file.read().splitlines():
            if search_string in line:
                print(line)

if __name__ == "__main__":
    '''Usage: search_path.py <file_path> <search_string>'''
    file_path = sys.argv[1]
    search_string = sys.argv[2]
    search_lines(file_path, search_string)
```

## 5. Dockerfile
Оптимизируем в рамках заданного базового образа:
```Dockerfile
FROM ubuntu:latest 
COPY search_path.sh extract_path_value.py config.txt /tmp/
RUN apt-get update; \
    apt-get install -y --no-install-recommends wget python3 python3-pip; \
    rm -rf /var/lib/apt/lists/*; \
    chmod +x /tmp/search_path.sh /tmp/extract_path_value.py
```

Используем легковесный образ python:alpine (wget в busybox уже присутствует, поэтому его установка не требуется).
```Dockerfile
FROM python:3.13-alpine3.21
COPY search_path.sh extract_path_value.py config.txt /tmp/
RUN chmod +x /tmp/search_path.sh /tmp/extract_path_value.py
```
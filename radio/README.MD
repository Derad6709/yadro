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

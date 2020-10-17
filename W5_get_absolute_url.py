def get_absolute_url(url, *args, **kwargs):
    rezult = url
    for i in args:
        rezult += f"/{i}"
    rezult += '?'
    for k, v in kwargs.items():
        rezult += f"{k}={v}&"
    return rezult     


print(get_absolute_url('www.yandex.ru', 'posts', 'news', id='24', author='admin'))
print(get_absolute_url('www.google.com', 'images', id='24', category='auto', color='red', size='small'))
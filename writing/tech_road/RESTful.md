## Django的RESTful实践

采用django-rest-framework,示例参考[github主页](https://github.com/encode/django-rest-framework/tree/master)

可以采用curl指令与api进行交互:

```shell
# get all users
$ curl -H 'Accept: application/json; indent=4' -u admin:password http://127.0.0.1:8000/users/
[
    {
        "url": "http://127.0.0.1:8000/users/1/",
        "username": "admin",
        "email": "admin@example.com",
        "is_staff": true,
    }
]

# create user
$ curl -X POST -d username=new -d email=new@example.com -d is_staff=false -H 'Accept: application/json; indent=4' -u admin:password http://127.0.0.1:8000/users/
{
    "url": "http://127.0.0.1:8000/users/2/",
    "username": "new",
    "email": "new@example.com",
    "is_staff": false,
}

```



- [ ] 如果是获取某一类资源按条件筛选的部分实体，在restful中应该如何表达：比如筛选出属于某个实验的所有仿真
- [ ] 


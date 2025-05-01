# Проект бэкенда для работы приложения базы горных перевалов.
## (практика Skillfactory) ##

##### Базовый URL: _https:// your_host /pereval/_ ############


#### Доступные эндпоинты: #
_POST /submitData/_  - создаёт объект "перевал"\
_PATCH /submit/<int:pk>/_ - редактирует объект "перевал"\
_GET /submit/<int:pk>/_ - извлекает информацию об объекте "перевал"\
_GET /submitData/filter/?user__email=<email>_  - извлекает список объектов созданных одним пользователем 

___


### создаёт объект "перевал":
__URL__: _https:// your_host /pereval/submitData/_\
__Method__ : POST\
__Format__: json\
__Parameters__: No\
__Responses__:\
* HTTP_201_CREATED : \
status: success, data: data\
* HTTP_400_BAD_REQUEST :\
status: error, errors: serializer.errors




### редактирует объект "перевал":
__URL__: _https:// your_host /pereval/submit/<int:pk>/_\
__Method__ : PATCH\
__Format__: json\
__Parameters__: No\
__Responses__:\
* state: '1', message: 'обновлено успешно'\
* state: '0', messag': 'форма не валидна'\
* state: '0', message: 'статья принята модератором, обновление запрещено'




### извлекает информацию об объекте "перевал":
__URL__: _https:// your_host /pereval/submit/<int:pk>/_\
__Method__ : GET\
__Format__: json\
__Parameters__: No\
__Responses__:\
data




### извлекает список объектов созданных одним пользователем:
__URL__: _https:// your_host /pereval/submitData/filter/_\
__Method__ : GET\
__Format__: json\
__Parameters__: user__email=email\
__Responses__:\
data

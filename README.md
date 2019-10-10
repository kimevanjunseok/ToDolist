# Django TODOlist



> 데이터베이스 환경을 위해 `settings.py` 가 `settings/local.py` 에 셋팅하였습니다.
>
> - DB는 MySQL
>
> 로컬에서 실행이나 마이그레이션 등을 위해서는 다음과 같이 `--settings=myapp.settings.local` 옵션을 붙여줍니다.
>
> ```shell
> $ python manage.py runserver --settings=myapp.settings.local
> $ python manage.py migrate --settings=myapp.settings.local
> ```



## 기능

#### list 생성 전 index 페이지

+ home 버튼은 new, detail, update 등 메인 페이지로 돌아오게 해준다.
+ +가있는 사각형을 클릭하면 new페이지로 이동하면서 list를 작성할 수 있다.

![캡처1](https://user-images.githubusercontent.com/45934117/66562302-5bd7c580-eb96-11e9-9546-4ebcd2bfe703.PNG)

#### list 작성 페이지

- TITLE, PRIORITY, DUE DAY, CONTENT를 작성할 수 있다.

![new](https://user-images.githubusercontent.com/45934117/66562350-714cef80-eb96-11e9-82e4-973a4eed75b8.PNG)

#### 작성 후 index 페이지

- PRIORITY에 따라 색깔로 구분 할 수 있다.
- X를 누르면 해당 글은 삭제 된다.
- 화살표를 누르면 TODO, WORKING, FINISHED로 이동이 가능하다.
- 날짜가 지나 마감된 일정은 Deadline글씨가 써져있다.

![index](https://user-images.githubusercontent.com/45934117/66562368-7a3dc100-eb96-11e9-9228-1bc7d40894ad.PNG)

#### list 상세 페이지

- list를 볼 수 있다. 
- 수정은 EDIT버른을 누르면 가능하다.

![detail](https://user-images.githubusercontent.com/45934117/66562385-84f85600-eb96-11e9-906e-cba43007397e.PNG)

#### list 수정 페이지

- 일정을 수정할 수 있다.

![update](https://user-images.githubusercontent.com/45934117/66562396-8d509100-eb96-11e9-86fb-471498847739.PNG)

#### 잘못된 url 접근 페이지

- 설정한 url 이외에 다른 url로 접근시 해당 페이지가 나온다.
- HOME버튼은 클릭하면 index페이지로 이동한다.

![캡처2](https://user-images.githubusercontent.com/45934117/66562318-64c89700-eb96-11e9-81d8-6c406d8b0205.PNG)
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

- TODOlist 목록 조회
- TODOlist 작성
- TODOlist 수정 및 삭제
- TODOlist 작성 및 수정에서 우선순위를 설정
- TODOlist 완료처리
- 마감기한이 지난 TODOlist 표시
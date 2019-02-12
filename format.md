# 이 글을 기준으로 하며 합의 후 임의수정합니다.

---
# 양식

## 프로토콜

###	대상(프로토콜 경로+파일명+확장자)/[응답의 경우 요청의 링크](#대상경로파일명확장자응답의-경우-요청의-링크)

- 헤더1 : 내용1
- 헤더2 : 내용2
- 헤더3 : 내용3
	- 헤더 3-1 : 부연내용 3-1

부연설명

---

# Request

## GET

### GET html/Index.html
- query : 검색어(null=전체보기)

메인화면 및 검색결과 페이지로

### GET json/List.json
- query : 검색어(null=전체보기)

메인화면 게시글 목록 요청
### GET html/View.html
- id : 보는 글 번호(필수)

한개의 글을 보는 페이지

### GET html/Write.html
- id : 보는 글 번호(null=새 글)

글을 쓰는 페이지

## POST

### POST html/View.html
- id : 보는 글 번호(null=새 글)
- store : 상호명
- product : 제품명
- content : 할인내용
- price : 가격
- start : 시작일(없으면 현재시간)
- end : 만료일

글 생성/수정하고 나서 Write에서 View로 갈때

---

# Response

### [json/List.json JSON 형식 데이터](#GET-jsonListjson)

- 다음 형식으로 된 JSON 배열
	- id : 보는 글 번호
	- store : 상호명
	- product : 제품명
	- content : 할인내용
	- price : 가격
	- end : 만료일

### [html/View.html 파일과 헤더](#GET-htmlViewhtml)
- id : 보는 글 번호(필수)

응답에 해당하는 사이트를 주면서 글 번호 유지

### [html/Write.html 파일과 헤더](#GET-htmlWritehtml)
- id : 보는 글 번호(null=새 글)

응답에 해당하는 사이트를 주면서 글 번호 유지,없으면 추가시 새 글

### [html/View.html 파일과 헤더](#Post-htmlViewhtml)
- id : 보는 글 번호(필수)

글 수정 후 해당 글 수정된 결과 보여주기
# Problem-Solving

Ref) https://www.notion.so/Problem_Solving-669bb90d72d74dc7b28cefa82011503c#ee36536a1f89414eb2fc57ef6f133a9c

---

## Coding Convention

- Java - Google Java Style Guide
  - 명월일지 - https://nowonbun.tistory.com/378
- Python  - PEP8
  - 초보몽키의 개발공부로그 - https://wayhome25.github.io/python/2017/05/04/pep8/

---

## Git Convention

- 참가자별 Branch 생성하기

````
#파일명
문제번호_사용자명.확장자
ex) 1260_hayeona.java

#Commit message
소요시간_본인체감난이도(1 ~ 10)

#PR의 경우, 템플릿 참조 (TODO)
````

- Commit Location:

  1. ROOT DIRECTORY에서 Lowest Level까지 적합한 알고리즘 폴더 찾기 

  2. 해당 문제번호로 폴더가 생성되어 있는지 확인하기

     - 생성되어 있다면, 그 폴더에 push하기

     - 생성되어 있지 않다면, 해당 문제번호로 폴더를 만들고 코드 push하기
- 작업 순서:
  - 코드 작성하기 전, main/branch 싱크 맞추기 (작업 브랜치로 변경 이후,  git merge origin/main)
  - 코드 작성하기
  - 코드 커밋&푸시하기
  - Pull Request 및 merge 진행하기
- 작업 순서: git pull &rarr; git add 파일명 &rarr; git commit &rarr; git push &rarr; create PR &rarr; Merge
- ~~PR Review 활용 여부는 미정~~
- Jetbrains IDE 사용시, 불필요한 파일/폴더 업로드 방지 위해 gitignore 작성하기 (https://www.toptal.com/developers/gitignore) 

- 문제풀이 공유방법: 슬랙 참조
----








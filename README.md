# Problem-Solving

ref) [모집글](https://www.notion.so/Problem_Solving-669bb90d72d74dc7b28cefa82011503c#ee36536a1f89414eb2fc57ef6f133a9c)

---

## Coding Convention

- Java - Google Java Style Guide
  - 참조) 명월일지 - https://nowonbun.tistory.com/378
- Python  - PEP8
  - 참조) 초보몽키의 개발공부로그 - https://wayhome25.github.io/python/2017/05/04/pep8/

---

## Git Convention

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
  
  
  
- **작업 순서:**

- 참조) andamiro25 - https://andamiro25.tistory.com/193

  - **최초 진행할 경우 -** 

    - 자신의 git으로 해당 repo fork받기

    - 자신의 git에 생긴 repo clone받기 (local저장소 만들기)

    - 자신의 레포와 메인 레포와 연결하기 

      ```
      git remote add upstream https://github.com/hayeona92/Problem-Solving.git
      ```

    - 자신의 닉네임으로 브랜치 생성하기

      ```
      git checkout -b "자신의 닉네임"
      ```

      

  ```
  # 1. 코드 작성하기
  # 2. 코드 작성 한 이후 working branch(자신의 닉네임 브랜치)에서 다음과 같은 작업 진행
  
  # 파일 등록
  git add "파일명"								 
  # 커밋 남기기
  git commit -m "커밋 메세지"			
  
  
  # 3. 자신의 Repo와 Main Repo와 snyc 맞추기
  
  #닉네임(sub)브랜치에서 main 브랜치로 넘어가기
  git checkout main							
  
  #repo간 snyc 맞추기
  git pull upstream main				
  
  # working branch로 전환
  git checkout "브랜치명"					
  
  # working branch와 main branch snyc 맞추기
  git merge main 							  
  
  # 코드 푸시하기
  git push origin "working_branch" 		
  
  
  # 4. Pull Reqeust 생성하기 (target: hayeona92-main // Source: 자신의 브랜치)
  # 5. Pull Request 작성 후, merge 진행 및 확인하기
  ```

  

  

- ~~PR Review 활용 여부는 미정~~

- Jetbrains IDE 사용시, 불필요한 파일/폴더 업로드 방지 위해 gitignore 작성하기 (https://www.toptal.com/developers/gitignore) 

- 문제풀이 공유방법: 슬랙 참조
----








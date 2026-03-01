# Omok AI Team - Contribution Guide

## 1. 기본 원칙
- main 브랜치에 직접 push 금지
- 모든 작업은 feature 브랜치에서 진행
- 작업 후 Pull Request(PR) 생성

---

## 2. 개발 흐름

1. 최신 코드 가져오기
```
# 최신 코드 가져오기
git checkout main
git pull origin main
```

2. 기능 브랜치 생성
```
git checkout -b feature/이름-기능
```

예:
```
feature/minsu-ui
feature/ai-evaluation
```

3. 작업 후 커밋
```
git add .
git commit -m "feat: 기능 설명"
```

4. 원격 저장소로 push
```
git push origin 브랜치이름
```

5. GitHub에서 Pull Request 생성

---

## 3. 브랜치 구조

- main → 배포 버전
- feature/* → 개인 작업

---

## 4. 커밋 메시지 규칙

feat: 기능 추가  
fix: 버그 수정  
docs: 문서 수정  
refactor: 코드 개선  

예:
```
feat: add omok board rendering
```

---

## 5. 금지 사항

❌ main 직접 push  
❌ 다른 사람 브랜치 수정  
❌ node_modules 업로드
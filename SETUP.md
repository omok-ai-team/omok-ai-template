# 🚀 Omok AI Team Setup Guide

## 1️⃣ Git 설치
https://git-scm.com/downloads

설치 후 터미널 확인:

```
git --version
```

---

## 2️⃣ 저장소 가져오기

```
git clone https://github.com/baesunghu/omok-ai-team.git
cd omok-ai-team
```

---

## 3️⃣ develop 브랜치 이동

```
git checkout develop
git pull origin develop
```

---

## 4️⃣ 개인 작업 브랜치 생성

```
git checkout -b feature/이름-작업
```

예:
```
feature/minsu-ui
```

---

## 5️⃣ 작업 후 업로드

```
git add .
git commit -m "feat: 작업 설명"
git push origin 브랜치이름
```

---

## 6️⃣ Pull Request 생성

GitHub → Pull Requests → New Pull Request

오너 승인 후 merge 됩니다 ✅
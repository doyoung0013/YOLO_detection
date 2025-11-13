# 📸 Photo Blog Service (Django × Android × YOLOv5)

Django 기반 **서버**, Android(Java) 기반 **클라이언트**, 그리고 **YOLOv5(Edge)** 를 통합한  
**포토 블로그 & 실시간 침입 감지 시스템**입니다.  

로컬 PC에서 YOLOv5가 침입자를 감지하면 Django 서버로 자동 업로드되고,  
Android 앱에서 이미지 + 통계까지 즉시 확인할 수 있습니다.

---

## 🌐 Deployment & Dev Environment

- **Server:** Django 5.2.x (Local & PythonAnywhere)
- **Client:** Android Studio (Java, MPAndroidChart)
- **Edge AI:** YOLOv5s (PyTorch CPU)
- **Database:** SQLite3
- **API Test Tools:** Postman, curl

---

## 🧩 System Architecture
```
📷 YOLOv5 (Edge)
└─ 객체 감지 → 변경 감지(ChangeDetection) → Django REST API 업로드

🌐 Django (PhotoBlogServer)
├─ /api_root/Post/ : 게시물 CRUD
├─ /api_root/stats/ : [신규] 탐지 통계 API
├─ /posts/<id>/like/ : 좋아요 +1
├─ /posts/<id>/comment/ : 익명 댓글 작성
├─ /api-token-auth/ : 토큰 인증
└─ admin/ : 관리자 페이지

📱 Android (PhotoViewer)
├─ 게시물 리스트/상세/업로드
├─ 검색/정렬
└─ [신규] 탐지 통계 그래프(Bar/Pie)
```

---

## 📦 project folder structure
```
📦 Project Root
│
├── 📁 PhotoBlogServer (Django)
│ ├── blog/
│ │ ├── models.py (Post, Comment, ObjectCount)
│ │ ├── views.py (CRUD, like, comment, stats)
│ │ ├── serializers.py
│ │ └── urls.py
│ ├── mysite/
│ ├── manage.py
│ └── media/
│
├── 📁 PhotoViewer (Android)
│ ├── app/src/
│ ├── build.gradle.kts
│ └── ...
│
└── 📁 yolov5 (Edge AI)
├── detect.py 
├── changedetection.py
└── runs/detect/
```

---

## ✅ Main Features

| 구분 | 기능명 | 설명 |
|------|-------|------|
| 1 | **게시글 업로드** | YOLO 또는 안드로이드 앱에서 이미지 + 텍스트 업로드 |
| 2 | **게시글 목록/상세 보기** | REST API + Android RecyclerView |
| 3 | **좋아요 기능** | 로그인 없이 +1 증가 |
| 4 | **익명 댓글 기능** | 닉네임 + 내용만으로 작성 |
| 5 | **검색/정렬 기능** | 제목 검색, 최신순/좋아요순 정렬 |
| 6 | **YOLOv5 연동(Edge)** | 웹캠 → 감지 → 변화 감지 → 서버 자동 업로드 |
| 7 | **탐지 통계 API (/api_root/stats/)** | 최근 7일 일자별/객체별 탐지 수 집계 |
| 8 | **탐지 통계 그래프 시각화 (Android)** | BarChart/PieChart로 추세·비율 시각화 |

---

## ✨ Added Features

✔ 1) 탐지 객체 통계 기능 (/api_root/stats/)

최근 7일간의 일자별 탐지 횟수와 객체유형(person, car 등)별 탐지 횟수를 제공하는 API를 구현했습니다.
이 기능을 통해 단순 감지 기록을 넘어서 데이터 기반의 보안 모니터링이 가능해졌습니다.

✔ 2) 탐지 통계 그래프 시각화 (Android)

서버의 통계 API 데이터를 기반으로 BarChart 및 PieChart를 앱에서 시각화했습니다.
사용자는 감지 패턴과 이상 상황을 한눈에 파악할 수 있어 보안 대응 효율성이 크게 향상되었습니다.

---
## 👨‍💻 Developer Info

| 항목 | 내용 |
|------|------|
| 이름 | 김도영 |
| 학번 | 2022100631 |
| 과제 | 모바일/웹서비스 프로젝트 공통평가 01 |
| 기술 스택 | Django · Android(Java) · YOLOv5|

---

# git-demo

echo "# django-demo" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ichbinhan/django-demo.git
git push -u origin main

- 加入遠端倉庫
- 顯示目前連結的倉庫
  - git remote -v 
- 從本地推送到雲端
  - git push -u origin master
- 新增分支上傳，先切換到分支  git checkout <filename>
  - git push -u origin <filename>
- git clone
  - git clone https://github.com/ichbinhan/django-demo.git
  - 複製專案到本地端
  - 本地端新增修正後
    - git add .
    - git commit -m"message"
    - git push 
 



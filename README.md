# 幕布 to Anki
本项目探索了一种学习方法

1. 使用 [幕布](https://mubu.com) 记录笔记
2. 并将笔记导出成卡片
3. 使用 [Anki](https://ankiweb.net) 记忆这些卡片

来达到记住知识的目的

本项目对第2步做了自动化,使得能够更加快速的组合

## 使用方法
1. 下载 幕布
2. 下载 Anki 并安装 [AnkiConnect](https://ankiweb.net/shared/info/2055492159) 插件

AnnkiConnect 提供了操作 Anki 的 HTTP 接口

3. 在 Anki 中创建好相应的卡组
4. 使用本项目的 `python3 anki_ls.py` 找到卡组的全路径

anki 支持嵌套卡组

5. 在幕布新建文档, 第一个主题需要是
```
- metadata
    - deckName
        - ${deckName}
```
deckName 即为刚刚找到的卡组名

6. 在幕布中写笔记, 以`?` 或 `？`结尾此条笔记会被视为一个问题
7. 在此问题下缩进写问题的答案
8. 使用 幕布的导出功能, 导出 `.opml` 到此项目下
9. `python3 mubu2anki.py` 即可将幕布中的问题转化为 Anki 的卡片

由于 Anki 不允许卡片的 front 重复,所以执行创建卡片操作是 幂等 的

10. 在 Anki 开始记忆

## 有现成的学习资料吗？
本项目提供了一个幕布导出的 [opml](k8s.opml) 用于测试，文中是我读k8s官方网站的笔记

但不会再提供其他资料。理由是请看:
[Do not memorize before you understand](https://supermemo.guru/wiki/Do_not_memorize_before_you_understand)

只有理解过的资料才能记忆才是有效的，否则真就成了死记硬背了

本项目提到的所有工具都只是辅助，真正核心，还是你的大脑和你的决心。

加油！

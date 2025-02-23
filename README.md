# Yahoo Realtime Search Scraper 🚀

このリポジトリでは、Yahoo!リアルタイム検索を利用して間接的にX（旧Twitter）をスクレイピングするPythonスクリプトを提供します！🐍✨

## 📌 特徴
- Yahoo!リアルタイム検索の結果を取得 ✅
- キーワード検索やメディア検索対応 🎥
- ページネーションで過去の投稿も取得可能 🔄

## 🛠 インストール

```bash
pip install -r requirements.txt
```

## 🚀 使い方

```python
# インスタンスを作成
yahoo_realtime_search = YahooRealtimeSearch()

# ユーザーの最新の投稿から40件取得
timeline = yahoo_realtime_search.search('@elonmusk')

# さらに40件
print(next(timeline))
```

## 🎯 検索オプション

`search(keyword: str, type: Optional[Literal["media"]] = None)`

| 引数 | 説明 |
|------|------|
| `keyword` | 検索キーワード（@username で特定ユーザーも検索可能） |
| `type` | `'media'` を指定すると画像付きツイートのみ取得 |

## ⚠️ 注意事項
- 本スクリプトは非公式な手法でデータを取得しているため、仕様変更などで動作しなくなる可能性があります。
- Yahoo!やX（旧Twitter）の利用規約に違反しないよう注意してください。

## 💡 コントリビュート
バグ報告や機能追加の提案は大歓迎！Pull Request も待ってます！🚀

Enjoy coding! ✨🐍


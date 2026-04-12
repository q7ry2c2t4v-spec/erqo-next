# Webビュー

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/web-views

# Webビュー

Webビューは、埋め込まれたHTMLやWebサイトなどのリッチなWebコンテンツをアプリ内に直接読み込んで表示します。

![図案化されたコンパスアイコン。画像は全体が、6色のオリジナルAppleロゴを連想させる赤色になっています。](https://docs-assets.developer.apple.com/published/d0967603b78a0a363afd853adbf8de97/components-web-view-intro%402x.png)

例えば「メール」では、メッセージ内のHTMLコンテンツを表示するためにWebビューが使われています。

## [ベストプラクティス](/jp/design/human-interface-guidelines/web-views#Best-practices)

**進む/戻るナビゲーションに適宜対応する。** Webビューは進む/戻るナビゲーションに対応していますが、デフォルトでは使用不可になっています。ユーザがWebビューで複数のページを閲覧する可能性がある場合は、進む/戻るナビゲーションを有効にし、それぞれに対応するコントロールでこれらの機能を呼び出してください。

**Webビューを使ってWebブラウザを構築することはしない。** アプリの操作環境を離れずに簡潔にWebサイトにアクセスできるようにする目的でWebビューを使うのはかまいませんが、Webブラウジングの主な手段はあくまでSafariです。Safariの機能をアプリ内で複製する必要はありません。むしろ、そうしないでください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/web-views#Platform-considerations)

 _iOS、iPadOS、macOS、visionOSには追加の考慮事項はありません。tvOSとwatchOSには対応していません。_

## [リソース](/jp/design/human-interface-guidelines/web-views#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/web-views#Related)

[Webkit.org](https://webkit.org/)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/web-views#Developer-documentation)

[`WKWebView`](/documentation/WebKit/WKWebView) — WebKit

#### [ビデオ](/jp/design/human-interface-guidelines/web-views#Videos)

[](https://developer.apple.com/videos/play/wwdc2021/10032)

# ShazamKit

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/shazamkit

# ShazamKit

ShazamKitでは、オーディオサンプルをShazamKitカタログやカスタムオーディオカタログと照合して音声認識を行うことができます。

![ShazamKitアイコンのスケッチ。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせる青色になっています。](https://docs-assets.developer.apple.com/published/7a295a311de059de0924ba1eddf3055a/technologies-ShazamKit-intro%402x.png)

ShazamKitを使用すると、以下のような機能を提供できます:

  * 再生中のミュージックのジャンルに合ったグラフィックスを表示して、より高品質なアプリ体験を提供する

  * オーディオと同期したクローズドキャプションや手話言語を表示して、聴覚障がいのある人がメディアコンテンツを楽しめるようにする

  * オンライン学習やオンライン販売のバーチャルコンテンツにアプリ内体験を同期させる

認識対象のオーディオサンプルを取得するためにデバイスのマイクを使う必要がある場合は、マイクへのアクセスをリクエストする必要があります。許可をリクエストするその他すべての場合と同様に、アクセスをリクエストする理由をユーザに理解してもらうことが重要です。ガイダンスは[プライバシー](/jp/design/human-interface-guidelines/privacy)を参照してください。

![iPhoneに表示されたMath Schoolアプリの許可アラートのスクリーンショット。「Math Schoolがマイクにアクセスしようとしています。文章や数学の演習問題を、教師が再生中のビデオと同期します」というメッセージが表示されています。その下に「今はしない」と「許可」という2つのボタンがあります。](https://docs-assets.developer.apple.com/published/3391b7663e29baac353d6e73275491d7/shazamkit-mic-permission%402x.png)

## [ベストプラクティス](/jp/design/human-interface-guidelines/shazamkit#Best-practices)

ShazamKitを利用する機能がマイクを使用する許可が得られたら、その後は以下のガイドラインに従ってください。

**録音はできる限り短時間で停止する。** 音声認識のための録音を許可したとしても、ユーザはマイクがオンの状態になったままになるとは想定していません。プライバシーを保護するために、必要なサンプルを得るのに十分な時間で録音を停止してください。

**アプリで認識された曲をiCloudライブラリに保存するかどうかの選択はユーザに委ねる。** 認識された曲をiCloudに保存できるようにしているアプリの場合は、最初にユーザの許可を取りましょう。アプリはミュージック認識コントロールとShazamアプリのどちらにも、認識した曲のソースとして表示されますが、ライブラリにコンテンツを保存できるアプリを制御できた方がユーザには喜ばれます。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/shazamkit#Platform-considerations)

 _iOS、iPadOS、macOS、tvOS、visionOS、watchOSに追加の考慮事項はありません。_

## [リソース](/jp/design/human-interface-guidelines/shazamkit#Resources)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/shazamkit#Developer-documentation)

[ShazamKit](/documentation/ShazamKit)

#### [ビデオ](/jp/design/human-interface-guidelines/shazamkit#Videos)

[](https://developer.apple.com/videos/play/wwdc2021/10044)

# 常時表示

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/always-on

# 常時表示

常時表示ディスプレイを搭載したデバイスでは、ユーザがデバイスの操作を中断してもシステムがアプリのインターフェイスの表示を継続できます。

![走っている人が写っているApple Watchのスケッチ。常時表示ディスプレイを示しています。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせる青色になっています。](https://docs-assets.developer.apple.com/published/19c479d3d428ef87dd2ade2824f87a7e/technologies-always-on-intro%402x.png)

常時表示状態になっているデバイスでは、有用な情報をいつでもぱっと確認できます。ディスプレイが暗くなり、画面上の動きも最小限になるので、省電力かつプライバシーに配慮した形で表示が継続されます。表示される項目はデバイスによって異なります。

  * iPhone 14 ProおよびiPhone 14 Pro Maxの場合: ユーザが画面を上にしてデバイスを置き、操作をやめると、[ウィジェット](/jp/design/human-interface-guidelines/widgets)や[ライブアクティビティ](/jp/design/human-interface-guidelines/live-activities)などのロック画面項目が表示されます。

  * Apple Watch: 装着している手首を下ろすと、文字盤が暗くなり、アプリが最前面にあるかバックグラウンドセッションで動作している間はアプリのインターフェイスの表示が継続されます。

どちらのデバイスでも、常時表示のときに通知が表示されます。また、画面のタップで常時表示を終了して操作を再開できます。

## [ベストプラクティス](/jp/design/human-interface-guidelines/always-on#Best-practices)

**機密情報を非表示にする。** 銀行口座の残高やヘルスケアデータなど、何気なく画面を見た人に見られたくない個人情報を除外することが非常に重要です。また、通知に表示される可能性がある個人情報も非表示にする必要があります。[通知](/jp/design/human-interface-guidelines/notifications)のガイダンスを参照してください。

**適宜その他の種類の個人情報を一目で確認できるようにする。** 例えばApple Watchでは、ワークアウト中にペースや心拍数の最新情報を確認できると多くのユーザに喜ばれます。iPhoneでは、一目で確認できるフライト到着時刻の最新情報や、配車サービスの車が着いたときの通知が表示されると喜ばれます。どの情報も表示したくないユーザは常時表示をオフにできます。

**重要なコンテンツの読みやすさをキープしたまま補足的なコンテンツを暗くする。** セカンダリーテキスト、画像、塗りつぶしをより暗くして、ユーザにとって重要な情報が目立つようにします。例えばTo Doリストアプリでは、行の背景を消して各項目の補足情報を暗くすることでタイトルを強調できます。また、画像が鮮やかな場合やカラーの付いた領域が大きい場合は、画像をなくしたりカラーを暗くしたりすることを検討してください。

**レイアウトを変えない。** 常時表示の開始時や終了時、および常時表示の最中は、ユーザの気が散るようなインターフェイスの変更を避けてください。例えばインタラクティブなコンポーネントの場合は、常時表示の開始時にただ単に消すよりも、インタラクティブでない見た目に変えることをおすすめします。常時表示の最中は、インターフェイスのアップデートの頻度を下げ、控えめにすることを心がけます。例えばスポーツアプリでは、常時表示のときは逐一アップデートすることをいったんやめ、スコアに変化があったときのみアップデートするなどします。常時表示の最中にインターフェイスが不必要に変化すると、iPhoneでは特に気になってしまうことがあります。iPhoneはたいてい画面を上にして置かれるので、直接見ていなくても画面上の動きが目に入るからです。

**いきなり動きを止めるのではなく、スムーズに静止させる。** 柔らかく動きを止めれば、エラーでも起きたのだろうかという誤解を生じさせずに、常時表示状態になったことが伝わりやすくなります。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/always-on#Platform-considerations)

 _iOS、watchOSに追加の考慮事項はありません。iPadOS、macOS、tvOS、visionOSには対応していません。_

## [リソース](/jp/design/human-interface-guidelines/always-on#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/always-on#Related)

[watchOS向けのデザイン](/jp/design/human-interface-guidelines/designing-for-watchos)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/always-on#Developer-documentation)

[常時表示状態に対応するアプリの設計](/documentation/watchOS-Apps/designing-your-app-for-the-always-on-state) — watchOSアプリ

#### [ビデオ](/jp/design/human-interface-guidelines/always-on#Videos)

[](https://developer.apple.com/videos/play/wwdc2021/10002)

[](https://developer.apple.com/videos/play/wwdc2021/10009)

[](https://developer.apple.com/videos/play/wwdc2021/10018)

## [変更履歴](/jp/design/human-interface-guidelines/always-on#Change-log)

日付| 変更内容  
---|---  
2023年9月12日| イントロ画像アートワークをアップデート。  
2022年9月23日| iPhone 14 ProおよびiPhone 14 Pro Maxの常時表示ディスプレイに関するガイダンスを追加しました。

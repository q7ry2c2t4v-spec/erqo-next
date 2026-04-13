# watchOS向けのデザイン

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/designing-for-watchos

# watchOS向けのデザイン

Apple Watchは、移動中でもそうでないときも、ひと目見るだけで重要な情報にアクセスしたり簡単なタスクをタイムリーに実行したりできるものと一般的に認識されています。

![図案化されたApple Watchのフレーム。グリッドの一番上に表示されています。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせる緑色になっています。](https://docs-assets.developer.apple.com/published/d29fb746b11ccb7eac96b3a8018efb35/platforms-watchOS-intro%402x.png)

Apple Watch向けのアプリをデザインするときは、まず以下に示すデバイスの基本的な特徴やwatchOSならではの操作パターンを理解することから始めてください。この特徴やパターンを参考にしてデザインを決定することで、Apple Watchユーザに喜ばれるアプリを提供できます。

**ディスプレイ:** Apple Watchには手首にぴったりの小型サイズながら読みやすい高解像度のディスプレイが搭載されています。

**人間工学:** Apple Watchは身につけるものなので、通常はディスプレイから30センチ以上離れることはありません。見るために手首を持ち上げたり、もう片方の手を使用してデバイスを操作したりします。また、常時表示ディスプレイにより、手首を下げているときも文字盤の情報を確認できます。

**入力:** ユーザは、[Digital Crown](/jp/design/human-interface-guidelines/digital-crown)を回して縦にナビゲーションしたり、データを調べたりできます。これによって、文字盤、ホーム画面、アプリ内で一貫性の高い操作感が生まれます。ユーザは、タップ、スワイプ、ドラッグなど標準の[ジェスチャ](/jp/design/human-interface-guidelines/gestures)で、動いているときでも入力操作を行えます。[アクションボタン](/jp/design/human-interface-guidelines/action-button)を押して、画面を見ずに重要なアクションを開始できます。[ショートカット](/jp/design/human-interface-guidelines/siri#Shortcuts-and-suggestions)は、繰り返し行うタスクを素早く簡単に実行するのに便利です。GPS、血中酸素や心機能のセンサー、高度計、加速度計、ジャイロスコープなどのデバイス内蔵機能を利用することもできます。

**アプリの操作:** 一般にユーザは1日に何度も常時表示ディスプレイを見て、アプリを短時間で操作します。操作が終わるまで1分もかかりません。アプリ自体よりも、コンプリケーションや通知、Siriとの会話など、watchOSのアプリに関連する体験の方がよく使われます。

**システム機能:** watchOSには、馴染みのある一貫した方法でシステムやアプリを操作できる複数の機能があります。

  * [コンプリケーション](/jp/design/human-interface-guidelines/complications)

  * [通知](/jp/design/human-interface-guidelines/notifications)

  * [常時表示](/jp/design/human-interface-guidelines/always-on)

  * [文字盤](/jp/design/human-interface-guidelines/watch-faces)

## [ベストプラクティス](/jp/design/human-interface-guidelines/designing-for-watchos#Best-practices)

Apple Watchは、プラットフォームとデバイスの機能を統合して、ユーザにきわめて価値のある特別な体験を提供することに特化した製品です。watchOSらしい操作環境にするために、以下の方法に優先順位を付けてそれぞれの特徴や機能を取り入れてください。

  * 重要な情報を簡潔に伝え、ユーザがひと目見ただけで必要な操作を1画面で完了できるようにします。1回か2回の簡単なジェスチャで目的のアクションを実行できるのが適切です。

  * アプリのナビゲーション階層の深さを最小化し、[Digital Crown](/jp/design/human-interface-guidelines/digital-crown)を使って、スクロールや画面の切り替えを行う縦方向のナビゲーション機能を提供します。

  * ユーザが求めるものを先回りして予測したり、デバイス上のデータを使用してそのときどきや近い将来に関連する有用なコンテンツを提示したりして、体験をパーソナライズします。

  * [コンプリケーション](/jp/design/human-interface-guidelines/complications)を使用して、必要なデータやグラフィックスを文字盤に直接表示します。動的なデータを表示することもできます。文字盤はユーザが手首を持ち上げるたびに目に入るのに加え、タップして直接アプリを開くことができます。

  * [通知](/jp/design/human-interface-guidelines/notifications)を使用して有益な情報をタイムリーに届け、アプリを開かなくても重要なアクションを行えるようにします。

  * [カラー](/jp/design/human-interface-guidelines/color)などのバックグラウンドコンテンツを活用してユーザに役立つ情報を伝え、[マテリアル](/jp/design/human-interface-guidelines/materials)を使って、階層構造や今どの画面にいるかを分かりやすく表現します。

  * Siriに対応させて、Siriの文字盤のショートカットにアクセスしやすくします。

  * アプリが独立して機能するようにデザインし、詳細情報や追加機能を提供することで、通知やコンプリケーションを補完できるようにします。

## [リソース](/jp/design/human-interface-guidelines/designing-for-watchos#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/designing-for-watchos#Related)

[Appleデザインリソース](https://developer.apple.com/design/resources/#watchos-apps)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/designing-for-watchos#Developer-documentation)

[watchOS Pathway](https://developer.apple.com/watchos/get-started/)

#### [ビデオ](/jp/design/human-interface-guidelines/designing-for-watchos#Videos)

[](https://developer.apple.com/videos/play/wwdc2025/334)

## [変更履歴](/jp/design/human-interface-guidelines/designing-for-watchos#Change-log)

日付| 変更内容  
---|---  
2023年6月05日| ひと目で分かる、洗練されたアプリ体験を提供するためのガイダンスを改善。ナビゲーションにおけるDigital Crownの重要性を強調。

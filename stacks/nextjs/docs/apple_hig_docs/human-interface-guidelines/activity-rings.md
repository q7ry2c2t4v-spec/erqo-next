# アクティビティリング

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/activity-rings

# アクティビティリング

アクティビティリングは、毎日のムーブ、エクササイズ、スタンド目標の達成状況を示すコンポーネントです。

![ムーブ、エクササイズ、スタンドの達成状況を示す図案化されたアクティビティリング。画像は全体が、6色のオリジナルAppleロゴを連想させる赤色になっています。](https://docs-assets.developer.apple.com/published/564ce839558436a8509944b8ec9cab68/components-activity-ring-intro%402x.png)

watchOSのアクティビティリング要素には、常に3つのリングが含まれます。それぞれの色や意味はアクティビティアプリと対応しています。iOSのアクティビティリング要素には、おおよそのアクティビティを示すムーブリングのみ、またはApple Watchがペアリングされている場合は3つのリングすべてが表示されます。

## [ベストプラクティス](/jp/design/human-interface-guidelines/activity-rings#Best-practices)

**アクティビティリングは、アプリの目的に直接関わる場合に表示する。** 健康やフィットネス関連のアプリ、とりわけHealthKitに情報を提供するアプリの場合、ユーザはインターフェイスにアクティビティリングが示されることを期待します。例えば、アクティビティリングを完了することを主眼に置いたワークアウトや健康関連のセッションを構成する場合なら、ワークアウト指標画面にこの要素を表示し、ユーザがセッション中に進捗を確認できるようにすることをおすすめします。また、ワークアウトの終了時に概要画面を表示する場合は、アクティビティリングを表示して日々の目標の達成状況を確認できるようにしてもよいでしょう。

![進行中のワークアウト画面。現在のタイマーの値に続いて、現在のムーブ、エクササイズ、スタンドの値がリスト表示されています。画面には、アクティビティリングの画像も表示され、それぞれのリンクの状態が現在の値を表しています。](https://docs-assets.developer.apple.com/published/068b4894ca9e6fc91d641a8778be9198/activity-rings-summary%402x.png)

**アクティビティリングは、ムーブ、エクササイズ、スタンドの情報を表示するためだけに使用する。** アクティビティリングは、上記の項目の達成状況を表示することに特化したコンポーネントです。ほかの目的のために複製したり、変更を加えたりしないでください。アクティビティリングでほかのタイプのデータを表示することは決してしないでください。また、ムーブ、エクササイズ、スタンドの達成状況を、リングに似たほかの要素で表すことも決してしないでください。

**アクティビティリングは、1人のユーザの進捗を表示するために使用する。** アクティビティリングを使用して複数のユーザのデータを表示してはなりません。ラベルや写真、アバターを使用して、誰の達成状況を示しているかを必ず明確にします。

**アクティビティリングの見た目は、表示する場所にかかわらず常に同じにする。** 以下のガイドラインに従い、一貫した体験を提供します:

  * リングの色は変更しないでください。例えば、フィルタを使用したり、透明度を変更したりしないようにします。

  * アクティビティリングは、必ず黒い背景上に表示します。

  * 可能な限り、リングと背景を円で囲むようにします。これを行うには、円形のマスクを適用するのではなく、リングを囲むビューの角丸半径を調整します。

  * 一番外側のリングの周辺に、視認できる黒い背景を残すようにします。必要に応じて、リングの外側の端に細い黒線を追加します。また、グラデーションやシャドウなどの視覚エフェクトは含めないようにします。

  * リングがバラバラになったり、あるべき位置からずれたりしないよう、リングの拡大/縮小は常に適切な比率で行ってください。

  * 必要に応じて、リングと調和するように周囲のインターフェイスをデザインしてください。リングが周辺のインターフェイスに溶け込まないようにします。

**アクティビティリングに直接関係するラベルや値を表示する場合は、色を合わせるようにする。** _ムーブ_ 、 _エクササイズ_ 、 _スタンド_ のリング固有のラベルを表示する場合、または各リングのその人の現在値や目標値を表示する場合は、以下のRGB値の色を使用します。

ムーブ| エクササイズ| スタンド  
---|---|---  
![R-250,G-17,B-79](https://docs-assets.developer.apple.com/published/f347174d08cc485cd465646660bce083/activity-rings-color-swatch-red%402x.png)| ![R-166,G-255,B-0](https://docs-assets.developer.apple.com/published/462bfbf466935f89dcc63b1c79aa0a7c/activity-rings-color-swatch-green%402x.png)| ![R-0,G-255,B-246](https://docs-assets.developer.apple.com/published/a766fb1cbeeacd0434ca05b581168f1a/activity-rings-color-swatch-blue%402x.png)  
  
**アクティビティリングの余白を保つ。** アクティビティリング要素の外側には、リング間の距離以上の余白を設ける必要があります。ほかの要素やリング自身によって、表示が欠けたり、重なったり、余白部分にはみ出たりすることがないようにしてください。

**アクティビティリングとリングに似たほかの要素を区別する。** 異なるスタイルのリングを混在させると、インターフェイスが見づらくなります。ほかのリングを含める必要がある場合は、間隔を空けたり、線やラベルを使用したりしてアクティビティリングと区別してください。カラーや大きさを変えることでも、視覚的に区別しやすくなります。

**アクティビティアプリが送る通知と重複する通知を送らない。** ムーブ、エクササイズ、スタンドの達成状況の更新情報が先にシステムから配信されるので、重複する情報がアプリから届くとユーザは戸惑います。また、アクティビティリング要素をアプリの通知に表示しないでください。アプリの通知でアクティビティの達成状況を参照してもかまいませんが、その場合はアプリ独自の方法で行い、システムが提供する情報をそのまま流用しないでください。

**アクティビティリングを装飾目的で使わない。** アクティビティリングはユーザに情報を提供するためのもので、単にアプリのデザイン向上を目的としたものではありません。アクティビティリングをラベルや背景のグラフィックスに絶対に表示しないでください。

**アクティビティリングをブランディング目的で使わない。** アクティビティリングは、アプリでアクティビティの達成状況を表示するためだけに使用します。アクティビティリングをアプリのアイコンやマーケティング素材に使用しないでください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/activity-rings#Platform-considerations)

 _iPadOS、watchOSに追加の考慮事項はありません。macOS、tvOS、visionOSには対応していません。_

### [iOS](/jp/design/human-interface-guidelines/activity-rings#iOS)

iOSでは、[`HKActivityRingView`](/documentation/HealthKitUI/HKActivityRingView)でアクティビティリングを利用できます。アクティビティリング要素の見た目は、Apple Watchがペアリングされているかどうかによって自動的に以下のように変化します。

  * Apple Watchがペアリングされている場合、iOSには3つのアクティビティリングすべてが表示されます。

  * Apple Watchがペアリングされていない場合、iOSにはムーブリングのみが表示されます。このリングは、ほかのアプリの歩数やワークアウトの情報に基づいたユーザのおおよそのアクティビティを表します。

![Apple WatchとペアリングされたiOSフィットネスアプリの「アクティビティの概要」のスクリーンショット。3つすべてのアクティビティリングが表示されています。](https://docs-assets.developer.apple.com/published/6f51c8c70e84ef7e42fdc6485f822806/activity-rings-watch-paired%402x.png)

Apple Watchとペアリングされています

![Apple WatchとペアリングされていないiOSフィットネスアプリの「アクティビティの概要」のスクリーンショット。ムーブリングのみが表示されています。](https://docs-assets.developer.apple.com/published/28b49cb0c1378ea2c29f3960590e8ab5/activity-rings-no-watch-paired%402x.png)

Apple Watchとペアリングされていません

iOSでは、Apple Watchがペアリングされているかどうかにかかわらず、アクティビティリングが表示されるので、アクティビティの履歴には両方のスタイルが含まれる場合があります。例えば、「フィットネス」のアクティビティリングには、Apple Watchをペアリングしてエクササイズを行った場合は3つのリングが、Apple Watchなしでエクササイズを行った場合はムーブリングのみが表示されます。

## [リソース](/jp/design/human-interface-guidelines/activity-rings#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/activity-rings#Related)

[ワークアウト](/jp/design/human-interface-guidelines/workouts)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/activity-rings#Developer-documentation)

[`HKActivityRingView`](/documentation/HealthKitUI/HKActivityRingView) — HealthKit

#### [ビデオ](/jp/design/human-interface-guidelines/activity-rings#Videos)

[](https://developer.apple.com/videos/play/wwdc2025/322)

[](https://developer.apple.com/videos/play/wwdc2021/10009)

[](https://developer.apple.com/videos/play/wwdc2023/10016)

## [変更履歴](/jp/design/human-interface-guidelines/activity-rings#Change-log)

日付| 変更内容  
---|---  
2024年3月29日| アクティビティリングの表示に関するガイドを改善。関連コンテンツを表示する際の特定の色を列挙。  
2023年12月05日| iOSのアクティビティリングを表すアートワークを追加。

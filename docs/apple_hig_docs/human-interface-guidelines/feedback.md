# フィードバック

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/feedback

# フィードバック

フィードバックは、ユーザが現在の状況を把握し、次に何ができるかを知り、操作の結果を理解し、間違いを避けるのに役立ちます。

![ポインタをいくつかの短い線が円形に囲んでいるスケッチ。マウスクリックへの応答を示しています。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせるオレンジ色になっています。](https://docs-assets.developer.apple.com/published/d7e2c91a509e05b5e8ee422c6fea86b3/patterns-feedback-intro%402x.png)

ユーザがアプリやゲームを適切に操作できる明確で一貫したフィードバックを呈示すれば、アプリを直感的に操作でき、より高度に使いこなせるようになります。フィードバックで伝達できる主な情報は以下の通りです:

  * システムやアプリ内のさまざまな個所の現在の状態

  * 重要なタスクやアクションの成功または失敗

  * 望ましくない結果を招く可能性のある操作に対する警告

  * 間違いや問題のある状況を修正する機会

一般に、効果的なフィードバックにするには、情報の重大度にふさわしい方法で伝達する必要があります。例えば、状況情報は多くの場合、ユーザが必要なときに確認できるような控えめな方法で提示するのが効果的です。それとは対照的にデータ損失の可能性を警告するメッセージは、問題を回避する機会を逃さないよう、ユーザの作業を中断してでも表示する必要があります。

## [ベストプラクティス](/jp/design/human-interface-guidelines/feedback#Best-practices)

**すべてのフィードバックを確実にアクセス可能にする。** 複数の方法でフィードバックを提示すると、より幅広いユーザを対象として、各ユーザにとって効果的な方法でフィードバックを届けることができるようになります。例えば、色、テキスト、サウンド、触覚を使ってフィードバックを提示すれば、ユーザがデバイスを無音にしていたり、画面を見ていなかったり、VoiceOverを使っていたりしてもフィードバックを受け取れます。（触覚フィードバックの提示についてのガイダンスは、[触覚フィードバックの提供](/jp/design/human-interface-guidelines/playing-haptics)を参照してください。）

**状況のフィードバックをインターフェイスに組み込む。** 状況のフィードバックを対象の項目の近くで提示すれば、ユーザは追加の操作をしたり現在の作業を中断したりせずに、重要な情報を得ることができます。例えば、iOSおよびiPadOSの「メール」では、メールボックス画面のツールバーには最新情報と未読メッセージの数が表示されます。情報の表示方法は控えめですが、ユーザは関心があれば簡単にチェックできます。

**重大な情報はアラートを使って（できれば行動につながる情報も）伝達する。** アラートはどうしても現在の作業を中断させることになるので、情報の重大度が中断の程度に見合ったものでなければなりません。アラートをあまりに頻繁に使用したり、重要でない情報の伝達に使ったりすると、アラートの効果が薄れかねません。ガイダンスは、[アラート](/jp/design/human-interface-guidelines/alerts)を参照してください。

**予期できず取り返しのつかないデータ損失の原因になる可能性があるタスクを開始しようとするユーザに警告する。** 逆に、ユーザの操作の結果としてデータ損失が予期される場合、警告は不要です。例えば、Finderはユーザがファイルを捨てるたびに警告しません。ファイルを削除するどうなるか予期できるからです。

**重要なアクションやタスクの完了を必要に応じて確認する。** 例えば、Apple Payの取引が正常に完了したことを確認するフィードバックはユーザにとって有用な情報です。一般に、このタイプの確認は十分に重要性のあるアクティビティに限定するのが最善です。通常、ユーザはアクションやタスクが正常に完了すると考えており、そうならなかった場合だけ確認が必要だからです。

**コマンドを実行できない場合はその旨と理由をユーザに伝える。** 例えば「マップ」は、ユーザが目的地を指定せずに経路を要求すると、同一場所を出発および到着地点とした経路の表示はできないことを通知します。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/feedback#Platform-considerations)

 _iOS、iPadOS、macOS、tvOS、visionOSに追加の考慮事項はありません。_

### [watchOS](/jp/design/human-interface-guidelines/feedback#watchOS)

**watchOSアプリでは読み込みインジケータなどの不確定的なプログレスインジケーターを表示しない。** 動きのあるインジケータを表示すると、ユーザはディスプレイを見続けなければならないと感じる可能性があります。これでは良好な操作感が損なわれます。ユーザに安心してもらうため、プロセスが完了したら通知を受け取れることを明確に伝えてください。

## [リソース](/jp/design/human-interface-guidelines/feedback#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/feedback#Related)

[オーディオの再生](/jp/design/human-interface-guidelines/playing-audio)

[触覚フィードバックの提供](/jp/design/human-interface-guidelines/playing-haptics)

[モーション](/jp/design/human-interface-guidelines/motion)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/feedback#Developer-documentation)

[アニメーションおよび触覚フィードバック](/documentation/UIKit/animation-and-haptics) — UIKit

#### [ビデオ](/jp/design/human-interface-guidelines/feedback#Videos)

[](https://developer.apple.com/videos/play/wwdc2018/803)

[](https://developer.apple.com/videos/play/wwdc2017/802)

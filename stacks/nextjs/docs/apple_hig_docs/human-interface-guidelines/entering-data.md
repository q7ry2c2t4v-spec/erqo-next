# データの入力

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/entering-data

# データの入力

ユーザからの情報が必要な場合、ユーザが正確かつ簡単に情報を入力できる方法を考えてください。

![フィールドにペンシルで手書きしているスケッチ。データの入力を示しています。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせるオレンジ色になっています。](https://docs-assets.developer.apple.com/published/cf9c15cc07141563743a0518f605b5c6/patterns-entering-data-intro%402x.png)

どんなに操作方法を工夫しても、情報の入力は基本的に面倒な作業です。ユーザ体験を改善するには、以下のような方法があります。

  * できるだけ多くの情報を事前に収集し、ユーザが入力しなければならないデータの量を最小限に抑える

  * 利用可能なすべての入力方法に対応し、ユーザが自分に都合のよい方法を選べるようにする

## [ベストプラクティス](/jp/design/human-interface-guidelines/entering-data#Best-practices)

**可能な限りシステムから情報を入手する。** 設定などから自動的に収集できる情報の入力をユーザに求めないでください。また、ユーザが許可していれば、場所やカレンダー情報なども収集できます。

**必要なデータを明確にする。** 例えば、プロンプトのテキストフィールドに「username@company.com」のような文字列を入れたり、「メールアドレス」のように必要な情報をはっきり指定するラベルを表示したりできます。意思決定を最小限にしてデータ入力を高速化するため、妥当なデフォルト値をあらかじめフィールドに入力しておくこともできます。

**必要に応じてセキュリティ保護されたテキスト入力フィールドを使う。** 機密データを必要とするアプリやゲームでは、ユーザの入力内容が表示されないフィールドを使用します（通常、入力文字の代わりに小さい「●」が表示される）。デベロッパ向けのガイダンスは、[`SecureField`](/documentation/SwiftUI/SecureField)を参照してください。tvOSでは、[数字入力ビュー](https://developer.apple.com/jp/design/human-interface-guidelines/digit-entry-views)を設定して、ユーザが入力した数字を隠すこともできます（デベロッパ向けのガイダンスは、[`isSecureDigitEntry`](/documentation/TVUIKit/TVDigitEntryViewController/isSecureDigitEntry)を参照してください）。visionOSでは、システム定義のテキストフィールドを使えば、入力されたデータは装着者のみに表示され、ほかの人には表示されません。例えば、AirPlayを使ってコンテンツをストリーミングするときにはセキュアテキストフィールドに自動的にぼかしがかかります。

**パスワードフィールドの内容は自動入力しないようにする。** パスワードの入力または生体認証やキーチェーン認証の使用は必ずユーザに要求するようにしてください。ガイダンスは、[アカウントの管理](/jp/design/human-interface-guidelines/managing-accounts)を参照してください。

**できるだけテキスト入力ではなく選択方式にする。** キーボードに慣れたユーザでも、通常は、情報をタイプするよりリストから選択する方が簡単で効率も高くなります。状況に応じて、必要な情報をユーザが簡単に提供できる方法として、ピッカー、メニューなどの選択コンポーネントの使用を検討してください。

**できる限り、ユーザがドラッグ＆ドロップやペーストでデータを入力できるようにする。** これらの操作に対応すれば、データ入力を簡素化できるだけでなく、アプリとシステムとの統合性をユーザに強く体感してもらえます。

**フィールドの値を動的に検証する。** 長いフォームに入力したあとで、戻って間違いを修正しなければならないという流れは、ユーザのイライラの原因になります。ユーザが入力した直後にその値を確認し、問題を検出したらすぐにフィードバックを提示するようにすれば、その場で間違いを訂正できます。特に数値データの場合は、数値データのみを受け付けるようにテキストフィールドを自動的に設定する数字フォーマットの使用を検討してください。パーセント表示や通貨表示などでの小数点以下の桁数を決めるなど、値を特定の方法で表示するようにフォーマッタを設定することもできます。

**データ入力が必要な場合は、必須データを提供するまで次に進めないことがユーザに分かるようにする。** 例えば、一連のテキストフィールドのあとに「次へ」または「続ける」ボタンを置く場合は、必須データが入力されるまでボタンを選択できないようにします。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/entering-data#Platform-considerations)

 _iOS、iPadOS、tvOS、visionOS、watchOSに追加の考慮事項はありません。_

### [macOS](/jp/design/human-interface-guidelines/entering-data#macOS)

**フィールドにテキストを表示しきれない場合、拡張ツールヒントでテキスト全体を表示することを検討する。** _拡張ツールチップ_ はポインタをフィールドに合わせたときに表示され、通常のツールチップのように動作します。macOSで実行されるアプリ（Macで実行されるiOSおよびiPadOSのアプリを含む）では、テキストフィールドが小さすぎてユーザが入力したデータ全体を表示できない場合、データ全体を表示する手段として拡張ツールチップを使えます。ガイダンスは[「ヘルプの提供」＞「macOS、visionOS」](https://developer.apple.com/jp/design/human-interface-guidelines/offering-help#macOS-visionOS)を参照してください。

## [リソース](/jp/design/human-interface-guidelines/entering-data#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/entering-data#Related)

[テキストフィールド](/jp/design/human-interface-guidelines/text-fields)

[仮想キーボード](/jp/design/human-interface-guidelines/virtual-keyboards)

[キーボード](/jp/design/human-interface-guidelines/keyboards)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/entering-data#Developer-documentation)

[入力イベント](/documentation/SwiftUI/Input-events) — SwiftUI

#### [ビデオ](/jp/design/human-interface-guidelines/entering-data#Videos)

[](https://developer.apple.com/videos/play/wwdc2021/10059)

## [変更履歴](/jp/design/human-interface-guidelines/entering-data#Change-log)

日付| 変更内容  
---|---  
2023年6月21日| visionOSのガイダンスを追加するために更新。

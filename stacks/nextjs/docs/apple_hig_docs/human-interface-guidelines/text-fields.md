# テキストフィールド

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/text-fields

# テキストフィールド

テキストフィールドは、少量の特定のテキストを入力または編集できる四角形の領域です。

![図案化されたテキストフィールド。値が含まれています。画像全体が、6色の初代Appleロゴの赤色を連想させる赤みを帯びています。](https://docs-assets.developer.apple.com/published/b22fcac3cbc20d3599a6e7e492edb155/components-text-field-intro%402x.png)

## [ベストプラクティス](/jp/design/human-interface-guidelines/text-fields#Best-practices)

**テキストフィールドは、名前やメールアドレスのような少量の情報をリクエストする際に使用する。** 大量のテキストを入力できるようにする場合は、[テキストビュー](/jp/design/human-interface-guidelines/text-views)を使用します。

**テキストフィールドには目的を伝えるヒントを表示する。** テキストフィールドには、フィールド内にテキストが入力されていないときに表示されるプレースホルダテキスト（「メール」や「パスワード」など）を含めることができます。ユーザの入力が始まるとプレースホルダテキストは表示されなくなるので、フィールドの目的が分からなくならないように、フィールドを説明するラベルを別途提供してもよいでしょう。

**セキュアテキストフィールドを使用してプライベートなデータが表示されないようにする。** パスワードなど、アプリで機密性の高いデータを要求するときは、必ずセキュアテキストフィールドを使ってください。デベロッパ向けのガイダンスは、[`SecureField`](/documentation/SwiftUI/SecureField)を参照してください。

**テキストフィールドのサイズは想定されるテキストの量に可能な限り合わせる。** ユーザは、テキストフィールドのサイズから、入力する情報の量を視覚的に判断します。

**テキストフィールドが複数ある場合は均等に間隔を空けて配置する。** レイアウトに複数のテキストフィールドが含まれている場合は、入力フィールドと説明ラベルの対応関係が簡単に判断できるように、十分な間隔を空けます。可能な場合は複数のテキストフィールドを縦に並べ、幅に一貫性を持たせてレイアウトを整理します。例えば、住所入力フォームの姓と名のフィールドの幅を揃え、市区町村や番地などのフィールドはまた違う幅にするなどします。

**フィールド間のタブ移動が期待通りに動作するようにする。** フィールド間をタブで移動するときに自然な順序でフォーカスが移動するようにします。システムは自動的にこの動作を実現しようとするので、通常、カスタマイズは必要になりません。

**適宜フィールドで検証を実行する。** 例えば、数字列しか認めないフィールドの場合は、数字以外の文字が入力されたときにアプリからアラートを出す必要があります。データをチェックすべきタイミングはコンテキストによって異なります。メールアドレスを入力するフィールドの場合は、フォーカスが移動したときに検証するのが最適です。ユーザ名やパスワードを作成するフィールドの場合は、別のフィールドに切り替える前に検証を行う必要があります。

**数値データには数字フォーマットを使用する。** 数字フォーマットを使用すると、数値だけを受け付けるように自動的にテキストフィールドが設定されます。小数点以下の桁数を固定したり、パーセント表示や通貨表示にしたりするなど、値の表示方法を指定することもできます。ただし、フォーマットはロケールによって大きく異なる場合があるので、データの実際の表示のされ方を決めてかからないようにしてください。

![縦に並んだ2個のテキストフィールドを写した部分的なスクリーンショット。上のフィールドには、4桁の小数部がある数値が含まれています。下のフィールドには、通貨が含まれています。](https://docs-assets.developer.apple.com/published/28ce9155626abdfb0d96c7394c0a2fc8/text-fields-formatted-text%402x.png)フォーマットされたテキスト

**フィールドのニーズに応じて改行を調整する。** デフォルトでは、テキストフィールドの境界をはみ出したテキストはすべて切り詰められます。または、文字や単語の境目で改行してテキストを折り返したり、先頭や中央、末尾を切り詰めて省略記号を表示したりするようにテキストフィールドを設定することもできます。

![テキストフィールドを写した部分的なスクリーンショット。途中で切れている文が含まれています。](https://docs-assets.developer.apple.com/published/4f5087014620cf61ae6e6cf691766376/text-fields-clipped-text%402x.png)切れたテキスト

![テキストフィールドを写した部分的なスクリーンショット。2行に折り返されている文が含まれています。](https://docs-assets.developer.apple.com/published/5e7b94570af0f50c9e9a3061a428aa15/text-fields-wrapped-text%402x.png)折り返されたテキスト

![テキストフィールドを写した部分的なスクリーンショット。末尾の語句の代わりに省略記号が表示された文が含まれています。](https://docs-assets.developer.apple.com/published/ad0040baa8369af2dbd9ab88a25c3439/text-fields-truncated-text%402x.png)省略されたテキスト

**テキストを表示しきれない場合は拡張ツールチップでテキスト全体を見せることを検討する。** 拡張ツールチップは通常の[ツールチップ](https://developer.apple.com/jp/design/human-interface-guidelines/offering-help#macOS-visionOS)のように動作し、ユーザがフィールドにポインタを置いたときに表示されます。

**iOS、iPadOS、tvOS、visionOSのアプリでは、適切なキーボードタイプを表示する。** 数字やURLなどの入力内容に合わせて最適化された、複数のタイプのキーボードを利用できます。データを効率よく入力できるように、入力するコンテンツのタイプに適したキーボードが表示されるようにしてください。ガイダンスは、[仮想キーボード](/jp/design/human-interface-guidelines/virtual-keyboards)を参照してください。

**tvOSおよびwatchOSのアプリではテキストの入力を最小限にとどめる。** Apple TVやApple Watchでテキストを長々と打ち込んだり、いくつものテキストフィールドに入力したりするのは時間がかかります。テキストの入力は最小限にとどめ、ボタンなどを使って情報を効率よく入力できるようにすることを検討してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/text-fields#Platform-considerations)

 _tvOS、visionOSに追加の考慮事項はありません。_

### [iOS/iPadOS](/jp/design/human-interface-guidelines/text-fields#iOS-iPadOS)

**テキストフィールドの末尾側に消去ボタンを表示して入力を消しやすくする。** この要素があれば、Deleteキーを何度もタップすることなく、消去ボタンのタップでテキストフィールドの内容を消去できます。

**画像とボタンを使用してテキストフィールドを分かりやすくしたり機能を持たせたりする。** テキストフィールドの両側にカスタム画像を表示したり、「ブックマーク」ボタンなどのシステム標準のボタンを追加したりできます。基本的に、フィールドの目的を示すものはテキストフィールドの先頭側に、ブックマークなどの追加機能は末尾側に配置します。

### [macOS](/jp/design/human-interface-guidelines/text-fields#macOS)

**テキスト入力と選択肢を組み合わせたい場合はコンボボックスの使用を検討する。** 関連するガイダンスは、[コンボボックス](/jp/design/human-interface-guidelines/combo-boxes)を参照してください。

### [watchOS](/jp/design/human-interface-guidelines/text-fields#watchOS)

**テキストフィールドは必要な場合に限り表示する。** 可能な場合は、テキスト入力を必須にするのではなく、選択肢のリストを表示します。

## [リソース](/jp/design/human-interface-guidelines/text-fields#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/text-fields#Related)

[テキストビュー](/jp/design/human-interface-guidelines/text-views)

[コンボボックス](/jp/design/human-interface-guidelines/combo-boxes)

[データの入力](/jp/design/human-interface-guidelines/entering-data)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/text-fields#Developer-documentation)

[`TextField`](/documentation/SwiftUI/TextField) — SwiftUI

[`SecureField`](/documentation/SwiftUI/SecureField) — SwiftUI

[`UITextField`](/documentation/UIKit/UITextField) — UIKit

[`NSTextField`](/documentation/AppKit/NSTextField) — AppKit

## [変更履歴](/jp/design/human-interface-guidelines/text-fields#Change-log)

日付| 変更内容  
---|---  
2023年6月05日| watchOS 10の変更点を反映するためにガイダンスを更新。

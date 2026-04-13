# テキストビュー

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/text-views

# テキストビュー

テキストビューは、複数行のスタイル付きテキストコンテンツを表示します。任意で編集可能にできます。

![図案化されたフィールド。テキストが含まれています。画像全体が、6色の初代Appleロゴの赤色を連想させる赤みを帯びています。](https://docs-assets.developer.apple.com/published/98045b4ad3922633479d6ecea8f6cb82/components-text-view-intro%402x.png)

テキストビューは任意の高さにすることができ、コンテンツがビューの枠に収まらないときはスクロールが可能です。テキストビュー内のコンテンツは、デフォルトではビューの先頭側揃えになり、システムのラベルカラーが使用されます。iOS、iPadOS、visionOSでは、編集可能なテキストビューを選択するとキーボードが表示されます。

## [ベストプラクティス](/jp/design/human-interface-guidelines/text-views#Best-practices)

**長いテキストや編集可能なテキスト、特殊なフォーマットのテキストを表示する場合に使用する。** テキストビューは、[テキストフィールド](/jp/design/human-interface-guidelines/text-fields)や[ラベル](/jp/design/human-interface-guidelines/labels)とは異なります。テキストビューには、特殊なテキストを表示したり、テキスト入力を受け取ったりするためのほとんどのオプションが用意されています。表示するテキストが少量の場合は、ラベルまたはテキストフィールド（編集可能なテキストを扱う場合）を使う方がシンプルです。

**テキストを読みやすくする。** さまざまなフォント、カラー、配置で工夫することはできますが、コンテンツの可読性を維持することが肝心です。ユーザがデバイスでテキストのサイズを変えても読みにくくならないように、ダイナミックタイプを採用することをおすすめします。文字を太くするなどのアクセシビリティオプションをオンにしてコンテンツをテストすることを忘れないでください。ガイダンスは、[アクセシビリティ](/jp/design/human-interface-guidelines/accessibility)および[タイポグラフィ](/jp/design/human-interface-guidelines/typography)を参照してください。

**有用なテキストは選択可能にする。** エラーメッセージ、シリアル番号、IPアドレスなどの有用な情報がテキストビューに含まれる場合は、ユーザがその情報を選択してほかの場所にコピー&ペーストできるようにすることを検討してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/text-views#Platform-considerations)

 _macOS、visionOS、watchOSに追加の考慮事項はありません。_

### [iOS/iPadOS](/jp/design/human-interface-guidelines/text-views#iOS-iPadOS)

**適切なキーボードを表示する。** 入力内容に合わせて最適化された、複数のタイプのキーボードを利用できます。データを効率よく入力できるように、テキストビューの編集時にコンテンツのタイプに適したキーボードが表示されるようにする必要があります。ガイダンスは、[仮想キーボード](/jp/design/human-interface-guidelines/virtual-keyboards)を参照してください。

### [tvOS](/jp/design/human-interface-guidelines/text-views#tvOS)

tvOSでもテキストをテキストビューで表示できます。ただし、tvOSは最低限のテキスト入力しかできない設計のため、編集可能なテキストには[テキストフィールド](/jp/design/human-interface-guidelines/text-fields)が使用されます。

## [リソース](/jp/design/human-interface-guidelines/text-views#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/text-views#Related)

[ラベル](/jp/design/human-interface-guidelines/labels)

[テキストフィールド](/jp/design/human-interface-guidelines/text-fields)

[コンボボックス](/jp/design/human-interface-guidelines/combo-boxes)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/text-views#Developer-documentation)

[`Text`](/documentation/SwiftUI/Text) — SwiftUI

[`UITextView`](/documentation/UIKit/UITextView) — UIKit

[`NSTextView`](/documentation/AppKit/NSTextView) — AppKit

## [変更履歴](/jp/design/human-interface-guidelines/text-views#Change-log)

日付| 変更内容  
---|---  
2023年6月05日| watchOS 10の変更点を反映するためにガイダンスを更新。

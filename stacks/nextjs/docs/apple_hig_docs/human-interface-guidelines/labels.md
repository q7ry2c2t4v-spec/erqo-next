# ラベル

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/labels

# ラベル

ラベルはユーザが読むことができる静的なテキストです。多くの場合コピーはできますが、編集はできません。

![図案化されたテキストラベル。画像は6色のオリジナルAppleロゴをイメージさせる赤色になっています。](https://docs-assets.developer.apple.com/published/048d6e97718c4b738eeeb457121b1d6f/components-label-intro%402x.png)

インターフェイス全体で、ボタン、メニュー項目、ビューのラベルにテキストが表示され、ユーザはこれによって現在のコンテンツや、次に何ができるかを認識できます。

 _ラベル_ という用語は、さまざまな場所に表示される編集不可のテキストを指します。以下に例を示します:

  * ボタン内では、ラベルは一般に「編集」、「キャンセル」、「送信」などのボタンの機能を伝えます。

  * 多くのリスト内では、ラベルで各項目を説明できます。ラベルにシンボルや画像が添えられることもよくあります。

  * ビュー内では、ラベルにコントロールの紹介やユーザがビュー内で実行できる一般的な操作やタスクの説明が表示されることで、コンテキストが追加される場合があります。

デベロッパ向けメモ

SwiftUIでは、編集不可のテキストを表示するために、 [`Label`](/documentation/SwiftUI/Label) と[`Text`](/documentation/SwiftUI/Text)の2つのコンポーネントが定義されています。

以下のガイドでは、ラベルを使ってテキストを表示する方法について説明します。[アクションボタン](https://developer.apple.com/jp/design/human-interface-guidelines/buttons)、[メニュー](https://developer.apple.com/jp/design/human-interface-guidelines/menus)、[リストおよびテーブル](https://developer.apple.com/jp/design/human-interface-guidelines/lists-and-tables)などの特定のコンポーネントについてのガイドには、テキストの使用に関する追加の推奨事項が含まれる場合があります。

## [ベストプラクティス](/jp/design/human-interface-guidelines/labels#Best-practices)

**ラベルはユーザが編集する必要がない少量のテキストを表示するために使用する。** 少量のテキストをユーザが編集できるようにしたい場合は、[テキストフィールド](https://developer.apple.com/jp/design/human-interface-guidelines/text-fields)を使用します。大量のテキストを表示し、適宜ユーザが編集できるようにする必要がある場合は、[テキストビュー](https://developer.apple.com/jp/design/human-interface-guidelines/text-views)を使用します。

**システムフォントを優先する。** ラベルは、プレーンテキストまたはスタイル付きテキストを表示でき、デフォルトでダイナミックタイプに対応します（使用可能な場所の場合）。ラベルのスタイルを調整するか、カスタムフォントを使用する場合は、必ずテキストを読めるようにしてください。

**システムで提供されるラベルカラーを使って相対的な重要度を伝える。** システムでは見た目の異なる4つのラベルカラーが定義されていて、テキストに異なるレベルの視覚的重要度を割り当てることができます。追加のガイダンスは、[カラー](/jp/design/human-interface-guidelines/color)を参照してください。

システムカラー| 使用例| iOS、iPadOS、tvOS、visionOS| macOS  
---|---|---|---  
ラベル| 一次情報| [`label`](/documentation/UIKit/UIColor/label)| [`labelColor`](/documentation/AppKit/NSColor/labelColor)  
第2ラベル| サブ見出しまたは補足テキスト| [`secondaryLabel`](/documentation/UIKit/UIColor/secondaryLabel)| [`secondaryLabelColor`](/documentation/AppKit/NSColor/secondaryLabelColor)  
第3ラベル| 使用不可の項目または動作について説明するテキスト| [`tertiaryLabel`](/documentation/UIKit/UIColor/tertiaryLabel)| [`tertiaryLabelColor`](/documentation/AppKit/NSColor/tertiaryLabelColor)  
第4ラベル| ウォーターマークテキスト| [`quaternaryLabel`](/documentation/UIKit/UIColor/quaternaryLabel)| [`quaternaryLabelColor`](/documentation/AppKit/NSColor/quaternaryLabelColor)  
  
**有用なラベルテキストは選択可能にする。** エラーメッセージ、場所、IPアドレスなどの有用な情報がラベルに含まれる場合は、ユーザがその情報を選択してほかの場所にコピー&ペーストできるようにすることを検討してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/labels#Platform-considerations)

 _iOS、iPadOS、tvOS、visionOSに追加の考慮事項はありません。_

### [macOS](/jp/design/human-interface-guidelines/labels#macOS)

デベロッパ向けメモ

ラベルに編集不可のテキストを表示するには、[`NSTextField`](/documentation/AppKit/NSTextField)の[`isEditable`](/documentation/AppKit/NSTextField/isEditable)プロパティを使用します。

### [watchOS](/jp/design/human-interface-guidelines/labels#watchOS)

日付と時刻のテキストコンポーネント（下の左側の図）には、現在の日付、現在時刻、またはその両方の組み合わせが表示されます。日付のテキストコンポーネントは、さまざまなフォーマット、カレンダー、タイムゾーンを使って構成できます。カウントダウンタイマーのテキストコンポーネント（下の右側の図）には、正確なカウントアップタイマーまたはカウントダウンタイマーが表示されます。タイマーのテキストコンポーネントは、さまざまなフォーマットのカウント値を使って構成できます。

![Apple Watchの日付と時刻のテキストコンポーネントの図。日付は先頭側に揃えられ、時刻は末尾側に揃えられています。](https://docs-assets.developer.apple.com/published/2985845727ef269e085718ce62ec8d62/labels-date-time-text-component%402x.png)日付と時刻のラベル

![Apple Watchのカウントダウンタイマーのテキストコンポーネントの図。中央に時間が表示されています。](https://docs-assets.developer.apple.com/published/bc3014364c7bc508ff68d21d79c15441/labels-countdown-timer-text-component%402x.png)タイマーラベル

システムで提供される日付とタイマーのテキストコンポーネントを使うと、使用可能な領域に合わせてラベルの表示がwatchOSで自動的に調整されます。また、アプリからそれ以上入力がなくてもラベルの内容がアップデートされます。

コンプリケーションでは日付とタイマーのコンポーネントを使用することを検討してください。デザインのガイダンスは[コンプリケーション](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications)を、デベロッパ向けのガイダンスは[`Text`](/documentation/SwiftUI/Text)を参照してください。

## [リソース](/jp/design/human-interface-guidelines/labels#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/labels#Related)

[テキストフィールド](/jp/design/human-interface-guidelines/text-fields)

[テキストビュー](/jp/design/human-interface-guidelines/text-views)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/labels#Developer-documentation)

[`Label`](/documentation/SwiftUI/Label) — SwiftUI

[`Text`](/documentation/SwiftUI/Text) — SwiftUI

[`UILabel`](/documentation/UIKit/UILabel) — UIKit

[`NSTextField`](/documentation/AppKit/NSTextField) — AppKit

## [変更履歴](/jp/design/human-interface-guidelines/labels#Change-log)

日付| 変更内容  
---|---  
2023年6月05日| watchOS 10の変更点を反映するためにガイダンスを更新。

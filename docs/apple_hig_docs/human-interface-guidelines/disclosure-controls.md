# 開閉コントロール

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/disclosure-controls

# 開閉コントロール

開閉コントロールで、特定のコントロールやビューに関連する情報や機能を表示したり非表示にしたりできます。

![折りたたまれた状態と展開された状態の、図案化された開閉用矢印ボタン。画像は6色のオリジナルAppleロゴをイメージさせる赤色になっています。](https://docs-assets.developer.apple.com/published/063be45e9cfc9633839b22e0377ffe3f/components-disclosure-control-intro%402x.png)

## [ベストプラクティス](/jp/design/human-interface-guidelines/disclosure-controls#Best-practices)

**詳細な情報は、それが必要になるまで開閉コントロールを使って非表示にする。** ユーザが使用する可能性が最も高いコントロールは、常にユーザに見えるように階層の最上位に配置し、より詳細な内容はデフォルトでは非表示にします。このような構造にすることで、ユーザは大量の詳細オプションに煩わされずに、最も重要な情報を素早く見つけることができます。

## [開閉用三角ボタン](/jp/design/human-interface-guidelines/disclosure-controls#Disclosure-triangles)

開閉用三角ボタンで、ビューや項目のリストに関連する情報と機能を表示したり非表示にしたりできます。例えばKeynoteでは、開閉用三角ボタンを使用して、プレゼンテーションを書き出す際の詳細オプションを表示できます。Finderでは、開閉用三角ボタンを使用して、リスト表示のフォルダ構造内を移動する際に徐々に階層を開いていけます。

![Finderのリスト表示の3つのフォルダの図。フォルダが折りたたまれていて、先頭側に内側を向いた開閉用三角ボタンがあり、展開してコンテンツを表示できることを示しています。](https://docs-assets.developer.apple.com/published/0d09efac5aa8b9fac9e1f049de778e60/disclosure-triangle-before%402x.png)

![Finderのリスト表示の3つのフォルダの図。1つ目と3つ目のフォルダは折りたたまれていて、先頭側に内側を向いた開閉用三角ボタンがあり、展開してコンテンツを表示できることを示しています。2つ目のフォルダは展開されていて、開閉用三角ボタンは下を向き、中の3つのサブフォルダが表示されています。](https://docs-assets.developer.apple.com/published/8fc884ec5e52941497afcbe7017ec09a/disclosure-triangle-after%402x.png)

開閉用三角ボタンは先頭側に配置され、コンテンツが非表示のときは先端が内側を向いています。コンテンツが表示されているときは、先端が下を向いています。開閉用三角ボタンをクリックまたはタップすることでこれら2つの状態が切り替わり、コンテンツを含むビューが拡げられたり折りたたまれたりします。

**開閉用三角ボタンを使うときは分かりやすいラベルを表示する。** 例えば「詳細オプション」のように、何が表示されたり非表示になったりするのかが分かるラベルを表示してください。

デベロッパ向けのガイダンスは、[`NSButton.BezelStyle.disclosure`](/documentation/AppKit/NSButton/BezelStyle-swift.enum/disclosure)を参照してください。

## [開閉用矢印ボタン](/jp/design/human-interface-guidelines/disclosure-controls#Disclosure-buttons)

開閉用矢印ボタンで、特定のコントロールに関連する機能を表示したり非表示にしたりできます。例えばmacOSで保存操作を実行すると、「別名で保存」テキストフィールドの横に開閉用矢印ボタンが表示されます。ユーザがこのボタンをクリックまたはタップすると、「保存」ダイアログが展開し、書類の出力場所を選択するオプションが表示されます。

コンテンツが非表示のときは開閉用矢印ボタンの先端が下を向いています。コンテンツが表示されているときは上を向いています。開閉用矢印ボタンのクリックまたはタップでこれら2つの状態が切り替わり、コンテンツを含むビューが拡げられたり折りたたまれたりします。

![macOSのスクリーンショット。折りたたまれた「保存」ダイアログが表示されています。ダイアログには、折りたたまれた状態の開閉用三角ボタンがあります。拡げられると追加のオプションが表示されます。](https://docs-assets.developer.apple.com/published/390e6782017895f5f14f17cb1f448e91/disclosure-button-before%402x.png)

![macOSのスクリーンショット。拡げられた「保存」ダイアログが表示されています。ダイアログには、拡げられた状態の開閉用三角ボタンがあります。閉じると追加のオプションが非表示になります。](https://docs-assets.developer.apple.com/published/cd69db367e508445743eeb62bad57c10/disclosure-button-after%402x.png)

**開閉用矢印ボタンは表示と非表示を切り替えるコンテンツの近くに配置する。** ユーザがボタンをクリックまたはタップしたときに表示される選択肢と元のコントロールとの関係が明確になるようにしてください。

**1つのビューで複数の開閉用矢印ボタンを使わない。** 複数の開閉用矢印ボタンがあるとインターフェイスが複雑になり、混乱の元です。

デベロッパ向けのガイダンスは、[`NSButton.BezelStyle.pushDisclosure`](/documentation/AppKit/NSButton/BezelStyle-swift.enum/pushDisclosure)を参照してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/disclosure-controls#Platform-considerations)

 _macOSに追加の考慮事項はありません。tvOSとwatchOSには対応していません。_

### [iOS、iPadOS、visionOS](/jp/design/human-interface-guidelines/disclosure-controls#iOS-iPadOS-visionOS)

iOS、iPadOS、visionOSでは、SwiftUI[`DisclosureGroup`](/documentation/SwiftUI/DisclosureGroup)ビューで開閉コントロールを利用できます。

## [リソース](/jp/design/human-interface-guidelines/disclosure-controls#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/disclosure-controls#Related)

[アウトラインビュー](/jp/design/human-interface-guidelines/outline-views)

[リストとテーブル](/jp/design/human-interface-guidelines/lists-and-tables)

[ボタン](/jp/design/human-interface-guidelines/buttons)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/disclosure-controls#Developer-documentation)

[`DisclosureGroup`](/documentation/SwiftUI/DisclosureGroup) — SwiftUI

[`NSButton.BezelStyle.disclosure`](/documentation/AppKit/NSButton/BezelStyle-swift.enum/disclosure) — AppKit

[`NSButton.BezelStyle.pushDisclosure`](/documentation/AppKit/NSButton/BezelStyle-swift.enum/pushDisclosure) — AppKit

#### [ビデオ](/jp/design/human-interface-guidelines/disclosure-controls#Videos)

[](https://developer.apple.com/videos/play/wwdc2020/10031)

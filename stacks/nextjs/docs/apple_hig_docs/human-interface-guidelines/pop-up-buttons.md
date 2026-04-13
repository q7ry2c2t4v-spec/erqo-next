# ポップアップボタン

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/pop-up-buttons

# ポップアップボタン

ポップアップボタンは、択一的なオプションを含むメニューを表示します。

![選択肢を表示している図案化されたポップアップボタン。画像は6色のオリジナルAppleロゴをイメージさせる赤色になっています。](https://docs-assets.developer.apple.com/published/e666d7b1d75bbafa32bcd3885b3fc0e6/components-pop-up-button-intro%402x.png)

ユーザがポップアップボタンのメニューから項目を選択すると、メニューが閉じ、ボタンのコンテンツがアップデートされて現在の選択値が表示されます。

![iPhoneの「カレンダー」のスクリーンショット。編集する新しいカレンダーの予定が開いています。編集画面には、予定の開始日と終了日、移動時間、繰り返しの間隔、カレンダー、予定出席者、通知のオプション、添付ファイルなど、予定の詳細を設定するためのコントロールが含まれています。](https://docs-assets.developer.apple.com/published/05014cb408eb3a845b9c50fedb75c546/pop-up-button-closed%402x.png)

![iPhoneの「カレンダー」のスクリーンショット。編集する新しいカレンダーの予定が開いています。ポップアップボタンのメニューが繰り返しボタンから開いて、プリセットオプションのリストから繰り返しの間隔を選んだり、カスタムの間隔を作成したりするためのオプションが表示されます。](https://docs-assets.developer.apple.com/published/cdf93d50f8511a91e2bb4efedb778b5b/pop-up-button-open%402x.png)

## [ベストプラクティス](/jp/design/human-interface-guidelines/pop-up-buttons#Best-practices)

**ポップアップボタンは択一的なオプションや状態を含むフラットなリストを提示する場合に使用する。** ポップアップボタンは、ユーザがコンテンツやその周囲のビューに影響する選択を行うのに役立ちます。以下の必要がある場合は、ポップアップボタンの代わりに[プルダウンボタン](https://developer.apple.com/jp/design/human-interface-guidelines/pull-down-buttons)を使います:

  * アクションのリストを提示する

  * 複数の項目を選択できるようにする

  * サブメニューを含める

**デフォルトで選択する項目は実用的なものにする。** ポップアップボタンでは、項目を選択することでコンテンツをアップデートできますが、ユーザが選択をまだ行っていない場合はアプリ側で指定したデフォルト項目が表示されます。なるべく大多数のユーザが選択する可能性の高い項目をデフォルトの選択項目にしてください。

**ポップアップボタンを開く前にオプションの内容を推測できるようにする。** 例えば、内容を推測しやすいラベルやボタンラベルを付ければ、ボタンの効果が理解でき、何に対するオプションの選択を行うのかが明確に伝わります。

**スペースが限られていて、すべてのオプションを常に表示する必要がない場合は、ポップアップボタンの使用を検討する。** ポップアップボタンは、幅広いさまざまな選択肢を提示するためのスペース効率のよい方法です。

**ユーザにとって有用と思われる追加項目は、必要に応じてポップアップボタンのメニューにカスタムオプションとして含める。** カスタムオプションとしてメニュー内に含めることで、ユーザがたまにしか必要としない項目やコントロールでインターフェイスが煩雑になるのを防ぐことができます。ユーザがオプションの効果を理解できるように、リストの下に説明テキストを表示することもできます。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/pop-up-buttons#Platform-considerations)

 _iOS、macOS、visionOSに追加の考慮事項はありません。tvOSとwatchOSには対応していません。_

### [iPadOS](/jp/design/human-interface-guidelines/pop-up-buttons#iPadOS)

**ポップオーバーまたはモーダルビュー内では、開閉用インジケータの代わりにポップアップボタンを使用して、リスト項目に複数のオプションを提示する手法を検討する。** こうすることにより、ユーザは詳細ビューに移動することなく、ポップアップボタンのメニューからオプションを素早く選択できます。項目数が十分に少なく、オプションの定義が明確であるような場合は、ポップアップボタンを使用することを検討してください。

## [リソース](/jp/design/human-interface-guidelines/pop-up-buttons#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/pop-up-buttons#Related)

[プルダウンボタン](/jp/design/human-interface-guidelines/pull-down-buttons)

[ボタン](/jp/design/human-interface-guidelines/buttons)

[メニュー](/jp/design/human-interface-guidelines/menus)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/pop-up-buttons#Developer-documentation)

[`MenuPickerStyle`](/documentation/SwiftUI/MenuPickerStyle) — SwiftUI

[`changesSelectionAsPrimaryAction`](/documentation/UIKit/UIButton/changesSelectionAsPrimaryAction) — UIKit

[`NSPopUpButton`](/documentation/AppKit/NSPopUpButton) — AppKit

## [変更履歴](/jp/design/human-interface-guidelines/pop-up-buttons#Change-log)

日付| 変更内容  
---|---  
2023年10月24日| アートワークを追加。  
2022年9月14日| iPadOSのポップオーバーまたはモーダルビューでのポップアップボタンの使用に関するガイドラインを追加。

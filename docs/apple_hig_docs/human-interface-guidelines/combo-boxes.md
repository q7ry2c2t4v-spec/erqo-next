# コンボボックス

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/combo-boxes

# コンボボックス

コンボボックスは、テキストフィールドとプルダウンボタンが1つのコントロールにまとめられたものです。

![都市の一覧を表示する図案化されたコンボボックスのコントロール。画像は6色のオリジナルAppleロゴをイメージさせる赤色になっています。](https://docs-assets.developer.apple.com/published/78645121fef80e5ffc56b01e72fad4df/components-combobox-intro%402x.png)

ユーザは、フィールドにカスタム値を入力することも、ボタンをクリックしてリストから定義済みの値を選択することもできます。ユーザがカスタム値を入力しても、その値は定義済み値のリストには追加されません。

## [ベストプラクティス](/jp/design/human-interface-guidelines/combo-boxes#Best-practices)

**フィールドのデフォルト値として、リストにある有用な値をあらかじめ設定しておく。** デフォルト状態のフィールドは空白にしてもかまいませんが、隠れている選択肢のいずれかをデフォルト値として設定しておくことをおすすめします。デフォルト値はリストの最初の項目である必要はありません。

**どんなタイプの項目を入力すればよいかを示す分かりやすいラベルを表示する。** 基本的に、ラベルはタイトル形式の文字列にし、最後にコロンを付けます。関連のガイダンスは[ラベル](/jp/design/human-interface-guidelines/labels)を参照してください。

**関連性の高い選択肢を提示する。** カスタム値を入力できる機能だけでなく、よく使う項目をリストから選ぶ方法も提供すると、ユーザの利便性が高まります。

**リストの項目がテキストフィールドの幅を超えないようにする。** 項目が長すぎると、テキストフィールドでテキスト切れが発生して項目が読めなくなるおそれがあります。

ガイダンスは、[テキストフィールド](/jp/design/human-interface-guidelines/text-fields)および[プルダウンボタン](/jp/design/human-interface-guidelines/pull-down-buttons)を参照してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/combo-boxes#Platform-considerations)

 _iOS、iPadOS、tvOS、visionOS、watchOSには対応していません。_

## [リソース](/jp/design/human-interface-guidelines/combo-boxes#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/combo-boxes#Related)

[テキストフィールド](/jp/design/human-interface-guidelines/text-fields)

[プルダウンボタン](/jp/design/human-interface-guidelines/pull-down-buttons)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/combo-boxes#Developer-documentation)

[`NSComboBox`](/documentation/AppKit/NSComboBox) — AppKit

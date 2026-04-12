# ステッパー

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/steppers

# ステッパー

ステッパーは、インクリメント値を増減できる2つのセグメントからなるコントロールです。

![図案化されたステッパーコントロール。画像全体が、6色の初代Appleロゴの赤色を連想させる赤みを帯びています。](https://docs-assets.developer.apple.com/published/0dad81ea5c2ee32c4e8d91f12f9853c9/components-stepper-intro%402x.png)

ステッパー自体は値を表示しないので、現在の値を表示するフィールドの横に配置します。

## [ベストプラクティス](/jp/design/human-interface-guidelines/steppers#Best-practices)

**ステッパーで変更できる値を明確にする。** ステッパー自体は何の値も表示しないので、ステッパーでどの値を変更できるのかが分かるようにします。

**値が大きく変更されることが想定される場合は、ステッパーとテキストフィールドを組み合わせることを検討する。** 数回のタップやクリックで済む程度のわずかな変更であればステッパーで十分ですが、特にユーザが値を大きく変更する可能性がある場合は、具体的な値を入力できるフィールドも選択肢として用意されている方がユーザに喜ばれます。例えばプリント画面なら、ステッパーとテキストフィールドの両方を使って部数を設定できる方が便利でしょう。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/steppers#Platform-considerations)

 _iOS、iPadOS、visionOSに追加の考慮事項はありません。watchOSとtvOSには対応していません。_

### [macOS](/jp/design/human-interface-guidelines/steppers#macOS)

**値の範囲が広い場合は、Shiftキーを押しながらのクリックで値を素早く変えられるようにすることを検討する。** ステッパーの値を大きく変更できると便利なアプリの場合は、Shiftキーを押しながらステッパーをクリックしてデフォルトのインクリメントより大きく値を変更できるようになっていると便利でしょう（例えばデフォルトの10倍など）。

## [リソース](/jp/design/human-interface-guidelines/steppers#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/steppers#Related)

[ピッカー](/jp/design/human-interface-guidelines/pickers)

[テキストフィールド](/jp/design/human-interface-guidelines/text-fields)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/steppers#Developer-documentation)

[`UIStepper`](/documentation/UIKit/UIStepper) — UIKit

[`NSStepper`](/documentation/AppKit/NSStepper) — AppKit

# 数字入力ビュー

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/digit-entry-views

# 数字入力ビュー

数字入力ビューは画面全体に表示されるコンポーネントで、PINなど複数桁の数字を数字専用キーボードを使って入力するようにユーザに促します。

![Apple TVの図案化された5桁のパスコード入力画面。画像は6色のオリジナルAppleロゴをイメージさせる赤色になっています。](https://docs-assets.developer.apple.com/published/5dff3898f16f6f6eabf6909d5f18551b/components-digit-entry-view-intro%402x.png)

数字の並びの上にオプションでタイトルやプロンプトを追加できます。

## [ベストプラクティス](/jp/design/human-interface-guidelines/digit-entry-views#Best-practices)

**せキュア数字フィールドを使用する。** せキュア数字フィールドでは、ユーザが入力した数字の代わりにアスタリスク（*）が表示されます。アプリで機密性の高いデータを要求するときには必ず、せキュア数字フィールドを使ってください。

**数字入力ビューの目的を明確に説明する。** タイトルやプロンプトを使って、数字の入力を必要とする理由を説明します。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/digit-entry-views#Platform-considerations)

 _iOS、iPadOS、macOS、visionOS、watchOSには対応していません。_

## [リソース](/jp/design/human-interface-guidelines/digit-entry-views#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/digit-entry-views#Related)

[仮想キーボード](/jp/design/human-interface-guidelines/virtual-keyboards)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/digit-entry-views#Developer-documentation)

[`TVDigitEntryViewController`](/documentation/TVUIKit/TVDigitEntryViewController) — TVUIKit

# カラーウェル

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/color-wells

# カラーウェル

カラーウェルで、テキスト、図形、ガイドなどの画面に表示される要素の色を調整できます。

![図案化された拡張ボタンから下に広がるカラー選択のポップオーバー。画像は6色のオリジナルAppleロゴをイメージさせる赤色になっています。](https://docs-assets.developer.apple.com/published/1721d57437b0d3a8392738b0439e5614/components-color-well-intro%402x.png)

ユーザがカラーウェルをタップまたはクリックすると、カラーピッカーが表示されます。ここで、システムが提供するカラーピッカーを用いても、カスタムのインターフェイスをデザインしてもかまいません。

## [ベストプラクティス](/jp/design/human-interface-guidelines/color-wells#Best-practices)

**親しみやすさを重視するならシステムが提供するカラーピッカーを採用する。** ビルトインのカラーピッカーを使用すると、ユーザが保存したカラーのセットをどのアプリからでも利用できるので、一貫性の高い操作環境が実現します。システム定義のカラーピッカーは、iOS、iPadOS、macOSにまたがるアプリを開発する際にも、ユーザが慣れ親しんだ操作方法を提供できます。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/color-wells#Platform-considerations)

 _iOS、iPadOS、visionOSに追加の考慮事項はありません。tvOSとwatchOSには対応していません。_

### [macOS](/jp/design/human-interface-guidelines/color-wells#macOS)

ユーザがカラーウェルをクリックすると、カラーウェルがアクティブになって強調表示されます。次に、カラーピッカーが開いて色を選べるようになります。ユーザが色を選択すると、カラーウェルにその色が表示されます。

カラーウェルはドラッグ＆ドロップに対応しているので、1つのカラーウェルから別のカラーウェルに色をドラッグしたり、カラーピッカーからカラーウェルに色をドラッグしたりすることもできます。

## [リソース](/jp/design/human-interface-guidelines/color-wells#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/color-wells#Related)

[カラー](/jp/design/human-interface-guidelines/color)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/color-wells#Developer-documentation)

[`UIColorWell`](/documentation/UIKit/UIColorWell) — UIKit

[`UIColorPickerViewController`](/documentation/UIKit/UIColorPickerViewController) — UIKit

[`NSColorWell`](/documentation/AppKit/NSColorWell) — AppKit

[カラーのプログラミングのトピック](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/DrawColor/DrawColor.html)

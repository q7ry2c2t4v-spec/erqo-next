# ボックス

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/boxes

# ボックス

ボックスは、論理的に関連のある情報やコンポーネントを視覚的にまとめるためのコンポーネントです。

![角丸四角形の中にある図案化されたインターフェイス要素のグループ。画像は全体が、6色のオリジナルAppleロゴを連想させる赤色になっています。](https://docs-assets.developer.apple.com/published/f69093edaa3123df5217308ef50925da/components-box-intro%402x.png)

ボックスには、そのコンテンツをインターフェイスの残りの部分と区別するためのボーダーやバックグラウンドカラーがデフォルトで設定されています。ボックスにはタイトルも含めることができます。

## [ベストプラクティス](/jp/design/human-interface-guidelines/boxes#Best-practices)

**ボックスは、それを含むビューに対してなるべく小さくする。** ボックスのサイズがそれを含むウインドウや画面のサイズに近いと、コンテンツのまとまりを区別する効果が減少する上に、ほかのコンテンツを圧迫してしまう場合もあります。

**ボックス内でさらにグループ化を行う場合は余白や配置を工夫する。** ボックスのボーダーは非常に目立つ視覚要素であるため、ボックスの中にボックスを表示すると、入り組んだ圧迫感のあるインターフェイスになるおそれがあります。

## [コンテンツ](/jp/design/human-interface-guidelines/boxes#Content)

**タイトルによってボックスのコンテンツを容易に識別できる場合は、簡潔なタイトルを含める。** ボックスの見た目だけで、コンテンツが1つのグループになっていることが分かりますが、その関係について詳しい情報を提供することが望ましい場合もあります。タイトルは、VoiceOverユーザがボックス内のコンテンツを予測する助けにもなります。

**タイトルが必要な場合は、簡潔な表現にする。** センテンススタイルの大文字化を使用します（英語の場合）。句読点は使用しないでください。ただし、設定パネルでボックスを使用する場合は、タイトルにコロンを付加します。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/boxes#Platform-considerations)

 _visionOSに追加の考慮事項はありません。tvOSとwatchOSには対応していません。_

### [iOS/iPadOS](/jp/design/human-interface-guidelines/boxes#iOS-iPadOS)

iOSとiPadOSのボックスには、デフォルトで2次および3次のバックグラウンド[カラー](https://developer.apple.com/jp/design/human-interface-guidelines/color)が使用されます。

### [macOS](/jp/design/human-interface-guidelines/boxes#macOS)

macOSのボックスのタイトルは、デフォルトでボックスの上に表示されます。

## [リソース](/jp/design/human-interface-guidelines/boxes#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/boxes#Related)

[レイアウト](/jp/design/human-interface-guidelines/layout)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/boxes#Developer-documentation)

[`GroupBox`](/documentation/SwiftUI/GroupBox) — SwiftUI

[`NSBox`](/documentation/AppKit/NSBox) — AppKit

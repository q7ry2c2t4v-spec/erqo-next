# オーナメント

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/ornaments

# オーナメント

visionOSのオーナメントには、ウインドウに関連するコントロールや情報を提示できます。これにより、ウインドウにコンテンツを詰め込んだり、コンテンツが見づらくなったりするのを避けることができます。

![ウインドウの下部に表示されている図案化されたオーナメント。デザインツールのキャンバスを思わせるグリッド上に表示されています。画像全体が、6色の初代Appleロゴの赤色を連想させる赤みを帯びています。](https://docs-assets.developer.apple.com/published/a9012c3e7b1c5d47a4788aefd7a5b48c/components-ornaments-intro%402x.png)

オーナメントは、関連するウインドウよりも少し手前にある、ウインドウに平行な平面に浮かびます。関連するウインドウが移動すると、オーナメントもウインドウとの位置関係を保ちながら移動します。ウインドウのコンテンツがスクロールしても、オーナメント内のコントロールや情報は影響を受けません。

オーナメントはウインドウの上下左右どのエッジにも配置でき、ボタン、セグメントコントロール、その他のビューなどのUIコンポーネントを含めることができます。システムは、[ツールバー](/jp/design/human-interface-guidelines/toolbars)、[タブバー](/jp/design/human-interface-guidelines/tab-bars)、ビデオ再生コントロールなどのコンポーネントの作成および管理にオーナメントを使用します。デベロッパは、オーナメントを使ってカスタムコンポーネントを作成できます。

## [ベストプラクティス](/jp/design/human-interface-guidelines/ornaments#Best-practices)

**よく使うコントロールや情報を、ウインドウの邪魔にならない一貫した位置に提示するときにはオーナメントの使用を検討する。** オーナメントは常に関連ウインドウの近くにあるので、ユーザが見失うことはありません。例えば、「ミュージック」ではオーナメントを使って「再生中」コントロールを提示するので、それらのコントロールが、ユーザが予想できる見つけやすい場所に常に表示されます。

**基本的にオーナメントは常時表示する。** 例えば、ビデオを視聴する、写真を見るなど、ユーザがウインドウのコンテンツのイマーシブな空間に入るときは、オーナメントを非表示にするのが自然ですが、基本的にはオーナメントのコントロールにいつでもアクセスできる方が便利です。

**複数のオーナメントを表示する必要がある場合は、ウインドウの全体的な見た目のバランスを重視する。** オーナメントでは重要なアクションを手前に表示できますが、それによってコンテンツが見づらくなることもあります。必要に応じてオーナメントの総数を減らすことを検討し、ウインドウの視覚的な重みが高くなってアプリが乱雑にならないようにしてください。オーナメントを削除する場合は、その要素をメインウインドウに移動しましょう。

**オーナメントの幅が、関連ウインドウの幅を超えないようにする。** ウインドウよりもオーナメントの幅の方が広いと、ウインドウの横に表示されるタブバーなどの縦型コンテンツに干渉してしまう可能性があります。

**オーナメントにはなるべく枠線なしのボタンを使う。** オーナメントのデフォルトのバックグラウンドは[ガラス](/jp/design/human-interface-guidelines/materials#visionOS)です。そのため、ボタンをバックグラウンド上に直接配置する場合には、枠線を表示する必要はないかもしれません。ユーザがオーナメント内の枠線なしボタンを見つめると、そのボタンに自動的にホバーエフェクトが適用されます（ガイダンスは[視線](/jp/design/human-interface-guidelines/eyes)を参照してください）。

**カスタムコンポーネントを作成する必要がない限り、システムが提供するツールバーとタブバーを使う。** visionOSでは、ツールバーとタブバーがオーナメントとして自動的に表示されます。オーナメントでこれらのコンポーネントを自作する必要はありません。デベロッパ向けのガイダンスは、[ツールバー](/documentation/SwiftUI/Toolbars)および[`TabView`](/documentation/SwiftUI/TabView)を参照してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/ornaments#Platform-considerations)

 _iOS、iPadOS、macOS、tvOS、watchOSには対応していません。_

## [リソース](/jp/design/human-interface-guidelines/ornaments#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/ornaments#Related)

[レイアウト](/jp/design/human-interface-guidelines/layout)

[ツールバー](/jp/design/human-interface-guidelines/toolbars)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/ornaments#Developer-documentation)

[`ornament(visibility:attachmentAnchor:contentAlignment:ornament:)`](/documentation/SwiftUI/View/ornament\(visibility:attachmentAnchor:contentAlignment:ornament:\)) — SwiftUI

#### [ビデオ](/jp/design/human-interface-guidelines/ornaments#Videos)

[](https://developer.apple.com/videos/play/wwdc2023/10076)

## [変更履歴](/jp/design/human-interface-guidelines/ornaments#Change-log)

日付| 変更内容  
---|---  
2024年2月02日| 複数のオーナメントの使用に関するガイダンスを追加。  
2023年12月05日| オーナメントを使用した補助項目の表示についての情報を削除。  
2023年6月21日| 新規ページ。

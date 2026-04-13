# マテリアル

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/materials

# マテリアル

マテリアルとは、フォアグラウンド要素とバックグラウンド要素の間に奥行きや層感、階層を生み出す視覚効果のことです。

![重なっている四角形のスケッチ。透明度を使用しての背景のコンテンツの手引きを示しています。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせる黄色になっています](https://docs-assets.developer.apple.com/published/caa98013c2d476fb4164cd49e7ea8ae1/foundations-materials-intro%402x.png)

マテリアルは、テキストやコントロールなどのフォアグラウンド要素と、コンテンツや単色などのバックグラウンド要素を視覚的に分離するのに役立ちます。バックグラウンドからフォアグラウンドにカラーが透けることで、マテリアルの視覚的階層を確立し、ユーザは自分の今いる場所を把握しやすくなります。

Appleプラットフォームには、2種類のマテリアルが用意されています: Liquid Glassと標準マテリアルです。[Liquid Glass](/jp/design/human-interface-guidelines/materials#Liquid-Glass)は、Appleプラットフォーム全体のデザイン言語を統一する動的なマテリアルであり、下のコンテンツを隠すことなくコントロールやナビゲーションを提示できます。Liquid Glassとは対照的に、[標準マテリアル](/jp/design/human-interface-guidelines/materials#Standard-materials)はコンテンツレイヤー内で視覚的に見分けやすくするのに役立ちます。

## [Liquid Glass](/jp/design/human-interface-guidelines/materials#Liquid-Glass)

Liquid Glassは、タブバーやサイドバーなど、コンテンツレイヤーの上に浮ぶコントロールやナビゲーション要素のための明確な機能レイヤーを形成し、機能要素とコンテンツの間に明確な視覚的階層を確立します。Liquid Glassでは、これらの要素の下からコンテンツをスクロールしたり覗いたりすることができます。そのため、インターフェイスにダイナミックさと奥行きが加わる一方で、コントロールやナビゲーションの可読性は維持されます。

**Liquid Glassをコンテンツレイヤーでは使用しない。** Liquid Glassは、インタラクティブ要素とコンテンツを明確に区別する場合に最も効果的です。Liquid Glassをコンテンツレイヤーで使用すると、不必要に複雑になり、視覚的階層が混乱するおそれがあります。そうではなく、アプリの背景など、コンテンツレイヤーの要素には[標準マテリアル](/jp/design/human-interface-guidelines/materials#Standard-materials)を使用してください。ただし、[スライダ](/jp/design/human-interface-guidelines/sliders)や[トグル](/jp/design/human-interface-guidelines/toggles)など、一時的なインタラクティブ要素を含むコンテンツレイヤーのコントロールは例外です。この場合は、ユーザが要素をアクティブにすると、その要素はLiquid Glassの見た目になり、インタラクティブ性が強調されます。

**Liquid Glassエフェクトの使用を控えめにする。** システムフレームワークの標準コンポーネントでは、このマテリアルの見た目と動作を自動的に取得します。カスタムコントロールにLiquid Glassエフェクトを適用する場合は、控えめに使用してください。Liquid Glassは、その下にあるコンテンツに注目してもらうことを目的としているため、このマテリアルを複数のカスタムコントロールで過度に使用すると、コンテンツから気を逸らしてしまい、ユーザ体験が低下する可能性があります。これらのエフェクトは、アプリの中で最も重要な機能要素に限定して使用してください。デベロッパ向けのガイダンスは、[カスタムビューへのLiquid Glassの適用](/documentation/SwiftUI/Applying-Liquid-Glass-to-custom-views)を参照してください。

**視覚的に豊かなバックグラウンドの上に表示するコンポーネントには透明性のあるLiquid Glassのみを使用する。** Liquid Glassには、カスタムコンポーネントの構築や一部のシステムコンポーネントのスタイルの適用の際に使用できる[`regular`](/documentation/SwiftUI/Glass/regular)および[`clear`](/documentation/SwiftUI/Glass/clear)という2つのバリアントがあります。これらのバリアントの見た目は、一部のシステム設定に応じて変わる場合があります。例えば、ユーザがデバイスの表示設定で使用するLiquid Glassの外観を選択したり、インターフェイスの透明度を下げたりコントラストを上げたりするアクセシビリティ設定をオンにしたりした場合に、これらのバリアントの見た目が変わります。

 _regular_ バリアントは、テキストやその他のフォアグラウンド要素の視認性を維持するため、ぼかしをかけ、バックグラウンドコンテンツの明度を調整します。スクロールエッジエフェクトは、ぼかしをかけてバックグラウンドコンテンツの不透明度を低下させることで、視認性をさらに高めます。ほとんどのシステムコンポーネントではこのバリアントが使用されます。regularバリアントは、バックグラウンドコンテンツで視認性の問題が生じる可能性がある場合や、コンポーネントにアラート、サイドバー、ポップオーバーなどのテキストが大量に含まれている場合に使用します。

![Liquid Glassのregularバリアントの視覚的な例。その下の背景が暗い色のときは、より暗く表示されます。](https://docs-assets.developer.apple.com/published/91bd48556358ab3deb6720c982aa8503/materials-ios-liquid-glass-regular-on-dark%402x.png)暗い背景の上

![Liquid Glassのregularバリアントの視覚的な例。その下の背景が明るい色のときは、より明るく表示されます。](https://docs-assets.developer.apple.com/published/07aee30876315c8b2985a59a3ac1df31/materials-ios-liquid-glass-regular-on-light%402x.png)明るい背景の上

 _clear_ バリアントは透明度が高く、下にあるコンテンツの視認性を優先し、視覚的に豊かなバックグラウンド要素を目立たせる場合に最適です。このバリアントは、よりイマーシブなコンテンツ体験を生み出すために、写真やビデオなどのメディアの背景の上に浮かんでいるコンポーネントに使用します。

![Liquid Glassのclearバリアントの視覚的な例。その下の背景の視覚的な細部が透けて見えるようにしています。](https://docs-assets.developer.apple.com/published/fe0cd9171626ada19f9ea7343f60a426/materials-ios-liquid-glass-clear%402x.png)

最適なコントラストと視認性を得るためには、clearのLiquid Glassでコンポーネントの下にディミングレイヤーを加えるかどうかを判断します:

  * 下にあるコンテンツが明るい場合は、不透明度が35%の暗いディミングレイヤーを加えることを検討してください。デベロッパ向けのガイダンスは、[`clear`](/documentation/SwiftUI/Glass/clear)を参照してください。

  * 下にあるコンテンツが十分に暗い場合や、独自のディミングレイヤーを備えたAVKitの標準のメディア再生コントロールを使用している場合、ディミングレイヤーを適用する必要はありません。

カラーの使用についてのガイダンスは、[Liquid Glassカラー](/jp/design/human-interface-guidelines/color#Liquid-Glass-color)を参照してください。

## [標準マテリアル](/jp/design/human-interface-guidelines/materials#Standard-materials)

標準のマテリアルやエフェクト（[ぼかし](/documentation/UIKit/UIBlurEffect)、[バイブランス](/documentation/UIKit/UIVibrancyEffect)、[ブレンディングモード](/documentation/AppKit/NSVisualEffectView/BlendingMode-swift.enum)など）を使用して、Liquid Glassの下にあるコンテンツの構造感を表現します。

**マテリアルやエフェクトは、それが持つ意味や推奨される使い方に基づいて選択する。** インターフェイスに反映される見た目のカラーでマテリアルやエフェクトを選ぶことは避けてください。見た目や動作はシステム設定によって変更されることがあります。そうではなく、個々の用途に適したマテリアルやバイブランススタイルを選んでください。

**可読性を確保するためにバイブラントカラーはマテリアルの前面に使用する。** システムで定義されたバイブラントカラーを使う場合は、さまざまな状況でカラーが暗すぎる、明るすぎる、鮮やかすぎる、コントラストが低いといったことを気にする必要はありません。選択したマテリアルにかかわらず、マテリアルの前面ではバイブラントカラーを使います。ガイダンスは[システムコントロール](/jp/design/human-interface-guidelines/color#System-colors)を参照してください。

![共有ボタンの図。半透明な背景マテリアルとシンボルが表示されています。シンボルにはsystemGray3カラーが使われ、背景マテリアルと区別しにくくなっています。](https://docs-assets.developer.apple.com/published/8a395765f911660a5e16b3bdb30ddd2f/materials-legibility-non-vibrant-label%402x.png)マテリアルと`systemGray3`ラベルのコントラストが十分でない

![丸に囲まれたバツ印が不適切な使い方であることを示しています](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![共有ボタンの図。半透明な背景マテリアルとシンボルが表示されています。シンボルにはバイブラントカラーが使われ、背景マテリアルとはっきり区別できます。](https://docs-assets.developer.apple.com/published/7495cfbce7d79a1f5635ea2a729dfc24/materials-legibility-primary-label%402x.png)マテリアルとバイブラントカラーラベルのコントラストが十分です

![丸に囲まれたチェックマークが適切な使い方であることを示しています](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

**マテリアルをぼかしやバイブランスのエフェクトと組み合わせる場合は、コントラストや視覚的な分離を考慮する。** 例えば、次のような点を考慮します。

  * 厚いマテリアルほど不透明度が高くなり、細かい特徴を持つテキストなどの要素のコントラストを高めることができます。

  * 薄いマテリアルほど透明度が高くなり、後ろにあるコンテンツがうっすらと見えるので、ユーザは全体の状況を把握しやすくなります。

デベロッパ向けのガイダンスは、[`Material`](/documentation/SwiftUI/Material)を参照してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/materials#Platform-considerations)

### [iOS/iPadOS](/jp/design/human-interface-guidelines/materials#iOS-iPadOS)

iOSとiPadOSでは、Liquid Glassだけでなく、視覚的な区分の作成のためにコンテンツレイヤーで使用できるultra-thin、thin、regular（デフォルト）、thickという4つの標準マテリアルも、引き続き提供します。

![iOSとiPadOSのultraThinマテリアルの図。カラフルな背景の上にあります。マテリアルが背景と重なる部分は、背景カラーの拡散グラデーションになっています。](https://docs-assets.developer.apple.com/published/2ad0598be0bf67fb23e479f102e16b59/materials-ios-material-background-ultrathin%402x.png)`ultraThin`

![iOSとiPadOSのthinマテリアルの図。カラフルな背景の上にあります。マテリアルが背景と重なる部分は、背景カラーのわずかに暗い拡散グラデーションになっています。](https://docs-assets.developer.apple.com/published/d298de701d98a146b1436fdf21d0b7ce/materials-ios-material-background-thin%402x.png)`thin`

![iOSとiPadOSのregularマテリアルの図。カラフルな背景の上にあります。マテリアルが背景と重なる部分は、背景カラーの暗い拡散グラデーションになっています。](https://docs-assets.developer.apple.com/published/93a77ac4cfc0786664563a0691498b05/materials-ios-material-background-regular%402x.png)`regular`

![iOSとiPadOSのthickマテリアルの図。カラフルな背景の上にあります。マテリアルが背景と重なる部分は、背景カラーの暗い控えめなグラデーションになっています。](https://docs-assets.developer.apple.com/published/2532ddf965d0effa12f528ac10b5a0b3/materials-ios-material-background-thick%402x.png)`thick`

iOSとiPadOSでは、ラベル、塗りつぶし、区切り向けに各マテリアルで利用できるように特別に設計されたバイブラントなカラーも定義されています。ラベルと塗りつぶしにはどちらも複数のレベルのバイブランスがありますが、区切りには1つのレベルしかありません。レベルの名前は、要素と背景との間のコントラストの高さを相対的に表しています。コントラストが最も高いのがデフォルトのレベルで、最も低いのは4段階目（存在する場合）です。

4段階目のquaternaryLabelを除き、あらゆるマテリアルのラベルには次のバイブランス値を使用できます。一般的に、[`thin`](/documentation/SwiftUI/Material/thin)および[`ultraThin`](/documentation/SwiftUI/Material/ultraThin)の上では、コントラストが低すぎるため、4段階目の使用は避けてください。

  * [`UIVibrancyEffectStyle.label`](/documentation/UIKit/UIVibrancyEffectStyle/label) （デフォルト）

  * [`UIVibrancyEffectStyle.secondaryLabel`](/documentation/UIKit/UIVibrancyEffectStyle/secondaryLabel)

  * [`UIVibrancyEffectStyle.tertiaryLabel`](/documentation/UIKit/UIVibrancyEffectStyle/tertiaryLabel)

  * [`UIVibrancyEffectStyle.quaternaryLabel`](/documentation/UIKit/UIVibrancyEffectStyle/quaternaryLabel)

すべてのマテリアルで、塗りつぶしに次のバイブランス値を使用できます。

  * [`UIVibrancyEffectStyle.fill`](/documentation/UIKit/UIVibrancyEffectStyle/fill) （デフォルト）

  * [`UIVibrancyEffectStyle.secondaryFill`](/documentation/UIKit/UIVibrancyEffectStyle/secondaryFill)

  * [`UIVibrancyEffectStyle.tertiaryFill`](/documentation/UIKit/UIVibrancyEffectStyle/tertiaryFill)

[separator](/documentation/UIKit/UIVibrancyEffectStyle/separator)には、デフォルトのバイブランス値が1つだけ提供されます。これはどのマテリアルにもうまくなじみます。

### [macOS](/jp/design/human-interface-guidelines/materials#macOS)

macOSには、目的が異なる複数の標準マテリアルと、すべての[システムカラー](/jp/design/human-interface-guidelines/color#Specifications)のバイブラントなバージョンがあります。デベロッパ向けのガイダンスは、[`NSVisualEffectView.Material`](/documentation/AppKit/NSVisualEffectView/Material-swift.enum)を参照してください。

**カスタムのビューやコントロールでいつバイブランスを許可するかを選択する。** 構成やシステム設定によっては、どのような背景に対してもフォアグラウンドのコンテンツが目立つように、システムのビューやコントロールにバイブランスが使われることがあります。バイブランスが適用されるさまざまな状況でインターフェイスをテストし、どのような場合にバイブランスによって見た目が向上し、伝達効果が高まるかを確認してください。

**インターフェイスデザインを向上させるバックグラウンドブレンディングモードを選択する。** macOSでは、バックグラウンドコンテンツをブレンドするモードとして、ウインドウ後方とウインドウ内の2つが定義されています。デベロッパ向けのガイダンスは、[`NSVisualEffectView.BlendingMode`](/documentation/AppKit/NSVisualEffectView/BlendingMode-swift.enum)を参照してください。

### [tvOS](/jp/design/human-interface-guidelines/materials#tvOS)

tvOSでは、Liquid Glassは、ナビゲーション要素とトップシェルフやコントロールセンターなどのシステム体験の全体で表示されます。画像ビューやボタンのような特定のインターフェイス要素では、フォーカスが当たったときにLiquid Glassを使用します。

![tvOSで実行されているDestination Videoアプリのスクリーンショット。アプリの画面に「BOT-anistアドベンチャー」というビデオについての詳細が表示されています。背景は、ビデオのワンシーンにいる主人公のカラフルな画像です。背景の上に浮かんでいるインターフェイス要素では、背景カラーが透けて見えるようにし、よりイマーシブなメディア体験を生み出すために、Liquid Glassの外観を採用しています。](https://docs-assets.developer.apple.com/published/fd83bb7f079cac7b59cb692d8e1c6707/materials-tvos-media-player%402x.png)

tvOSでは、Liquid Glassだけでなく、コンテンツレイヤーの構造の定義に使用できる標準マテリアルも、引き続き提供します。標準マテリアルの線の太さは、下にあるコンテンツをどの程度目立つように透けて見せるかに影響します。例えば、標準マテリアルを次のように使うことを検討してください:

マテリアル| 推奨用途  
---|---  
[`ultraThin`](/documentation/SwiftUI/Material/ultraThin)| ライトなカラースキームが必要なフルスクリーン表示  
[`thin`](/documentation/SwiftUI/Material/thin)| 画面上の一部のコンテンツを隠すオーバーレイ表示で、ライトなカラースキームが必要なもの  
[`regular`](/documentation/SwiftUI/Material/regular)| 画面上の一部のコンテンツを隠すオーバーレイ表示  
[`thick`](/documentation/SwiftUI/Material/thick)| 画面上の一部のコンテンツを隠すオーバーレイ表示で、ダークなカラースキームが必要なもの  
  
### [visionOS](/jp/design/human-interface-guidelines/materials#visionOS)

visionOSのウインドウには、基本的にシステム定義のマテリアルである _ガラス_ が使用されます（このマテリアルにモディファイアを追加することはできません）。このガラスによって、ユーザの周囲の光や照明、現在の環境、仮想コンテンツ、オブジェクト、物体が透けて見えることで、ユーザは現実世界に留まっている感覚を得ることができます。ガラスはバックグラウンドのカラー情報を制限するアダプティブなマテリアルなので、ウインドウ上のアプリコンテンツのコントラストは常に保たれ、ウインドウの明るさはユーザの物理的な環境や仮想コンテンツに応じて変化します。

以下のカスタムコントロールを使用できます 

このビデオコンテンツの説明: visionOSのミュージックアプリウインドウの録画。ウインドウには、見る角度や光の変化に応じて変化するガラスマテリアルが使用されています。 

再生 

備考

visionOSには、明確なダークモード設定はありません。その代わりに、ガラスがオブジェクトとその背後にあるカラーの輝度に合わせて自動的に変化するようになっています。

**ウインドウでは不透明なカラーよりも半透明が望ましい。** 不透明な部分があるとユーザの視界が妨げられ、ユーザが息苦しく感じたり、周囲にある仮想オブジェクトや現実世界のものを認識しにくくなったりします。

![visionOSの視野の図。ウインドウが中央にあります。ウインドウの背景は不透明で、周囲は見えません。](https://docs-assets.developer.apple.com/published/137ceb38a96227aa8a9d2021ee82a8e2/materials-visionos-opaque-window-incorrect%402x.png)

![丸に囲まれたバツ印が不適切な使い方であることを示しています](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![visionOSの視野の図。ウインドウが中央にあります。ウインドウの背景は半透明のマテリアルで、周囲が透過して見えます。](https://docs-assets.developer.apple.com/published/3f23b3476f6cf8cc77fdcb91a0c15063/materials-visionos-glass-window%402x.png)

![丸に囲まれたチェックマークが適切な使い方であることを示しています](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

**必要な場合は、アプリ内の要素を視覚的に分離するマテリアルやインタラクティブ性を示すマテリアルを選択する。** カスタムコンポーネントを作成する必要がある場合は、システムマテリアルを指定することをおすすめします。以下の例を参考にしてください。

  * [`thin`](/documentation/SwiftUI/Material/thin)マテリアルを使用すると、ボタンや選択中の項目など、インタラクティブな要素を目立たせることができます。

  * [`regular`](/documentation/SwiftUI/Material/regular)マテリアルでは、サイドバーやグループ化されたテーブルビューなど、アプリのセクションを視覚的に区切ることができます。

  * [`thick`](/documentation/SwiftUI/Material/thick)マテリアルを使用すると、`regular`の背景を使用している領域の上にあるときに、見分けやすくなる暗い要素を作成できます。

![visionOSの視野の図。ウインドウが中央にあります。ウインドウは左側のサイドバーと右側のコンテンツ領域で構成されており、上にテキストフィールドが、右下隅にボタンがあります。サイドバーにはregularマテリアルが使われていますが、テキストフィールドにはthickマテリアルが、ボタンにはthinマテリアルが使われています。](https://docs-assets.developer.apple.com/published/c3577aa1e00689431e49973173a151f9/visionos-materials-window-example%402x.png)

マテリアルに重ねて表示されたときにフォアグラウンドのコンテンツの読みやすさが損なわれないように、visionOSでは、テキスト、シンボル、塗りつぶしにバイブランスが適用されます。バイブランスは、背後にある仮想環境と物理環境の両方の光とカラーを透過させることで、奥行き感を高めます。

visionOSでは、テキスト、シンボル、塗りつぶしの階層を伝えるためのバイブランス値が3つ定義されています。

  * 標準テキストには[`UIVibrancyEffectStyle.label`](/documentation/UIKit/UIVibrancyEffectStyle/label)を使用する。

  * 脚注や字幕などの説明テキストには[`UIVibrancyEffectStyle.secondaryLabel`](/documentation/UIKit/UIVibrancyEffectStyle/secondaryLabel)を使用する。

  * アクティブでない要素には[`UIVibrancyEffectStyle.tertiaryLabel`](/documentation/UIKit/UIVibrancyEffectStyle/tertiaryLabel)を使用する（テキストの読みやすさを確保する必要がない場合のみ）。

![共有ボタンの図。半透明な背景マテリアルとシンボルが表示されています。シンボルにはデフォルトのバイブラントラベルカラーが使われ、背景マテリアルとのコントラストが非常に高くなっています。](https://docs-assets.developer.apple.com/published/8f850521ecc2e3953e8e693fe7b4887b/materials-visionos-label-vibrant-primary%402x.png)`label`

![共有ボタンの図。半透明な背景マテリアルとシンボルが表示されています。シンボルには第2バイブラントラベルカラーが使われ、背景マテリアルとのコントラストが高くなっています。](https://docs-assets.developer.apple.com/published/876503f2b2b5fd1783e359128ffd2482/materials-visionos-label-vibrant-secondary%402x.png)`secondaryLabel`

![共有ボタンの図。半透明な背景マテリアルとシンボルが表示されています。シンボルには第3バイブラントラベルカラーが使われ、背景マテリアルとのコントラストが控えめになっています。](https://docs-assets.developer.apple.com/published/b3b80e5f23b286f6c7897780676e6dfe/materials-visionos-label-vibrant-tertiary%402x.png)`tertiaryLabel`

### [watchOS](/jp/design/human-interface-guidelines/materials#watchOS)

**マテリアルを使って、フルスクリーンのモーダルビューのコンテキストを示す。** watchOSでは、フルスクリーンのモーダルビューが通常の表示です。マテリアルのレイヤーによってコントラストを生み出すと、アプリ内でユーザに正しい手順を示したり、コントロールやシステム要素をほかのコンテンツから明確に区別したりするのに役立ちます。モーダルシート用にデフォルトで提供されているマテリアルの背景を削除したり置き換えたりしないでください。

![watchOSのモーダルビューの図。サンプルのタイトル、説明テキスト、および1つのアクションボタンがあります。透明なマテリアルのモーダルが完全に画面を覆っており、ボタンには透明度が高いマテリアルが使われ、ラベルテキストはバイブラントです。](https://docs-assets.developer.apple.com/published/2b798f1f9b1974e5ca9bb8b19bd32431/watchos-modal-view-material-background%402x.png)

## [リソース](/jp/design/human-interface-guidelines/materials#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/materials#Related)

[カラー](/jp/design/human-interface-guidelines/color)

[アクセシビリティ](/jp/design/human-interface-guidelines/accessibility)

[ダークモード](/jp/design/human-interface-guidelines/dark-mode)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/materials#Developer-documentation)

[Liquid Glassの採用](/documentation/TechnologyOverviews/adopting-liquid-glass)

[`glassEffect(_:in:)`](/documentation/SwiftUI/View/glassEffect\(_:in:\)) — SwiftUI

[`Material`](/documentation/SwiftUI/Material) — SwiftUI

[`UIVisualEffectView`](/documentation/UIKit/UIVisualEffectView) — UIKit

[`NSVisualEffectView`](/documentation/AppKit/NSVisualEffectView) — AppKit

#### [ビデオ](/jp/design/human-interface-guidelines/materials#Videos)

[](https://developer.apple.com/videos/play/wwdc2025/219)

[](https://developer.apple.com/videos/play/wwdc2025/356)

## [変更履歴](/jp/design/human-interface-guidelines/materials#Change-log)

日付| 変更内容  
---|---  
2025年9月09日| Liquid Glassに関するガイダンスを更新。  
2025年6月09日| Liquid Glassに関するガイダンスを追加。  
2024年8月06日| プラットフォーム固有の画像を追加。  
2023年12月05日| さまざまなマテリアルタイプの説明を更新し、バイブランスとマテリアルの透明度に関する用語を明確化。  
2023年6月21日| visionOSのガイダンスを追加するために更新。  
2023年6月05日| watchOSのアプリでコンテキストや手順を示すためのマテリアルの使用に関するガイドを追加。

# カラー

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/color

2025年12月16日

Liquid Glassに関するガイダンスを更新。 

# カラー

カラーを適切に使用することは、コミュニケーションの強化、ブランドイメージの喚起、視覚的連続性の提供、状態やフィードバックの伝達、情報の理解につながります。

![絵の具のパレットのスケッチ。カラーの使用を示しています。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせる黄色になっています](https://docs-assets.developer.apple.com/published/25a1b5cc9571b7a69c3c31e932a259cb/foundations-color-intro%402x.png)

システムでは、さまざまな背景や外観モードに適したカラーが定義されています。こういったカラーは、バイブランスやアクセシビリティの設定に自動的に適応します。システムカラーを使用すれば、デバイスでのアプリの使用感を自然なものと感じてもらうことができます。

また、カスタムカラーを使用してアプリやゲームの視覚的体験を高めたり、独自の個性を表現したりすることもできます。以下のガイドでは、システムで定義されたカラーを使うか、カスタムカラーを使うかによらず、ユーザ体験の向上に役立つカラーの使い方を説明します。

## [ベストプラクティス](/jp/design/human-interface-guidelines/color#Best-practices)

**同じカラーを別の意味に使わない。** インターフェイス全体でカラーの使い方を一貫させます。状態や操作の可否といった情報を伝達するためにカラーを使う場合は、特にこの点に注意してください。例えば、枠線なしのボタンが操作可能であることを示すためにブランドカラーを使用する場合、操作不可能なテキストを同じ色または似た色で図案化すると、混乱を招きます。

**コンテキストがライト、ダーク、高いコントラストのいずれでも、アプリのすべてのカラーが適切に表示されることを確認する。** iOS、iPadOS、macOS、およびtvOSでは、ライトと[ダーク](/jp/design/human-interface-guidelines/dark-mode)の両方の見た目の設定が用意されています。[システムカラー](/jp/design/human-interface-guidelines/color#System-colors)は、システムの見た目に応じて微妙に変化し、テキスト、シンボル、およびその他の要素のカラーの違いとコントラストが適切になるように調整されます。「コントラストを上げる」設定をオンにすると、色の違いがはるかに明確になります。可能な場合はシステムカラーを使ってください。システムカラーではこれらすべてのコンテキストについてバリエーションがあらかじめ定義されています。カスタムカラーを定義する場合は、明るいバリアントと暗いバリアント、および各バリアントのコントラストを上げたオプション（視覚的に非常に見分けやすいもの）を用意してください。アプリに見た目のモードを1つしか用意しない場合でも、ライトとダーク両方のカラーを提供して、それらのコンテキストでLiquid Glassが適応できるようにしてください。

![iOSのメモアプリのスクリーンショット。システムのライトの見た目とデフォルトのコントラストが適用されています。メモアプリで「メモ」というテキストが含まれたメモが開いています。テキストが選択され、選択項目の黄色いハイライトとテキスト編集メニューが表示されています。右上隅には「完了」ボタンが表示されています。ボタンのLiquid Glassの背景は黄色で、チェックマークが表示されているラベルは白です。黄色の陰影はバイブラントです。](https://docs-assets.developer.apple.com/published/7b4a0afeed9131b9155ae1573e94336b/color-context-light-mode%402x.png)

デフォルト（ライト）

![iOSのメモアプリのスクリーンショット。システムのライトの見た目と高いコントラストが適用されています。メモアプリで「メモ」というテキストが含まれたメモが開いています。テキストが選択され、選択項目の黄色いハイライトとテキスト編集メニューが表示されています。右上隅には「完了」ボタンが表示されています。ボタンのLiquid Glassの背景は黄色で、チェックマークが表示されているラベルは黒です。黄色の濃淡は暗めで、メモの白い背景に対してコントラストがあり、見分けが付きやすくなっています。](https://docs-assets.developer.apple.com/published/2bc54d7dafde4288419062994c389cda/color-context-light-mode-high-contrast%402x.png)

コントラストを上げる（ライト）

![iOSのメモアプリのスクリーンショット。システムのダークの見た目とデフォルトのコントラストが適用されています。メモアプリで「メモ」というテキストが含まれたメモが開いています。テキストが選択され、選択項目の黄色いハイライトとテキスト編集メニューが表示されています。右上隅には「完了」ボタンが表示されています。ボタンのLiquid Glassの背景は黄色で、チェックマークが表示されているラベルは白です。](https://docs-assets.developer.apple.com/published/8d00a426cfb11893202485980ac1aa61/color-context-dark-mode%402x.png)

デフォルト（ダーク）

![iOSのメモアプリのスクリーンショット。システムのダークの見た目と高いコントラストが適用されています。メモアプリで「メモ」というテキストが含まれたメモが開いています。テキストが選択され、選択項目の黄色いハイライトとテキスト編集メニューが表示されています。右上隅には「完了」ボタンが表示されています。ボタンのLiquid Glassの背景は黄色で、チェックマークが表示されているラベルは黒です。](https://docs-assets.developer.apple.com/published/1df274f78bb4193045039c323916a576/color-context-dark-mode-high-contrast%402x.png)

コントラストを上げる（ダーク）

**さまざまな照明条件でアプリのカラースキームをテストする。** 晴れた日の屋外や薄暗い明かりのもとでアプリを表示すると違った色に見えることがあります。周囲が明るいと、色はより暗く、より落ち着いて見えます。暗い環境では、色は明るく、彩度が高く見えます。visionOSでは、ユーザの周囲にある壁や物体の色と光の反射の仕方によって、色の見え方が違ってくることがあります。大半のユースケースで最適に見えるようにアプリのカラーを調整してください。

**さまざまなデバイスでアプリをテストする。** 例えば、True Toneディスプレイ（一部のiPhone、iPad、Macで利用可能）では、環境光センサーを使用してディスプレイのホワイトポイントを現在の照明環境に合わせて自動調整します。読書、写真、ビデオ、ゲームを主目的とするアプリでは、ホワイトポイント適応スタイルを指定して、この効果を強めたり弱めたりすることができます（デベロッパ向けのガイダンスは、[`UIWhitePointAdaptivityStyle`](/documentation/BundleResources/Information-Property-List/UIWhitePointAdaptivityStyle)を参照してください）。tvOSアプリの場合は、さまざまなブランドのHDテレビや4Kテレビで、さまざまなディスプレイ設定をテストしてください。Macでは、「システム設定」＞「ディスプレイ」から、P3やStandard RGB（sRGB）などのさまざまなカラープロファイルを選んでアプリの見た目をテストすることもできます。ガイダンスは、[カラーマネジメント](/jp/design/human-interface-guidelines/color#Color-management)を参照してください。

**アートワークや透明度が周辺のカラーに与える影響を検討する。** アートワークが変化すると、視覚的連続性を維持し、インターフェイス要素のバランスを保つために、周辺のカラーを変えなければならなくなる場合もあります。例えば「マップ」では、マップモードではライトなカラースキームで表示されますが、航空写真モードではダークなカラースキームに切り替わります。ツールバーなどの半透明な要素の背後や、半透明な要素自体にカラーを適用したりすると、違って見えることもあります。

**アプリでユーザがカラーを選べるようにする場合、可能な限りシステムが提供するカラーコントロールを使用する。** 内蔵のカラーピッカーを使用すると、ユーザ体験が一貫したものとなるだけでなく、ユーザが保存したカラーのセットをどのアプリからでも使うことができます。デベロッパ向けのガイダンスは、[`ColorPicker`](/documentation/SwiftUI/ColorPicker)を参照してください。

## [インクルーシブなカラー](/jp/design/human-interface-guidelines/color#Inclusive-color)

**オブジェクトの区別、操作可否の提示、重要な情報の伝達をカラーだけで行わない。** カラーによって情報を伝えるときは、色覚や視覚に障がいがある人も理解できるように、別の方法でも同じ情報を伝えるようにしましょう。例えば、テキストラベルやグリフを使用するとオブジェクトや状態が識別できるようになります。

**アプリのコンテンツが識別しにくくなるようなカラーを使わない。** 例えば、コントラストが十分でないと、アイコンやテキストが背景に溶け込んでコンテンツが読みにくくなる場合があります。また、色覚に障がいがある人は、一部のカラーの組み合わせを区別できない場合があります。ガイダンスは[アクセシビリティ](/jp/design/human-interface-guidelines/accessibility)を参照してください。

**使用するカラーが国や文化によってどう認識されるかを考える。** 例えば、赤を危険と認識する文化も、肯定的な意味と認識する文化もあります。アプリで使用するカラーで意図したメッセージが伝わることを確認してください。

![英語の株価アプリの上昇トレンドを示す株価チャートの図。グラフの線は緑色で、選択した期間中に上昇している株価を示しています。](https://docs-assets.developer.apple.com/published/5969ae10a6eaca6879fb43df4f651e4d/color-inclusive-color-charts-english%402x.png)英語の株価アプリで緑色は肯定的なトレンドを示しています。

![中国語の株価アプリの上昇トレンドを示す株価チャートの図。グラフの線は赤色で、選択した期間中に上昇している株価を示しています。](https://docs-assets.developer.apple.com/published/e84b6e7089f1fb8f73712da462d66164/color-inclusive-color-charts-chinese%402x.png)中国語の株価アプリで赤色は肯定的なトレンドを示しています。

## [システムカラー](/jp/design/human-interface-guidelines/color#System-colors)

**アプリでシステムカラーの値をハードコードしない。** ドキュメントには、アプリデザインの参考のためにカラーの値が記載されていますが、実際のカラーの値は、さまざまな環境の変化に応じて、リリースごとに変動する場合があります。システムカラーを適用する場合は、[`Color`](/documentation/SwiftUI/Color)などのAPIを使用してください。

iOS、iPadOS、macOS、visionOSでは、一連の _ダイナミックシステムカラー_ も定義されています。ダイナミックシステムカラーは、標準UIコンポーネントのカラースキームに調和し、ライトとダークの両方のコンテキストに自動的に適応します。それぞれのダイナミックカラーは、見た目やカラーの値ではなく、目的に応じた意味で定義されています。例えば、さまざまな階層レベルに応じたビューの背景のためのカラーもあれば、ラベル、リンク、区切りなどのフォアグラウンドコンテンツのためのカラーもあります。

**ダイナミックシステムカラーの意味を再定義しない。** 今後、プラットフォームの外観が変化しても一貫した体験と最適なインターフェイスを維持できるように、ダイナミックシステムカラーは意図された通りに使用してください。例えば、[区切り](https://developer.apple.com/documentation/uikit/uicolor/separator)カラーをテキストカラーとして使用したり、[第2テキストラベル](https://developer.apple.com/documentation/uikit/uicolor/secondarylabel)のカラーを背景のカラーとして使用したりしないでください。

## [Liquid Glassカラー](/jp/design/human-interface-guidelines/color#Liquid-Glass-color)

デフォルトでは、[Liquid Glass](/jp/design/human-interface-guidelines/materials#Liquid-Glass)自体にカラーはなく、代わりにすぐ背後にあるコンテンツのカラーを反映します。一部のLiquid Glass要素にはカラーを適用して、カラーガラスやステンドグラスのような見た目にすることができます。これは主要な行動喚起などの特定のコントロールを強調するのに役立ち、目立つボタンのスタイルにシステムが採用している方法です。Liquid Glassコントロールのシンボルやテキストラベルもカラーを持つことができます。

![iOSの「完了」ボタンのスクリーンショット。ボタンは青いLiquid Glassの背景にチェックマークとして表示されています。](https://docs-assets.developer.apple.com/published/df4d0a0bca32edb16d7ff86e34d6fe2d/color-liquid-glass-overview-tinted%402x.png)プライマリアクションボタンのように、コントロールはLiquid Glassの背景にカラーを使用できます。

![iOSのタブバーのスクリーンショット。最初のタブが選択されています。選択されたタブバーの項目のシンボルとテキストラベルは青色です。](https://docs-assets.developer.apple.com/published/1386b32cc408c920f0a13857727f7b0a/color-liquid-glass-overview-color-over-tab-bar%402x.png)選択されたタブバーの項目のように、Liquid Glassに表示されるシンボルとテキストはカラーを持つことができます。

![カラフルな画像に重なっているiOSの「共有」ボタンのスクリーンショット。背景画像のカラーがボタンのLiquid Glassに染みこみ、カラーを変えています。](https://docs-assets.developer.apple.com/published/9cf610d972c97dee46b9e206525b2ae7/color-liquid-glass-overview-clear%402x.png)デフォルトでは、Liquid Glassは背後にあるコンテンツレイヤーのカラーを取り込みます。

ツールバーやタブバーなどの小さな要素では、システムは、その下にあるコンテンツに応じて、Liquid Glassを調整して明るい見た目と暗い見た目の間で切り替えることがあります。デフォルトでは、これらの要素のシンボルやテキストは、モノクロのカラースキームに従うため、下にあるコンテンツが明るい場合は暗くなり、暗い場合は明るくなります。Liquid Glassでは、サイドバーなどの大きな要素の不透明度は高くなるため、背景が複雑でも可読性を維持し、マテリアルの表面でよりリッチなコンテンツに対応します。

**Liquid Glassマテリアルおよびその上のシンボルやテキストには控えめにカラーを適用する。** カラーを適用する場合は、ステータスインジケータやプライマリアクションなど、強調することでメリットがある要素にのみ使用してください。プライマリアクションを強調するには、シンボルやテキストよりも背景にカラーを適用します。例えば、システムでは「完了」ボタンなどの目立つボタンの背景にアプリのアクセントカラーを適用することで、注意を引き、視認性を高めています。複数のコントロールの背景にカラーを追加しないでください。

![iPhoneアプリの上半分のスクリーンショット。複数のボタンがあるツールバーが表示されています。ツールバーのすべてのボタンは、Liquid Glassの背景として青のアクセントカラーを使用しています。](https://docs-assets.developer.apple.com/published/33b416322d9831eafe280631987928e7/colors-liquid-glass-usage-incorrect%402x.png)

![丸に囲まれたバツ印が不適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![iPhoneアプリの上半分のスクリーンショット。複数のボタンがあるツールバーが表示されています。ツールバーの「完了」ボタンだけが、Liquid Glassの背景に青のアクセントカラーを使用しています。](https://docs-assets.developer.apple.com/published/48dc83152523d157900d7fa6cabb26b3/colors-liquid-glass-usage-correct%402x.png)

![丸に囲まれたチェックマークが適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

**アプリの背景がカラフルな場合は、コントロールラベルに似たカラーを使わない。** カラーを使うとアプリの視覚的な魅力を増したり、遊び心を出したり、ブランドらしさを表現したりできますが、カラーを使いすぎるとくどい印象になり、コントロールラベルが読みづらくなります。アプリにカラフルな背景や視覚的に豊かなコンテンツがある場合は、ツールバーとタブバーにモノクロの見た目を使用するか、視覚的に十分に異なるアクセントカラーを選択します。逆に、主にモノクロのコンテンツや背景があるアプリでは、ブランドカラーをアプリのアクセントカラーにすることで、アプリ体験を調整して企業の独自性を示す効果的な方法になる可能性があります。

**コンテンツレイヤー内のカラーの配置に注意する。** 可能であれば、コンテンツレイヤーとコントロールで似たカラーが重ならないようにして、インターフェイスに十分なコントラストを確保してください。カラフルなコンテンツが断続的にコントロールの下をスクロールすることがあっても、コンテンツのデフォルト状態や静止状態（スクロール可能なコンテンツの画面上部など）では、はっきりと判読できるようにしてください。

## [カラーマネジメント](/jp/design/human-interface-guidelines/color#Color-management)

 _色空間_ とは、RGBやCMYKなどの _カラーモデル_ におけるカラーの集合を表します。一般的な色空間（ _色域_ と呼ばれることもあります）として、sRGBやDisplay P3が挙げられます。

![sRGB空間に含まれるカラーセットを、P3色空間に含まれる、より規模の大きいカラーセットと比較した図。](https://docs-assets.developer.apple.com/published/c10d0ec4c78a6b824552058caac031b5/color-graphic-wide-color%402x.png)

 _カラープロファイル_ は、カラーを数値表現に対応させる数式やデータ表などを使用して色空間の中のカラーを記述したものです。画像にはカラープロファイルが埋め込まれ、デバイスが画像のカラーを正しく解釈してディスプレイに再現できるようになっています。

**画像にカラープロファイルを適用する。** カラープロファイルは、さまざまなディスプレイでアプリのカラーを意図した通りに表示するために役立ちます。sRGB色空間は、ほとんどのディスプレイでカラーを正確に再現します。

**ワイドカラー互換ディスプレイでの視覚体験を高める場合はワイドカラーを使用する。** ワイドカラーディスプレイはP3色空間に対応しています。P3色空間を使用すると、sRGBよりも豊かで鮮やかなカラーを再現できます。そのため、ワイドカラーを使用した写真やビデオはより実物に近い表現が可能になり、ワイドカラーを使用した視覚的なデータやステータスインジケータはさらに豊富な情報を伝えることができます。ワイドカラーを使用する場合は、各ピクセルのチャネル当たり16ビットのDisplay P3カラープロファイルを使用し、画像をPNG形式で書き出します。ワイドカラー画像を作成してP3カラーを選択するには、ワイドカラーディスプレイを使用する必要がある点に注意してください。

**必要な場合は色空間に固有な画像とカラーバリエーションを提供する。** 通常、P3カラーとその画像は、sRGBディスプレイでも問題なく表示されます。ただし、sRGBディスプレイでは、よく似た2つのP3カラーを区別できない場合もあります。P3カラーを使用したグラデーションは、sRGBディスプレイでは不完全に見える場合もあります。このような問題を回避し、ワイドカラーとsRGBの両方のディスプレイでビジュアルを忠実に再現するには、Xcodeプロジェクトでアセットカタログを使用し、それぞれの色空間に対して異なる画像とカラーを提供します。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/color#Platform-considerations)

### [iOS/iPadOS](/jp/design/human-interface-guidelines/color#iOS-iPadOS)

iOSでは、 _システム_ および _グループ化_ という2種類のダイナミックバックグラウンドカラーが定義されており、それぞれに1次、2次、および3次といったバリアントが含まれています。これにより、階層的に情報を伝えることができます。通常は、グループ化したテーブルビューにはグループ化のバックグラウンドカラー（[`systemGroupedBackground`](/documentation/UIKit/UIColor/systemGroupedBackground)、[`secondarySystemGroupedBackground`](/documentation/UIKit/UIColor/secondarySystemGroupedBackground)、および[`tertiarySystemGroupedBackground`](/documentation/UIKit/UIColor/tertiarySystemGroupedBackground)）を、その他にはシステムセットのバックグラウンドカラー（[`systemBackground`](/documentation/UIKit/UIColor/systemBackground)、[`secondarySystemBackground`](/documentation/UIKit/UIColor/secondarySystemBackground)、および[`tertiarySystemBackground`](/documentation/UIKit/UIColor/tertiarySystemBackground)）を使用します。

どちらのセットのバックグランドカラーでも、通常は次のようにバリアントを使用して階層を示します。

  * 1次: 全体ビュー

  * 2次: 全体ビュー内のコンテンツや要素のグループ化

  * 3次: セカンダリな要素内のコンテンツや要素のグループ化

iOSでは、フォアグラウンドコンテンツ用に以下のダイナミックカラーが定義されています。

カラー| 用途| UIKit API  
---|---|---  
ラベル| 1次コンテンツを含むテキストラベル。| [`label`](/documentation/UIKit/UIColor/label)  
第2ラベル| 2次コンテンツを含むテキストラベル。| [`secondaryLabel`](/documentation/UIKit/UIColor/secondaryLabel)  
第3ラベル| 3次コンテンツを含むテキストラベル。| [`tertiaryLabel`](/documentation/UIKit/UIColor/tertiaryLabel)  
第4ラベル| 4次コンテンツを含むテキストラベル。| [`quaternaryLabel`](/documentation/UIKit/UIColor/quaternaryLabel)  
プレースホルダテキスト| コントロールやテキストビューのプレースホルダのテキスト。| [`placeholderText`](/documentation/UIKit/UIColor/placeholderText)  
区切り| 下にあるコンテンツが表示される区切り。| [`separator`](/documentation/UIKit/UIColor/separator)  
不透明な区切り| 下にあるコンテンツが表示されない区切り。| [`opaqueSeparator`](/documentation/UIKit/UIColor/opaqueSeparator)  
リンク| リンクとして動作するテキスト。| [`link`](/documentation/UIKit/UIColor/link)  
  
### [macOS](/jp/design/human-interface-guidelines/color#macOS)

macOSでは、以下のダイナミックシステムカラーが定義されています（標準の「カラー」パネルの「デベロッパ」パレットでも表示できます）:

カラー| 用途| AppKit API  
---|---|---  
選択されたコントロールの代替テキストカラー| リストやテーブル内で選択された部分のテキスト。| [`alternateSelectedControlTextColor`](/documentation/AppKit/NSColor/alternateSelectedControlTextColor)  
交互に塗り分けるコンテンツのバックグラウンドカラー| リストビュー、テーブルビュー、コレクションビューの交互に塗り分ける行や列の背景。| [`alternatingContentBackgroundColors`](/documentation/AppKit/NSColor/alternatingContentBackgroundColors)  
コントロールのアクセント| システム設定でユーザが選択したアクセントカラー。| [`controlAccentColor`](/documentation/AppKit/NSColor/controlAccentColor)  
コントロールのバックグラウンドカラー| ブラウザやテーブルなど、大きなインターフェイス要素の背景。| [`controlBackgroundColor`](/documentation/AppKit/NSColor/controlBackgroundColor)  
コントロールのカラー| コントロールの表面。| [`controlColor`](/documentation/AppKit/NSColor/controlColor)  
コントロールのテキストカラー| 使用可能なコントロールのテキスト。| [`controlTextColor`](/documentation/AppKit/NSColor/controlTextColor)  
現在のコントロールの色合い| システムで定義されたコントロールの色合い。| [`currentControlTint`](/documentation/AppKit/NSColor/currentControlTint)  
使用不可のコントロールのテキストカラー| 使用不可のコントロールのテキスト。| [`disabledControlTextColor`](/documentation/AppKit/NSColor/disabledControlTextColor)  
検索ハイライトカラー| 検索インジケータのカラー。| [`findHighlightColor`](/documentation/AppKit/NSColor/findHighlightColor)  
グリッドカラー| テーブルなどのインターフェイス要素のグリッド線。| [`gridColor`](/documentation/AppKit/NSColor/gridColor)  
ヘッダのテキストカラー| テーブルのヘッダセルのテキスト。| [`headerTextColor`](/documentation/AppKit/NSColor/headerTextColor)  
ハイライトカラー| 画面上のバーチャル光源。| [`highlightColor`](/documentation/AppKit/NSColor/highlightColor)  
キーボードフォーカスインジケータのカラー| キーボードを使用してインターフェイスを操作する際に、現在フォーカスが当たっているコントロールの周囲に表示されるリング。| [`keyboardFocusIndicatorColor`](/documentation/AppKit/NSColor/keyboardFocusIndicatorColor)  
ラベルカラー| 1次コンテンツを含むラベルのテキスト。| [`labelColor`](/documentation/AppKit/NSColor/labelColor)  
リンクカラー| ほかのコンテンツへのリンク。| [`linkColor`](/documentation/AppKit/NSColor/linkColor)  
プレースホルダのテキストカラー| コントロールやテキストビューのプレースホルダ文字列。| [`placeholderTextColor`](/documentation/AppKit/NSColor/placeholderTextColor)  
第4ラベルカラー| 第3レベルよりも重要度の低いラベルのテキスト。ウォーターマークのテキストなど。| [`quaternaryLabelColor`](/documentation/AppKit/NSColor/quaternaryLabelColor)  
第2ラベルカラー| 第1レベルよりも重要度の低いラベルのテキスト。小見出しや追加情報を表すラベルなど。| [`secondaryLabelColor`](/documentation/AppKit/NSColor/secondaryLabelColor)  
選択されたコンテンツのバックグラウンドカラー| キーウインドウやビューで選択されたコンテンツの背景。| [`selectedContentBackgroundColor`](/documentation/AppKit/NSColor/selectedContentBackgroundColor)  
選択されたコントロールのカラー| 選択されたコントロールの表面。| [`selectedControlColor`](/documentation/AppKit/NSColor/selectedControlColor)  
選択されたコントロールのテキストカラー| 選択されたコントロールのテキスト。| [`selectedControlTextColor`](/documentation/AppKit/NSColor/selectedControlTextColor)  
選択されたメニュー項目のテキストカラー| 選択されメニューのテキスト。| [`selectedMenuItemTextColor`](/documentation/AppKit/NSColor/selectedMenuItemTextColor)  
選択されたテキストのバックグラウンドカラー| 選択されたテキストの背景。| [`selectedTextBackgroundColor`](/documentation/AppKit/NSColor/selectedTextBackgroundColor)  
選択されたテキストのカラー| 選択されたテキストのカラー。| [`selectedTextColor`](/documentation/AppKit/NSColor/selectedTextColor)  
区切りカラー| コンテンツのセクション間の区切り。| [`separatorColor`](/documentation/AppKit/NSColor/separatorColor)  
シャドウカラー| 画面上の持ち上がったオブジェクトのバーチャルな影。| [`shadowColor`](/documentation/AppKit/NSColor/shadowColor)  
第3ラベルカラー| 第2レベルよりも重要度の低いラベルのテキスト。| [`tertiaryLabelColor`](/documentation/AppKit/NSColor/tertiaryLabelColor)  
テキストのバックグラウンドカラー| テキストの背景となる色。| [`textBackgroundColor`](/documentation/AppKit/NSColor/textBackgroundColor)  
テキストカラー| 書類内のテキスト。| [`textColor`](/documentation/AppKit/NSColor/textColor)  
ページの後ろのバックグラウンドカラー| 書類のコンテンツの後ろの背景。| [`underPageBackgroundColor`](/documentation/AppKit/NSColor/underPageBackgroundColor)  
選択されたコンテンツのバックグラウンドカラー（未強調）| 重要度の低いウインドウやビューで選択されたコンテンツ。| [`unemphasizedSelectedContentBackgroundColor`](/documentation/AppKit/NSColor/unemphasizedSelectedContentBackgroundColor)  
選択されたテキストのバックグラウンドカラー（未強調）| 重要度の低いウインドウやビューで選択されたテキストの背景。| [`unemphasizedSelectedTextBackgroundColor`](/documentation/AppKit/NSColor/unemphasizedSelectedTextBackgroundColor)  
選択されたテキストのカラー（未強調）| 重要度の低いウインドウやビューで選択されたテキスト。| [`unemphasizedSelectedTextColor`](/documentation/AppKit/NSColor/unemphasizedSelectedTextColor)  
ウインドウのバックグラウンドカラー| ウインドウの背景。| [`windowBackgroundColor`](/documentation/AppKit/NSColor/windowBackgroundColor)  
ウインドウフレームのテキストカラー| ウインドウのタイトルバー領域のテキスト。| [`windowFrameTextColor`](/documentation/AppKit/NSColor/windowFrameTextColor)  
  
#### [アプリのアクセントカラー](/jp/design/human-interface-guidelines/color#App-accent-colors)

macOS 11以降では、 _アクセントカラー_ を指定してアプリのボタン、選択のハイライト、サイドバーのアイコンの見た目をカスタマイズできます。アクセントカラーは、「一般」＞「アクセントカラー」設定の現在値が _マルチカラー_ である場合に適用されます。

![システム設定アプリのアクセントカラーピッカーのスクリーンショット。](https://docs-assets.developer.apple.com/published/2eb7a2be85ea17d65fca559587b0be00/colors-accent-colors-picker-multicolor%402x.png)

ユーザがアクセントカラー設定をマルチカラー以外の値に設定すると、アプリ全体の関連する項目で、アクセントカラーに代わって選択したカラーが適用されます。サイドバーは例外で、指定した固定カラーが使われます。固定カラーのサイドバーアイコンでは特定のカラーが意味を持つため、アクセントカラー設定の値を変更しても、カラーは上書きされません。ガイダンスは、[サイドバー](/jp/design/human-interface-guidelines/sidebars)を参照してください。

### [tvOS](/jp/design/human-interface-guidelines/color#tvOS)

**アプリのロゴと調和した、カラー数を抑えたカラーパレットを選択することを検討する。** カラーを控えめに使うことで、コンテンツの調和を保ちながらブランドのイメージを伝えることができます。

**カラーだけを使用してフォーカスを示さない。** 要素にフォーカスが当たって操作対象となっていることを伝える主な方法としては、わずかに拡大したり、操作に反応してアニメーションを表示させたりといった方法があります。

### [visionOS](/jp/design/human-interface-guidelines/color#visionOS)

**カラーの使用を控えめにする（特にガラス上で）。** visionOSの標準ウインドウでは通常、システム定義のガラス[マテリアル](/jp/design/human-interface-guidelines/materials)が使用されるため、ユーザの物理的な周囲環境の光や物体とユーザのスペースが透けて見えます。ガラスではこうした現実の物体や仮想オブジェクトの色が透けるため、ウインドウ内のアプリコンテンツがカラフルになっていると読みやすさに影響するかもしれません。カラーを使用するのは、重要な情報に注意を向けたり、インターフェイスのパーツ同士の関係を示したりする場合に留めることをおすすめします。

**カラーは太字テキストと大きな領域で使うことが望ましい。** 太字でないテキストまたは小さい領域でカラーを使うと、見づらくなったり、分かりにくくなったりすることがあります。

**完全なイマーシブ体験では、輝度レベルのバランスを調整してユーザが視覚的に快適に使えるようにする。** コントラストを高めるとユーザの注意を重要なコンテンツに向けることができますが、ユーザの目が暗い環境に慣れていると、視覚的な不快感が生じる可能性もあります。コンテンツの明るさを一番高くするのは、その他の視覚的な状況も明るい場合のみにしましょう。例えば、明るいオブジェクトを、非常に暗い、または黒い背景に表示することは避けてください。オブジェクトが点滅したり動いたりする場合はなおさらです。

### [watchOS](/jp/design/human-interface-guidelines/color#watchOS)

**バックグラウンドカラーは、既存のコンテンツに対応するか情報を追加する目的で使う。** バックグラウンドカラーを使うと、その場に合った雰囲気を演出して、主要なコンテンツにユーザの注意を引くことができます。例えば、アクティビティのムーブ、エクササイズ、スタンドアクティビティリングのインフォグラフィック表示は、リングのカラーに合ったバックグラウンドカラーになります。バックグラウンドカラーは、単なる装飾目的ではなく、ユーザに重要な情報を伝えたいときに使ってください。ワークアウトやオーディオ再生のアプリなど、長時間画面に残り続ける可能性が高いビューでは、フルスクリーンバックグラウンドカラーを使用しないでください。

**フルカラーではなく淡色モードでグラフィックスのコンプリケーションを使用するユーザがいることを認識する。** グラフィックスのコンプリケーションの画像、ゲージ、テキストに、ユーザが選択したカラーに基づく単色が使用される場合があります。ガイダンスは、[コンプリケーション](/jp/design/human-interface-guidelines/complications)を参照してください。

## [仕様](/jp/design/human-interface-guidelines/color#Specifications)

### [システムカラー](/jp/design/human-interface-guidelines/color#System-colors)

名前| SwiftUI API| デフォルト（ライト）| デフォルト（ダーク）| コントラストを上げる（ライト）| コントラストを上げる（ダーク）  
---|---|---|---|---|---  
赤| [`red`](/documentation/SwiftUI/Color/red)| ![R-255,G-56,B-60](https://docs-assets.developer.apple.com/published/56ba9eebe119d2e1b3063503a2eb45b7/colors-unified-red-light%402x.png)| ![R-255,G-66,B-69](https://docs-assets.developer.apple.com/published/9d7a7df4db48b0dcbd2915724d010235/colors-unified-red-dark%402x.png)| ![R-233,G-21,B-45](https://docs-assets.developer.apple.com/published/5b3473fcd986facfdee26a24601c7082/colors-unified-accessible-red-light%402x.png)| ![R-255,G-97,B-101](https://docs-assets.developer.apple.com/published/d097760a50a181eb7f688e9d62f4e710/colors-unified-accessible-red-dark%402x.png)  
オレンジ| [`orange`](/documentation/SwiftUI/Color/orange)| ![R-255,G-141,B-40](https://docs-assets.developer.apple.com/published/57f431ec786e31e33f578ace3dbb8c78/colors-unified-orange-light%402x.png)| ![R-255,G-146,B-48](https://docs-assets.developer.apple.com/published/e906c25c1cadcb9cf7514d01b83f3bb7/colors-unified-orange-dark%402x.png)| ![R-197,G-83,B-0](https://docs-assets.developer.apple.com/published/2222321d0b29cad6987f0f6e26d198c1/colors-unified-accessible-orange-light%402x.png)| ![R-255,G-160,B-86](https://docs-assets.developer.apple.com/published/c82984219db600ea8396f4fd1933fc19/colors-unified-accessible-orange-dark%402x.png)  
黄| [`yellow`](/documentation/SwiftUI/Color/yellow)| ![R-255,G-204,B-0](https://docs-assets.developer.apple.com/published/bebac431675840fa7e0e70cce0a6eb76/colors-unified-yellow-light%402x.png)| ![R-255,G-214,B-0](https://docs-assets.developer.apple.com/published/80c02086ccc5f013058932129cf9c6d3/colors-unified-yellow-dark%402x.png)| ![R-161,G-106,B-0](https://docs-assets.developer.apple.com/published/a51b94b82d9ea46e9de2ab8da5a57bbe/colors-unified-accessible-yellow-light%402x.png)| ![R-254,G-223,B-67](https://docs-assets.developer.apple.com/published/cd06b12d9e053739b089fb102b70901e/colors-unified-accessible-yellow-dark%402x.png)  
緑| [`green`](/documentation/SwiftUI/Color/green)| ![R-52,G-199,B-89](https://docs-assets.developer.apple.com/published/b4226cfcf596812d46bd084322f47e65/colors-unified-green-light%402x.png)| ![R-48,G-209,B-88](https://docs-assets.developer.apple.com/published/7724e5dd4f60d300eaffe45c9a5e1f9d/colors-unified-green-dark%402x.png)| ![R-0,G-137,B-50](https://docs-assets.developer.apple.com/published/51471c6578d192e9dae6f40d8ace1835/colors-unified-accessible-green-light%402x.png)| ![R-74,G-217,B-104](https://docs-assets.developer.apple.com/published/aff6bca03c74050c6b78015925c8fd21/colors-unified-accessible-green-dark%402x.png)  
ミント| [`mint`](/documentation/SwiftUI/Color/mint)| ![R-0,G-200,B-179](https://docs-assets.developer.apple.com/published/5d07acb38b9d0d7098f0b92456a7d27c/colors-unified-mint-light%402x.png)| ![R-0,G-218,B-195](https://docs-assets.developer.apple.com/published/851d8c0c2bea51a9377ae31520097e8c/colors-unified-mint-dark%402x.png)| ![R-0,G-133,B-117](https://docs-assets.developer.apple.com/published/d24198fce4dd42183e7b35abc9b67c20/colors-unified-accessible-mint-light%402x.png)| ![R-84,G-223,B-203](https://docs-assets.developer.apple.com/published/72586072586bb6d91589cc4ab78177b1/colors-unified-accessible-mint-dark%402x.png)  
ティール| [`teal`](/documentation/SwiftUI/Color/teal)| ![R-0,G-195,B-208](https://docs-assets.developer.apple.com/published/6b8e5d90758cc858b4d3e20110a31f53/colors-unified-teal-light%402x.png)| ![R-0,G-210,B-224](https://docs-assets.developer.apple.com/published/d02bd29f4ba3580e84756f8c332fd677/colors-unified-teal-dark%402x.png)| ![R-0,G-129,B-152](https://docs-assets.developer.apple.com/published/f2137be89fb79e4822b633a450d6fc2c/colors-unified-accessible-teal-light%402x.png)| ![R-59,G-221,B-236](https://docs-assets.developer.apple.com/published/9a76a2333c746ded944e6610a01d4daf/colors-unified-accessible-teal-dark%402x.png)  
シアン| [`cyan`](/documentation/SwiftUI/Color/cyan)| ![R-0,G-192,B-232](https://docs-assets.developer.apple.com/published/3eb3076ca71a16ce1bede399e815e736/colors-unified-cyan-light%402x.png)| ![R-60,G-211,B-254](https://docs-assets.developer.apple.com/published/34399c5683f58d0710a50625f2fbca64/colors-unified-cyan-dark%402x.png)| ![R-0,G-126,B-174](https://docs-assets.developer.apple.com/published/e54287c8eb8d532283dac9d646886953/colors-unified-accessible-cyan-light%402x.png)| ![R-109,G-217,B-255](https://docs-assets.developer.apple.com/published/6d3ef826eb37c61642d57f798de4d14f/colors-unified-accessible-cyan-dark%402x.png)  
青| [`blue`](/documentation/SwiftUI/Color/blue)| ![R-0,G-136,B-255](https://docs-assets.developer.apple.com/published/6ea9cabe180214ed99be04320df3501b/colors-unified-blue-light%402x.png)| ![R-0,G-145,B-255](https://docs-assets.developer.apple.com/published/580c321f95c59b2b4479be066d24f10f/colors-unified-blue-dark%402x.png)| ![R-30,G-110,B-244](https://docs-assets.developer.apple.com/published/f46653318bcfae105ff78fe412d64da2/colors-unified-accessible-blue-light%402x.png)| ![R-92,G-184,B-255](https://docs-assets.developer.apple.com/published/07b7bcb2d65911636342cee25db1f953/colors-unified-accessible-blue-dark%402x.png)  
インディゴ| [`indigo`](/documentation/SwiftUI/Color/indigo)| ![R-97,G-85,B-245](https://docs-assets.developer.apple.com/published/2da5c45a0e483dcaac4447464da4b6a7/colors-unified-indigo-light%402x.png)| ![R-109,G-124,B-255](https://docs-assets.developer.apple.com/published/b5e1fd9a1fc2347cc7238668b2df251b/colors-unified-indigo-dark%402x.png)| ![R-86,G-74,B-222](https://docs-assets.developer.apple.com/published/e326f52473ede4e5427208f9929196d9/colors-unified-accessible-indigo-light%402x.png)| ![R-167,G-170,B-255](https://docs-assets.developer.apple.com/published/d19249c65dab279c41f16c802365df10/colors-unified-accessible-indigo-dark%402x.png)  
紫| [`purple`](/documentation/SwiftUI/Color/purple)| ![R-203,G-48,B-224](https://docs-assets.developer.apple.com/published/2f07dfc6c397fba6d0abda5f5051a025/colors-unified-purple-light%402x.png)| ![R-219,G-52,B-242](https://docs-assets.developer.apple.com/published/04bce86fef3077014010ce6cfceb659f/colors-unified-purple-dark%402x.png)| ![R-176,G-47,B-194](https://docs-assets.developer.apple.com/published/a63779bec8a313582e11c6bbe348fc10/colors-unified-accessible-purple-light%402x.png)| ![R-234,G-141,B-255](https://docs-assets.developer.apple.com/published/82c3b96b548cbc455ef685f3e44d01d1/colors-unified-accessible-purple-dark%402x.png)  
ピンク| [`pink`](/documentation/SwiftUI/Color/pink)| ![R-255,G-45,B-85](https://docs-assets.developer.apple.com/published/1486931dce50d7610a397607afc0fb4d/colors-unified-pink-light%402x.png)| ![R-255,G-55,B-95](https://docs-assets.developer.apple.com/published/d68a9dbf37bab028b011f68fdd794e9c/colors-unified-pink-dark%402x.png)| ![R-231,G-18,B-77](https://docs-assets.developer.apple.com/published/d696af68031ce91a63330e0469ff592b/colors-unified-accessible-pink-light%402x.png)| ![R-255,G-138,B-196](https://docs-assets.developer.apple.com/published/a64993da9a61253e266e411d76c2cefd/colors-unified-accessible-pink-dark%402x.png)  
茶| [`brown`](/documentation/SwiftUI/Color/brown)| ![R-172,G-127,B-94](https://docs-assets.developer.apple.com/published/366eca06d26c2f759d6200a1e9b0a56f/colors-unified-brown-light%402x.png)| ![R-183,G-138,B-102](https://docs-assets.developer.apple.com/published/df6c5da440560b2054af5b55fe9b87f4/colors-unified-brown-dark%402x.png)| ![R-149,G-109,B-81](https://docs-assets.developer.apple.com/published/c80a760835a2bc94a68337d0208a469e/colors-unified-accessible-brown-light%402x.png)| ![R-219,G-166,B-121](https://docs-assets.developer.apple.com/published/3c6062e007c9d60e4684d063b3618786/colors-unified-accessible-brown-dark%402x.png)  
  
visionOSのシステムカラーでは、デフォルトでダークなカラー値を使用します。

### [iOS、iPadOSのシステムグレイカラー](/jp/design/human-interface-guidelines/color#iOS-iPadOS-system-gray-colors)

名前| UIKit API| デフォルト（ライト）| デフォルト（ダーク）| コントラストを上げる（ライト）| コントラストを上げる（ダーク）  
---|---|---|---|---|---  
グレイ| [`systemGray`](/documentation/UIKit/UIColor/systemGray)| ![R-142,G-142,B-147](https://docs-assets.developer.apple.com/published/cc1289b6fd4b76c79bbeda356463232a/ios-default-systemgray%402x.png)| ![R-142,G-142,B-147](https://docs-assets.developer.apple.com/published/cc1289b6fd4b76c79bbeda356463232a/ios-default-systemgraydark%402x.png)| ![R-108,G-108,B-112](https://docs-assets.developer.apple.com/published/5d86cbc8b4ddef8b68954882b4c87a18/ios-accessible-systemgray%402x.png)| ![R-174,G-174,B-178](https://docs-assets.developer.apple.com/published/d00617ff05181a53d2cb5ddf143d502e/ios-accessible-systemgraydark%402x.png)  
グレイ（2）| [`systemGray2`](/documentation/UIKit/UIColor/systemGray2)| ![R-174,G-174,B-178](https://docs-assets.developer.apple.com/published/d00617ff05181a53d2cb5ddf143d502e/ios-default-systemgray2%402x.png)| ![R-99,G-99,B-102](https://docs-assets.developer.apple.com/published/1f681e808c0f4f35a2e7642872719c8b/ios-default-systemgray2dark%402x.png)| ![R-142,G-142,B-147](https://docs-assets.developer.apple.com/published/cc1289b6fd4b76c79bbeda356463232a/ios-accessible-systemgray2%402x.png)| ![R-124,G-124,B-128](https://docs-assets.developer.apple.com/published/f941ec556140a435aa9556a993e57e63/ios-accessible-systemgray2dark%402x.png)  
グレイ（3）| [`systemGray3`](/documentation/UIKit/UIColor/systemGray3)| ![R-199,G-199,B-204](https://docs-assets.developer.apple.com/published/bcbb9fb97382e52aa09de7239a6edcf7/ios-default-systemgray3%402x.png)| ![R-72,G-72,B-74](https://docs-assets.developer.apple.com/published/d99ad33dcdd426585e7107e1b130d713/ios-default-systemgray3dark%402x.png)| ![R-174,G-174,B-178](https://docs-assets.developer.apple.com/published/d00617ff05181a53d2cb5ddf143d502e/ios-accessible-systemgray3%402x.png)| ![R-84,G-84,B-86](https://docs-assets.developer.apple.com/published/693c40b65e2752b3a2b7741d61ebbb3b/ios-accessible-systemgray3dark%402x.png)  
グレイ（4）| [`systemGray4`](/documentation/UIKit/UIColor/systemGray4)| ![R-209,G-209,B-214](https://docs-assets.developer.apple.com/published/5e1c546e8c78d9700b1ee58ce3a39972/ios-default-systemgray4%402x.png)| ![R-58,G-58,B-60](https://docs-assets.developer.apple.com/published/983cdcdfa9a664db0c5ff7c09905582a/ios-default-systemgray4dark%402x.png)| ![R-188,G-188,B-192](https://docs-assets.developer.apple.com/published/93644725b33daf923f7e3a146e9b2d42/ios-accessible-systemgray4%402x.png)| ![R-68,G-68,B-70](https://docs-assets.developer.apple.com/published/6439d861c1fe8a41615d5f09d3cde938/ios-accessible-systemgray4dark%402x.png)  
グレイ（5）| [`systemGray5`](/documentation/UIKit/UIColor/systemGray5)| ![R-229,G-229,B-234](https://docs-assets.developer.apple.com/published/91f296b3990bfe6dcd28b1804c803581/ios-default-systemgray5%402x.png)| ![R-44,G-44,B-46](https://docs-assets.developer.apple.com/published/a8b1d65979b02865c203f18019b1084d/ios-default-systemgray5dark%402x.png)| ![R-216,G-216,B-220](https://docs-assets.developer.apple.com/published/616159815cf002c39f570affa027c298/ios-accessible-systemgray5%402x.png)| ![R-54,G-54,B-56](https://docs-assets.developer.apple.com/published/aacb35c6af213ef544f77d26df56df39/ios-accessible-systemgray5dark%402x.png)  
グレイ（6）| [`systemGray6`](/documentation/UIKit/UIColor/systemGray6)| ![R-242,G-242,B-247](https://docs-assets.developer.apple.com/published/3d60e2b1bf4771610453a31de912647b/ios-default-systemgray6%402x.png)| ![R-28,G-28,B-30](https://docs-assets.developer.apple.com/published/5d86f031014f556ef2d26da001c1f639/ios-default-systemgray6dark%402x.png)| ![R-235,G-235,B-240](https://docs-assets.developer.apple.com/published/82102708ad5dc7921fc0473f6ace4613/ios-accessible-systemgray6%402x.png)| ![R-36,G-36,B-38](https://docs-assets.developer.apple.com/published/5dc6249020925c5ec09f88f8adc9bbaa/ios-accessible-systemgray6dark%402x.png)  
  
SwiftUIで`systemGray`に相当するのは[`gray`](/documentation/SwiftUI/Color/gray)です。

## [リソース](/jp/design/human-interface-guidelines/color#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/color#Related)

[ダークモード](/jp/design/human-interface-guidelines/dark-mode)

[アクセシビリティ](/jp/design/human-interface-guidelines/accessibility)

[マテリアル](/jp/design/human-interface-guidelines/materials)

[Appleデザインリソース](https://developer.apple.com/design/resources/)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/color#Developer-documentation)

[`Color`](/documentation/SwiftUI/Color) — SwiftUI

[`UIColor`](/documentation/UIKit/UIColor) — UIKit

[カラー](/documentation/AppKit/color) — AppKit

#### [ビデオ](/jp/design/human-interface-guidelines/color#Videos)

[](https://developer.apple.com/videos/play/wwdc2025/219)

## [変更履歴](/jp/design/human-interface-guidelines/color#Change-log)

日付| 変更内容  
---|---  
2025年12月16日| Liquid Glassに関するガイダンスを更新。  
2025年6月09日| システムカラー値を更新、およびLiquid Glassに関するガイダンスを追加。  
2024年2月02日| iOSおよびiPadOSでのUIKitとSwiftUIのグレイカラーを区別し、visionOSアプリでの輝度レベルのバランスに関するガイダンスを追加。  
2023年9月12日| watchOSのビューにおけるバックグラウンドカラーの使用に関するガイドを改善。tvOSのカラー見本を追加。  
2023年6月21日| visionOSのガイダンスを追加するために更新。  
2023年6月05日| watchOSのバックグラウンドカラーの使用に関するガイドを更新。  
2022年12月19日| iOSおよびiPadOSのシステムカラーのミント（ダークモード）のRGB値を修正。

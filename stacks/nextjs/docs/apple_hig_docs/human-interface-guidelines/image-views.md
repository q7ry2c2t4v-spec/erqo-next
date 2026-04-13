# 画像ビュー

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/image-views

# 画像ビュー

画像ビューには、透明または不透明な背景の上に1つの画像が表示されます。場合によっては、画像のアニメーションシーケンスが表示されることもあります。

![図案化された写真。画像は6色のオリジナルAppleロゴをイメージさせる赤色になっています。](https://docs-assets.developer.apple.com/published/0307c2c5d25332199d2b5e634f455137/components-image-view-intro%402x.png)

画像ビュー内では、画像を伸ばしたり、拡大/縮小したり、画面に合わせたり、特定の位置に固定したりできます。通常、画像ビューはインタラクティブではありません。

## [ベストプラクティス](/jp/design/human-interface-guidelines/image-views#Best-practices)

**画像ビューはビューの主な目的が単に画像を表示することである場合に使用する。** まれにあることですが、画像をインタラクティブにしたい場合は、画像ビューにボタンの挙動を追加するのではなく、システムで提供される[ボタン](https://developer.apple.com/jp/design/human-interface-guidelines/buttons)に画像を表示してください。

**インターフェイスにアイコンを表示したい場合は、画像ビューの代わりにシンボルまたはインターフェイスアイコンを使用することを検討する。**[SF Symbols](/jp/design/human-interface-guidelines/sf-symbols)では、ベクトルベースのシンプルな画像の充実したライブラリが提供されます。これらの画像はさまざまなカラーや不透明度でレンダリングできます。[アイコン](https://developer.apple.com/jp/design/human-interface-guidelines/icons)（グリフまたはテンプレート画像とも呼ばれます）は一般にビットマップ画像で、透明でないピクセルにカラーを適用できます。シンボルでもインターフェイスアイコンでも、ユーザが選択するアクセントカラーを使用できます。

## [コンテンツ](/jp/design/human-interface-guidelines/image-views#Content)

画像ビューには、PNG、JPEG、PDFなどのさまざまなフォーマットのリッチ画像データを含めることができます。ガイダンスは、[画像](/jp/design/human-interface-guidelines/images)を参照してください。

**画像上にテキストをオーバーレイするときは注意する。** 画像上にテキストを合成すると、画像の明瞭さとテキストの読みやすさの両方が低下する場合があります。結果を改善するには、テキストと画像のコントラストを十分に確保すると共に、テキストのシャドウや背景のレイヤーを追加するなど、テキストオブジェクトを目立たせる方法を検討してください。

**アニメーションシーケンスではすべての画像に一貫したサイズを使用するよう努める。** ビューに合わせて画像を事前に拡大/縮小しておくと、システムでの拡大/縮小が不要になります。システムでの拡大/縮小が必要な場合は、すべての画像が同じサイズおよび同じ形状の方が一般にパフォーマンスがよくなります。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/image-views#Platform-considerations)

 _iOS、iPadOSに追加の考慮事項はありません。_

### [macOS](/jp/design/human-interface-guidelines/image-views#macOS)

**編集可能な画像ビューが必要なアプリの場合はイメージウェルを使用する。**[イメージウェル](https://developer.apple.com/jp/design/human-interface-guidelines/image-wells)は、コピー、ペースト、ドラッグ、およびDeleteキーを使ってのコンテンツの消去に対応する画像ビューです。

**クリッカブル画像を作成するときは画像ビューではなく画像ボタンを使用する。**[画像ボタン](https://developer.apple.com/jp/design/human-interface-guidelines/buttons#Image-buttons)は、画像またはアイコンが含まれ、ビューに表示されます。クリックするとアプリ固有のアクションが瞬時に開始されます。

### [tvOS](/jp/design/human-interface-guidelines/image-views#tvOS)

tvOSの多くの画像では、透明度のある複数のレイヤーを組み合わせて奥行き感が生み出されます。ガイダンスは、[レイヤード画像](/jp/design/human-interface-guidelines/images#Layered-images)を参照してください。

### [visionOS](/jp/design/human-interface-guidelines/image-views#visionOS)

visionOSのアプリやゲームのウインドウでは、画像ビューを使用して2D画像やステレオスコピック画像、空間写真を表示できます。アプリでRealityKitを使用している場合は、画像ビューの外側の3Dコンテンツの横に任意の種類の画像を表示したり、既存の2D画像から空間シーンを生成したりすることもできます。デザインのガイダンスは[「画像」の「visionOS」](/jp/design/human-interface-guidelines/images#visionOS)を、デベロッパ向けのガイダンスは[`ImagePresentationComponent`](/documentation/RealityKit/ImagePresentationComponent)を参照してください。

ウインドウやボリュームでのその他の3Dコンテンツの表示に関するガイダンスは、[「ウインドウ」の「visionOS」](/jp/design/human-interface-guidelines/windows#visionOS)を参照してください。

### [watchOS](/jp/design/human-interface-guidelines/image-views#watchOS)

**アニメーションの作成には可能な限りSwiftUIを使用する。** または、必要に応じて、WatchKitを使って画像要素内で画像のシーケンスをアニメートできます。デベロッパ向けのガイダンスは、[`WKImageAnimatable`](/documentation/WatchKit/WKImageAnimatable)を参照してください。

## [リソース](/jp/design/human-interface-guidelines/image-views#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/image-views#Related)

[画像](/jp/design/human-interface-guidelines/images)

[イメージウェル](/jp/design/human-interface-guidelines/image-wells)

[画像ボタン](/jp/design/human-interface-guidelines/buttons#Image-buttons)

[SF Symbols](/jp/design/human-interface-guidelines/sf-symbols)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/image-views#Developer-documentation)

[`Image`](/documentation/SwiftUI/Image) — SwiftUI

[`UIImageView`](/documentation/UIKit/UIImageView) — UIKit

[`NSImageView`](/documentation/AppKit/NSImageView) — AppKit

#### [ビデオ](/jp/design/human-interface-guidelines/image-views#Videos)

[](https://developer.apple.com/videos/play/wwdc2023/10181)

[](https://developer.apple.com/videos/play/wwdc2021/10021)

## [変更履歴](/jp/design/human-interface-guidelines/image-views#Change-log)

日付| 変更内容  
---|---  
2023年6月21日| visionOSのガイダンスを追加するために更新。

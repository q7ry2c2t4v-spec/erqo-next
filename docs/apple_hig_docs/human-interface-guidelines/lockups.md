# ロックアップ

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/lockups

# ロックアップ

ロックアップは、複数の別個のビューを組み合わせて1つのインタラクティブな単位にしたものです。

![見出し行と脚注行のテキストの上にある図案化された人物アイコン。画像は6色のオリジナルAppleロゴをイメージさせる赤色になっています。](https://docs-assets.developer.apple.com/published/e74eca5a04fc63d4d67f774f845d5144/components-lockups-intro%402x.png)

各ロックアップは、コンテンツビュー、ヘッダ、フッタで構成されます。ヘッダはロックアップのメインコンテンツの上、フッタはメインコンテンツの下に表示されます。ロックアップにフォーカスが移動すると、3つのビューすべてが一緒に広がったり縮まったりします。

アプリのニーズに応じて、カード、キャプションボタン、モノグラム、ポスターの4種類のロックアップを組み合わせることができます。

## [ベストプラクティス](/jp/design/human-interface-guidelines/lockups#Best-practices)

**ロックアップ間に十分なスペースを取る。** フォーカスが置かれたロックアップはサイズが大きくなるため、重なったりほかのロックアップを移動させたりしないようにロックアップ間に十分なスペースを確保します。ガイダンスは[レイアウト](/jp/design/human-interface-guidelines/layout)を参照してください。

![3列に等間隔で並んだ5つのロックアップを示す図。各列の中央のロックアップにフォーカスがあり、ほかのロックアップより少し大きくなっています。](https://docs-assets.developer.apple.com/published/67a6f9b8d570939f21cd6af73ce21032/lockups-generic%402x.png)

**1つの列またはグループ内で一貫したロックアップのサイズを使用する。** ボタンのグループや1列に並んだコンテンツ画像は、すべての要素の幅と高さを一致させると視覚的な魅力が増します。

デベロッパ向けのガイダンスは、[`TVLockupView`](/documentation/TVUIKit/TVLockupView)および[`TVLockupHeaderFooterView`](/documentation/TVUIKit/TVLockupHeaderFooterView)を参照してください。

## [カード](/jp/design/human-interface-guidelines/lockups#Cards)

カードでは、ヘッダ、フッタ、およびコンテンツビューを組み合わせてメディア項目の制限指定やレビューが表示されます。

![複数のカードが含まれたApple TV画面。そのうちの1つがハイライトされています。上部からハイライトされたカード内のプレースホルダコンテンツで、制限指定の位置および複数行のテキストが示されています。](https://docs-assets.developer.apple.com/published/f400f125041819281ab98d9305900dde/lockups-background%402x.png)

デベロッパ向けのガイダンスは、[`TVCardView`](/documentation/TVUIKit/TVCardView)を参照してください。

## [キャプションボタン](/jp/design/human-interface-guidelines/lockups#Caption-buttons)

キャプションボタンでは、ボタンの下にタイトルとサブタイトルを含めることができます。キャプションボタンには画像またはテキストを使用できます。

ユーザがキャプションボタンにフォーカスを置いたときに、スワイプするアクションと共にキャプションボタンが傾くようにしてください。縦に位置揃えしている場合は、キャプションボタンを上下に傾けます。横に位置揃えしている場合は、キャプションボタンを左右に傾けます。グリッドに表示している場合は、キャプションボタンを縦方向と横方向の両方に傾けます。

![横に並んだ4つのキャプションボタンがハイライトされているApple TV画面。左端のボタンはフォーカスされているので、少し拡大して表示され、背景から浮き上がっているように見えます。](https://docs-assets.developer.apple.com/published/4d17d738ba6eb73a1687ed9b1a955ee8/lockups-caption-button%402x.png)

デベロッパ向けのガイダンスは、[`TVCaptionButtonView`](/documentation/TVUIKit/TVCaptionButtonView)を参照してください。

## [モノグラム](/jp/design/human-interface-guidelines/lockups#Monograms)

モノグラムでは人物を明確にします。通常はメディア項目のキャストやスタッフを表します。各モノグラムは人物の円形の写真と名前で構成されます。画像が使用不可の場合は、画像の代わりにその人のイニシャルが表示されます。

**できる限りイニシャルではなく画像を使用する。** 人物の写真は、テキストよりも親密なつながりを生み出します。

![複数のモノグラムが横に並んでいるApple TV画面。左端のモノグラムがハイライトされています。各モノグラムにユーザのシンボルが含まれています。各モノグラムの下に、2行のテキストが示されたプレースホルダコンテンツがあります。](https://docs-assets.developer.apple.com/published/cd35d73e0bee5af4515295a809049ee4/lockups-monogram%402x.png)

デベロッパ向けのガイダンスは、[`TVMonogramContentView`](/documentation/TVUIKit/TVMonogramContentView)を参照してください。

## [ポスター](/jp/design/human-interface-guidelines/lockups#Posters)

ポスターは画像とオプションのタイトルおよびサブタイトルで構成されます。タイトルとサブタイトルはポスターにフォーカスが移動するまで非表示になります。ポスターは任意のサイズにできますが、コンテンツに適したサイズにする必要があります。[画像ビュー](/jp/design/human-interface-guidelines/image-views)の関連するガイドを参照してください。

![下端近くに横に並んだ複数のポスターが表示されているApple TV画面。1つのポスターがフォーカスされていて、その下に1行のテキストが示されたプレースホルダコンテンツがあります。](https://docs-assets.developer.apple.com/published/f5e35c8a97ffb3b86edffb4247359ec4/lockups-poster%402x.png)

デベロッパ向けのガイダンスは、[`TVPosterView`](/documentation/TVUIKit/TVPosterView)を参照してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/lockups#Platform-considerations)

 _iOS、iPadOS、macOS、visionOS、watchOSには対応していません。_

## [リソース](/jp/design/human-interface-guidelines/lockups#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/lockups#Related)

[tvOS向けのデザイン](/jp/design/human-interface-guidelines/designing-for-tvos)

[レイアウト](/jp/design/human-interface-guidelines/layout)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/lockups#Developer-documentation)

[`TVLockupView`](/documentation/TVUIKit/TVLockupView) — TVUIKit

[`TVLockupHeaderFooterView`](/documentation/TVUIKit/TVLockupHeaderFooterView) — TVUIKit

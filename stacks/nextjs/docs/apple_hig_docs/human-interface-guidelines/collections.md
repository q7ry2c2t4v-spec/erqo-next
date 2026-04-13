# コレクション

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/collections

# コレクション

コレクションを使うと、順序の付いたコンテンツのセットを管理して、カスタマイズ可能な視覚に訴えるレイアウトで表示できます。

![図案化された8つの画像アイコン。4つずつ2列に並んでいます。画像は全体が、6色のオリジナルAppleロゴを連想させる赤色になっています。](https://docs-assets.developer.apple.com/published/59d2bc55c4c2e946bb4559365573f276/components-collection-view-intro%402x.png)

コレクションは通常、画像ベースのコンテンツの表示に最適です。

## [ベストプラクティス](/jp/design/human-interface-guidelines/collections#Best-practices)

**可能な場合は常に、標準の行レイアウトやグリッドレイアウトを使用する。** コレクションは、デフォルトでコンテンツを水平方向の行やグリッドで表示します。これらは、ユーザがすぐに受け入れられるシンプルで効果的なレイアウトです。ユーザを戸惑わせたり、不必要に注目を引いたりするようなカスタムレイアウトは避けてください。

**テキストを表示する場合はコレクションではなくテーブルを使用する。** テキスト情報を表示したり要約したりする場合、通常は、スクロール可能なリストに表示する方がシンプルで効果的です。

**項目を選択しやすくする。** コレクションで項目にたどり着くのが難しすぎると、ユーザは不満を感じ、目的のコンテンツに到達する前に興味を失ってしまいます。画像の周囲に十分なパディングを設けると、フォーカスのある項目やホバーエフェクトを見やすくでき、コンテンツの重複を避けられます。

**必要に応じてカスタムの操作を追加する。** デフォルトでは、選択するときはタップし、編集するときはタッチして押さえたままにし、スクロールするときはスワイプします。アプリでカスタムのアクションが必要な場合は、それを実行するためのジェスチャを追加できます。

**ユーザが項目を挿入、削除、並べ替えた場合は、なるべくアニメーションを使用してフィードバックを返す。** コレクションでは、これらのアクション向けの標準アニメーションを利用できます。カスタムのアニメーションも使用できます。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/collections#Platform-considerations)

 _macOS、tvOS、visionOSに追加の考慮事項はありません。watchOSには対応していません。_

### [iOS/iPadOS](/jp/design/human-interface-guidelines/collections#iOS-iPadOS)

**動的にレイアウトを変化させる場合は細心の注意を払う。** コレクションのレイアウトは動的に変化させることができます。どんな変化も、その場にふさわしく、ユーザが戸惑わない動きにしてください。ユーザの明示的なアクションに反応する場合を除き、レイアウトの表示中や操作中はできるだけ変化させないようにします。

## [リソース](/jp/design/human-interface-guidelines/collections#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/collections#Related)

[リストとテーブル](/jp/design/human-interface-guidelines/lists-and-tables)

[画像ビュー](/jp/design/human-interface-guidelines/image-views)

[レイアウト](/jp/design/human-interface-guidelines/layout)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/collections#Developer-documentation)

[`UICollectionView`](/documentation/UIKit/UICollectionView) — UIKit

[`NSCollectionView`](/documentation/AppKit/NSCollectionView) — AppKit

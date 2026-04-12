# 評価インジケータ

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/rating-indicators

# 評価インジケータ

評価インジケータは、横方向に並んだグラフィカルなシンボル（デフォルトは星）によってユーザがランク付けを行うためのコンポーネントです。

![5つ星のうち3つであることを示す図案化された評価インジケータ。画像は6色のオリジナルAppleロゴをイメージさせる赤色になっています。](https://docs-assets.developer.apple.com/published/f42f1026882031ed572f4b4df726a13c/components-rating-indicators-intro%402x.png)

評価インジケータでは一部が欠けたシンボルを使った評価は行いません。つまり、評価は完全なシンボル1個を単位として表示されます。評価インジケータ内のシンボルの間隔は常に一定で、コンポーネントの幅に合わせて変化することはありません。

## [ベストプラクティス](/jp/design/human-interface-guidelines/rating-indicators#Best-practices)

**ランキングを簡単に変更できるようにする。** 項目のランキングリストを表示する場合は、ユーザが個々の項目のランキングを別の編集画面に移動せずに直接調整できるようにします。

**明確な目的もなく星をカスタムシンボルに置き換えない。** 星はランキングシンボルとして広く認知されています。ほかのシンボルを評価の尺度に使用すると違和感を持つユーザがいるかもしれません。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/rating-indicators#Platform-considerations)

 _macOSに追加の考慮事項はありません。 iOS、iPadOS、tvOS、visionOS、watchOSには対応していません。_

## [リソース](/jp/design/human-interface-guidelines/rating-indicators#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/rating-indicators#Related)

[評価およびレビュー](/jp/design/human-interface-guidelines/ratings-and-reviews)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/rating-indicators#Developer-documentation)

[`NSLevelIndicator.Style.rating`](/documentation/AppKit/NSLevelIndicator/Style/rating) — AppKit

## [変更履歴](/jp/design/human-interface-guidelines/rating-indicators#Change-log)

日付| 変更内容  
---|---  
2022年9月23日| 新規ページ。

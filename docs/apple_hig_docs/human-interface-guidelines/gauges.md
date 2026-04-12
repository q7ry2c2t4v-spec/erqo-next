# ゲージ

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/gauges

# ゲージ

ゲージは、ある範囲内での特定の数値を表すのに用います。

![円形の数値ゲージとその下にある直線のパーセントゲージの図案。画像は6色のオリジナルAppleロゴをイメージさせる赤色になっています。](https://docs-assets.developer.apple.com/published/1a72d5759d584827d882872b44c72a26/components-gauges-intro%402x.png)

ゲージはある範囲における現在の値を示すだけでなく、その範囲自体についてもより多くの情報をもたらします。例えば温度ゲージでは、特定の範囲内での最高温度と最低温度を示すテキストを表示し、それらの値の変化を色スペクトルを使って示すことで視覚に訴えることができます。

## [構造](/jp/design/human-interface-guidelines/gauges#Anatomy)

ゲージでは、値の範囲を表すのに円形または線形のラインを使い、現在の値をそのライン上の特定の位置にマップします。標準ゲージには、現在の値の位置を示すインジケータが表示されます。容量スタイルのゲージは、その値のライン上での位置までを塗りつぶして値を表現します。

円形および線形のゲージでは、標準スタイルと容量スタイルの両方で、watchOSのコンプリケーションに見た目がよく似たバリエーションを利用できます。このようなバリエーションはアクセサリと呼ばれ、iOSのロック画面ウィジェットやコンプリケーションの見た目を再現したい任意の場所で効果的に利用できます。

注意

macOSはゲージに加えて、レベルインジケータにも対応します。一部のレベルインジケータは視覚的にゲージに類似しています。ガイダンスは[macOS](/jp/design/human-interface-guidelines/gauges#macOS)を参照してください。

## [ベストプラクティス](/jp/design/human-interface-guidelines/gauges#Best-practices)

**現在の値と範囲の両端の値を説明する簡潔なラベルを作成する。** どのゲージスタイルでもすべてのラベルが表示されるわけではありませんが、視覚的なラベルはVoiceOverで読み上げられるので、画面を見られないユーザがゲージを理解する助けになります。

**ゲージが示す内容を効果的に伝えられるように、ラインをグラデーションで表現することを検討する。** 例えば温度ゲージでは、高温から低温まで変化する温度を赤から青へのグラデーションで表す手法を検討できます。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/gauges#Platform-considerations)

 _iOS、iPadOS、visionOS、watchOSに追加の考慮事項はありません。tvOSには対応していません。_

### [macOS](/jp/design/human-interface-guidelines/gauges#macOS)

macOSではゲージへの対応のほかに、範囲内の特定の数値を表示するレベルインジケータも定義されています。レベルインジケータは、容量、評価、（まれですが）関連性を表すように設定できます。

容量スタイルでは、断続的または連続的な値を表現できます。

![連続的な容量インジケータ。全体の容量の約3分の2が、デフォルトの緑の塗りつぶしで示されています。](https://docs-assets.developer.apple.com/published/8d1f4b040b7736a1ba832b93a7dc3bfb/indicators-continuous%402x.png)

**連続的。** 半透明の水平なラインを塗りつぶすことで、現在の値を示しています。

![断続的な容量インジケータ。全体の容量の4分の3が、デフォルトの緑の塗りつぶしで示されています。](https://docs-assets.developer.apple.com/published/f148e7934177391449aa61cc97ffea49/indicators-discrete%402x.png)

**断続的。** サイズが同じ長方形のセグメントがほぼ隙間なく水平に並んでいます。セグメントの総数で全体の容量を表しています。部分的にではなく完全に塗りつぶされたセグメントによって、現在の値が示されています。

**大きい範囲には連続的なスタイルを使用する。** 断続的な容量インジケータを使って、大きい範囲にわたる値を有意な精度で表そうとすると、セグメントを過剰に細かくしなければなりません。

**塗りつぶしの色を変化させて範囲の中の重要な部分を強調する。** デフォルトでは、どちらの容量インジケータスタイルも塗りつぶしの色は緑です。アプリによっては、現在の値が特定のレベルに達した（非常に低い、非常に高い、中間点を過ぎた）時点で塗りつぶしの色を変化させてもよいでしょう。インジケータ全体で塗りつぶしの色を変更するほか、下に示すように1つのインジケータ内で複数の色を並べて、段階的な状態を示す方法もあります。

![連続的な容量インジケータ。左端の8分の1は赤、次の8分の3は黄色、次の4分の1は緑で、最後の4分の1は塗りつぶされていません。](https://docs-assets.developer.apple.com/published/6d84b116ed12ffcabc2a36fb8f63e31e/indicators-continuous-tiered%402x.png)段階的な状態の表示

評価スタイルを使ってユーザに何かを簡単に評価してもらう方法についてのガイダンスは、[評価インジケータ](/jp/design/human-interface-guidelines/rating-indicators)を参照してください。

まれなユースケースですが、影付きの水平バーを使って関連性を表す、関連性スタイルもあります。例えば、検索結果のリストに関連性インジケータを表示して、ユーザが結果の関連性を視覚的に把握しながら、複数の項目を簡単に並べ替えたり比較したりできるようにするという用途が考えられます。

## [リソース](/jp/design/human-interface-guidelines/gauges#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/gauges#Related)

[評価およびレビュー](/jp/design/human-interface-guidelines/ratings-and-reviews)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/gauges#Developer-documentation)

[`Gauge`](/documentation/SwiftUI/Gauge) — SwiftUI

[`NSLevelIndicator`](/documentation/AppKit/NSLevelIndicator) — AppKit

## [変更履歴](/jp/design/human-interface-guidelines/gauges#Change-log)

日付| 変更内容  
---|---  
2022年9月23日| 新規ページ。

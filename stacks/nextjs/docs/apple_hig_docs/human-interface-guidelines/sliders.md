# スライダ

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/sliders

# スライダ

スライダはつまみと呼ばれるコントロールがついた水平なトラックで、ユーザが最小値から最大値の範囲で調整を行うためのコンポーネントです。

![図案化された明るさスライダ。画像は全体が、6色のオリジナルAppleロゴを連想させる赤色になっています。](https://docs-assets.developer.apple.com/published/5390b3c85b762073a3e1f307705224db/components-slider-intro%402x.png)

スライダの値が変更されると、最小値からつまみ位置までのトラックが塗りつぶされます。オプションで、左右に最小値と最大値を表すアイコンを表示できます。

## [ベストプラクティス](/jp/design/human-interface-guidelines/sliders#Best-practices)

**有用な場合は、スライダの見た目をカスタマイズする。** アプリのデザインになじませたり、意図を効果的に伝えたりするため、トラックの色、つまみの画像や色合い、左右のアイコンなどのスライダの見た目を調整できます。例えば画像のサイズを調整するスライダなら、左側に小さな画像アイコン、右側に大きな画像アイコンを表示できます。

**スライダの方向をシステムやほかのアプリと合わせる。** ほとんどのユーザにとってスライダは、どのアプリでも最小値が先頭側で最大値が末尾側（水平スライダの場合）、または最小値が下で最大値が上（垂直スライダの場合）になっているコンポーネントです。例えば水平スライダは、0%が先頭側、100%が末尾側になっているのが普通です。

**対応するテキストフィールドやステッパーでスライダを補完する。** 特にスライダが広い範囲の値を表す場合は、テキストフィールドでスライダの正確な値を確認したり、特定の値を入力したりできるようにすると効果的です。ステッパーを追加すると、値を一定の幅で簡単に増減できます。関連するガイダンスは、[テキストフィールド](/jp/design/human-interface-guidelines/text-fields)および[ステッパー](/jp/design/human-interface-guidelines/steppers)を参照してください。

![目盛りのない水平直線スライダの図。末尾側にテキストフィールドとステッパーがあります。つまみはスライダの中央にあり、テキストフィールドに50%と表示されています。](https://docs-assets.developer.apple.com/published/51010448e5e61de3a6271ef895d88a0b/sliders-text-field%402x.png)

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/sliders#Platform-considerations)

 _tvOSには対応していません。_

### [iOS/iPadOS](/jp/design/human-interface-guidelines/sliders#iOS-iPadOS)

**オーディオの音量調整にスライダを使用しない。** アプリで音量コントロールが必要な場合は、ボリュームビューを使用してください。ボリュームビューはカスタマイズ可能で、音量レベルスライダとアクティブなオーディオ出力デバイスを変更するためのコントロールが含まれています。ガイダンスは、[オーディオの再生](/jp/design/human-interface-guidelines/playing-audio)を参照してください。

### [macOS](/jp/design/human-interface-guidelines/sliders#macOS)

macOSのスライダには目盛りをつけることができます。範囲内の値をピンポイントで指定しやすくなります。

目盛りありと目盛りなしの直線スライダでは、つまみは角の丸い小さな長方形で、最小値とつまみの間のトラックが塗りつぶされます。多くの場合、直線スライダには最小値と最大値の意味を表す補助アイコンが含まれます。

円形スライダでは、つまみは小さい円で表されます。目盛りがある場合は、スライダの円周に等間隔に点が表示されます。

![水平スライダの図。中央につまみがあります。トラックの先頭部分からつまみまで、青いハイライトカラーで塗りつぶされています。](https://docs-assets.developer.apple.com/published/92445cf683c4dc1b179fb5359a0bdb28/sliders-no-tick-marks%402x.png)目盛りのない直線スライダ

![水平スライダの図。スライダ中央の2つの目盛りの間につまみがあります。トラックの先頭部分からつまみまで、青いハイライトカラーで塗りつぶされています。](https://docs-assets.developer.apple.com/published/e31ef9e35e8675bd62f695ba6a988a51/sliders-tick-marks%402x.png)目盛りのある直線スライダ

![円形スライダの図。つまみは12時の位置にあります。](https://docs-assets.developer.apple.com/published/3f253ed199e7e92b6124e6161dd79152/sliders-circular%402x.png)円形スライダ

**スライダの値が変化したらすぐにフィードバックを返す。** その場ですぐにフィードバックを返すと、ユーザはリアルタイムで結果を確認できます。例えば、「Dock」設定の「サイズ」スライダを調整すると、「Dock」のアイコンサイズがすぐに変わります。

**ユーザが違和感を抱かないスライダのスタイルを選択する。** 水平スライダは、固定された開始点と終了点との間の移動に最適です。例えば、グラフィックスアプリでオブジェクトの不透明度レベルを0%と100%の間で設定する場合は、水平スライダが適しています。円形スライダは、値の上限下限がなく、何度でも繰り返せる場合に使用します。例えば、グラフィックスアプリでオブジェクトの回転を0度と360度の間で調整する場合は、円形スライダが適しています。アニメーションアプリでは、円形スライダを使用してオブジェクトの回転数を調整できます。4回転は360度x4で1440度になります。

**スライダにラベルを付ける。** 通常、ラベルでは[センテンススタイルの大文字化（英語の場合）](https://help.apple.com/applestyleguide/#/apsgb744e4a3?sub=apdca93e113f1d64)を使用し、末尾をコロンにします。ガイダンスは、[ラベル](/jp/design/human-interface-guidelines/labels)を参照してください。

**明確さと精度を向上させるために目盛りを使用する。** 目盛りを使用すると、ユーザが値の調整範囲を把握したり、特定の値を見つけたりしやすくなります。

![macOSの「省エネルギー」設定パネルの一部。操作が行われなくなったあとディスプレイをオンにしたままにする時間を調整するスライダが強調表示されています。](https://docs-assets.developer.apple.com/published/43f38d85d553ee0f3551579716d33b76/sliders-labels%402x.png)

**さらに明確にするために目盛りにラベルを追加する。** スライダの値によって、ラベルは数値にすることも言葉にすることもできます。混乱を減らすために必要な場合を除き、すべての目盛りにラベルを付ける必要はありません。多くの場合、最小値と最大値にラベルを付けるだけで十分です。「省エネルギー」設定パネルのように、スライダの値の変化量が一定でない場合は、ラベルを付けると分かりやすくなります。ユーザがつまみにポインタを合わせるとその値が表示される[ツールチップ](https://developer.apple.com/jp/design/human-interface-guidelines/offering-help#macOS-visionOS)を設けるのもおすすめです。

### [visionOS](/jp/design/human-interface-guidelines/sliders#visionOS)

**横方向のスライダが望ましい。** ユーザには、縦方向よりも横方向のジェスチャの方が一般的に簡単です。

### [watchOS](/jp/design/human-interface-guidelines/sliders#watchOS)

スライダは有限の値の範囲を表す水平トラックで、一定の区切りごとに増減するか、連続したバーとして表示されます。スライダの両端にあるボタンをタップすると、あらかじめ定義された量で値が増減します。

![一定の区切りごとに増減するwatchOSの音量スライダの図。3つのうち最初の2つの区切りが、音量レベルを示す緑のハイライトカラーで塗りつぶされています。](https://docs-assets.developer.apple.com/published/3acc4339289d9cf65ec982e73f950f97/sliders-watchos-discrete%402x.png)断続的

![連続したバーがあるwatchOSの音量スライダの図。バーの3分の2が、音量レベルを示す緑のハイライトカラーで塗りつぶされています。](https://docs-assets.developer.apple.com/published/b356f0616bad32afce9ac9e62763414b/sliders-watchos-continuous%402x.png)連続的

**必要な場合は、カスタムのグリフを作成してスライダの目的を伝える。** デフォルトでは、プラス記号とマイナス記号が表示されます。

## [リソース](/jp/design/human-interface-guidelines/sliders#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/sliders#Related)

[ステッパー](/jp/design/human-interface-guidelines/steppers)

[ピッカー](/jp/design/human-interface-guidelines/pickers)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/sliders#Developer-documentation)

[`Slider`](/documentation/SwiftUI/Slider) — SwiftUI

[`UISlider`](/documentation/UIKit/UISlider) — UIKit

[`NSSlider`](/documentation/AppKit/NSSlider) — AppKit

## [変更履歴](/jp/design/human-interface-guidelines/sliders#Change-log)

日付| 変更内容  
---|---  
2023年6月21日| visionOSのガイダンスを追加するために更新。
